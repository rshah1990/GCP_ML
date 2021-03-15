import os
import pickle
import numpy as np
from sklearn.externals import joblib
import pandas as pd
import sys
from google.cloud import bigquery
from google.oauth2 import service_account
from google.cloud import storage
import logging
import google.cloud.logging
client = google.cloud.logging.Client()
client.setup_logging()


def pre_process(data):
    col=['sex', 'Year.end.age', 'height', 'body.weight', 'BMI',
       'Abdominal.circumference', 'Systolic.blood.pressure',
       'Diastolic.blood.pressure', 'Neutral.fat', 'Drug.1..blood.pressure.',
       'History.history.1..cerebrovascular.', 'History.2..cardiovascular.',
       'smoking', 'Exercise.habits.of.30.minutes.or.more',
       'Walking.or.physical.activity', 'Walking.speed', 'Eating.habit',
       'Drinking', 'sleep']
    df = pd.DataFrame(data,columns=col)
    
    df.sex.replace({'female':"2",'male':"1"},inplace=True)
    df.smoking.replace({'yes':"2",'No':"1"},inplace=True)
    df['Walking.speed'].replace({'high':"2",'low':"1"},inplace=True)
    
    return df.values

def export_items_to_bigquery(data,pred):
    credentials = service_account.Credentials.from_service_account_info()

    bigquery_client = bigquery.Client(project="advance-vector-233712",credentials=credentials)

    # Prepares a reference to the dataset
    dataset_ref = bigquery_client.dataset('dataset_logging')

    table_ref = dataset_ref.table('drift_detection')
    table = bigquery_client.get_table(table_ref)  # API call

    new_data = []
    for index,row in enumerate(data.tolist()):
        row.append(str(pred[index]))
        row.append(None)
        new_data.append(row)
    logging.warning(type(new_data[0][0]))
    logging.warning(type(new_data[0][-2]))
    errors = bigquery_client.insert_rows(table, new_data)  # API request
    print(errors)
    assert errors == []


class MyPredictor(object):
    """An example Predictor for an AI Platform custom prediction routine."""

    def __init__(self, model):
        """Stores artifacts for prediction. Only initialized via `from_path`.
        """
        self._model = model

    def predict(self, instances, **kwargs):
        """Performs custom prediction.
        Preprocesses inputs, then performs prediction using the trained
        scikit-learn model.
        Args:
            instances: A list of prediction input instances.
            **kwargs: A dictionary of keyword args provided as additional
                fields on the predict request body.
        Returns:
            A list of outputs containing the prediction results.
        """
        inputs = np.asarray(instances)
        process_input = pre_process(inputs)
           
        # prediction
        outputs = self._model.predict(process_input)
        
        # post processing
        custom_out = ['diabetic' if i == 0 else 'Non-diabetic' for i in outputs]
        
        export_items_to_bigquery(process_input,outputs)

        return custom_out

    @classmethod
    def from_path(cls, model_dir):
        """Creates an instance of MyPredictor using the given path.
        This loads artifacts that have been copied from your model directory in
        Cloud Storage. MyPredictor uses them during prediction.
        Args:
            model_dir: The local directory that contains the trained
                scikit-learn model and the pickled preprocessor instance. These
                are copied from the Cloud Storage model directory you provide
                when you deploy a version resource.
        Returns:
            An instance of `MyPredictor`.
        """
        model_path = os.path.join(model_dir, 'model.joblib')
        model = joblib.load(model_path)

        return cls(model)
# Component of ML system 

- Data ingestion
  - For streaming data use Pub-sub
  - for structured data use big query 
  - to transform data & dump use cloud storage 
- Data analysis & validation
  - data analysis is to check distribution of data during training & inference to detect bug in data 
  - data validation is to check if data is healthy or not. you can ask below questions to detect bug
    - Is new distribution is similar to old one?
    - all expected features are present?
    - any unexpected feature are present ?
    - does features have expected type?
    - expected propotion of data is present?
    - expected number of values in feature?
- Data transformation: all transformation done during training should be part of inference. failing to do so can introduce training serving skew. data flow , data prep & data proc
- Trainer: to train model. it should support data & model parallelism. also it should scale to lage number of workers. ML engine & GKE
- Tuner : ML engine supports hyperparameter tuning
- Model evaluation & validation: 
  - in evaluation we care more about model safeness (likeliness to crash or taking more resources) & prediction quality
  - model validation using different slice of prediction (TFMA)
- serving: low latency, high efficent , scale horizontally & easy to update version . ML engine & TF serving 
- loging 
- Orchestration + Workflow: cloud composer if we are using GCP services & Argo for apache airflow (GKE) if we are using containerized application


# Design decision

- Training design decision 

![static_dynamic](https://user-images.githubusercontent.com/37735152/110774289-a675d980-8283-11eb-901f-298baa2c7fee.PNG)

- Serving design decision:
  - static vs dynamic serving: Precompute the predictions & store it for static serving. this will have faster response time but its resource intensive since we are caching the predicted results 
  - static vs dynamic serving decision can be taken using peakness & cardinality.
  - Peakness refers to the how concentrated prediction distribution is ex: next word prediction model is highly peaked since small amount of words represents majority predictions. 
  - Cardinality: refers to the number of values in the set for which we have to make prediction for. ex: customer life time value will have high cardinality since number of users can be really large

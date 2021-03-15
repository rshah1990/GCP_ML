# Custom Prediction Routine 

- custom prediction routine helps you to run python code when online prediction request comes to AI platform 
- this is perticularly usefule when pre-processing is not part of model or post-processing is required
- Two information is needed to run custom prediction routine 
  - GCS path for model (model.pkl / model.h5)
  - python source distribution package 

### Step 1: Upload model artifacts to your model directory
- upload trained model on cloud storage 
- size of model should be less than 500MB , to upload larger model request quota size

### Step 2: Create your Predictor class
- refer scikit-predictor.py file in custom_routine folder 

### Step 3: Package your Predictor and its dependencies
- You must package your Predictor as a .tar.gz source distribution package
- create setup.py file
- run python setup.py sdist --formats=gztar

### Step 4: Deploy your custom prediction routine

gcloud beta ai-platform versions create version-name \
  --model model-name \
  --runtime-version 2.2 \
  --python-version 3.7 \
  --origin gs://your-bucket/path-to-model-dir \
  --package-uris gs://your-bucket/path-to-staging-dir/my_custom_code-0.1.tar.gz \
  --prediction-class predictor.MyPredictor



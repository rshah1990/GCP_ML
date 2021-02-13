# Hyperparameter tuning in AI platform

## Step 1: Create pipeline
- AI platform -> Pipeline - > New instance -> Configure -> select checkbox (access to cloud API) -> create cluster
- this will create a cluster & deploy pipeline installation. you can validate this in Kubernetes Engine -> clutser
- click deploy at bottom which will create default storage for pipeline (gs://Project ID-kubeflowpipelines-default/). 

## Step 2: Code to Train model 
- create a function which will take hyperparameter as input 
- using FIRE library convery that function into command line interface.
- use hypertune to log different runs (hpt.report_hyperparameter_tuning_metric)

## Step 3: Custom container 
- create a docker file to create custom container which will be used by AI platform for distributed training. 
  - take base image & install required libraries
  - copy training code 
  - using cloud build create docker formatted image and push it to container registry
  
## Step 4: Hyperparameter YAML file 
- create config file to define hyperparameters , early stopping , parameter names & its values , max trials & goal (to maximise or minimize)

## Step 5: Submit job
- Submit job on AI platform  which will accept custom container image location & hyperparameter tuning config file.
- once job is completed, you can get best hyperparameter values in response object. 
- ! gcloud ai-platform jobs submit training $JOB_NAME \
                                      --region=$REGION \
                                      --job-dir=$JOB_DIR \
                                      --master-image-uri=$IMAGE_URI \
                                      --scale-tier=$SCALE_TIER \
                                      --config $/hptuning_config.yaml \
                                      -- \
                                      --dataset_path=$TRAINING_FILE_PATH \
                                      --hptune

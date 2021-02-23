# Containers
- AI platform training allows you to run job using containers. containers can be pre-defined or custom.
- advantage of custom container is that you can build custom containers using ML frameworks and versions as well as non-ML dependencies, libraries and binaries that are not otherwise supported on AI Platform Training

# Training with containers
- create a python code which will train your ML model. all the variables will be accepted as input to the function.
- to use custom container, Build a docker image with all the dependencies & push it to container registry , make sure AI platform have an access to that container registry
- store train & test data where custom containers have access to ex: GCS
- submit job using "ai-platform job submit" command & specify arguments in config.YAML file 
- AI platform training creates a job & allocates one or more VM based on the job configration (scaleTier)
- To monitor job
  - cloud logging
  - gcloud command 

# GPUs/TPUs  with custom containers

- Pre-install the CUDA toolkit and cuDNN in your container or use nvidia/cuda image as your base image is the recommended way to handle this.
- if you are using distributed training on tensorflow,can use TPUs on your worker VMs. configure training job to use TPU & tpuTfversion.

# Distributed training with custom containers

- To run distributed training on custom containers, you can use same image as master,worker & parameter server or different image for all nodes.
- In code, use the environment variables TF_CONFIG and CLUSTER_SPEC. 
- These environment variables describe the overall structure of the cluster, and AI Platform Training populates them for you in each node of your training cluster.
- Ex: you have defined three different image for each type of node, push it to container registry & submit training job 

    gcloud ai-platform jobs submit training $JOB_NAME \
      --region $REGION \
      --master-machine-type complex_model_m \
      --master-image-uri $MASTER_IMAGE_URI \
      --worker-machine-type complex_model_m \
      --worker-image-uri $WORKER_IMAGE_URI \
      --worker-count 9 \
      --parameter-server-machine-type large_model \
      --parameter-server-image-uri $PS_IMAGE_URI \
      --parameter-server-count 3 \
      -- \
      --model-dir=gs://$BUCKET_NAME/$MODEL_DIR \
      --epochs=10

# Monitoring model versions

- Model (Lung cancer) -> version (V1,V2..)
- we can monitor your model's traffic patterns, error rates, latency, and resource utilization to spot problems in ML system
- this pattern can help you to find right type of machine to optimize latency & cost

### Performance Tab
- **Predictions**: The number of predictions per second. counted at instance level 
- **Errors**: errors is usually a sign that something is wrong with the model or the requests to the model
- **Model latency and Total latency** : Model latency is the time spent performing computation.Total latency is the total time the request spends in the service
### Resource usage Tab
- **Replica** : The number of replicas for your version
- **CPU usage, Memory usage, Accelerator average duty cycle, and Accelerator memory usage**: The version's CPU, GPU, and memory utilization, per replica
- **Network bytes sent and Network bytes received** :The job's network usage

# Monitoring training jobs

- AI platform -> Jobs
- The job's aggregate CPU or GPU utilization, and the memory utilization. 
- These are broken down by master, worker, and parameter server.
- The job's network usage, measured in bytes per second. There are separate charts for bytes sent, and bytes received
- **Monitoring with TensorBoard*
  - save summary data to cloud storage 
  - launch tensorboard from cloud shell
  - point TensorBoard to a directory with subdirectories that contain the output from multiple jobs

# Continuous Model Evaluation

- Continous evaluation regularly samples prediction input & output from trained machine learning models that is deployed on AI platform 
- For ground truth label, you can provide it by your own or opt for data labelling service 
- model evaluation is done at model version level. (Model (cancer) can have multiple version inside it)
- input & output of some online predictions is saved in Big query, we can customize how many data gets sampled. it does not sample batch predictions
- big query table will have ground truth column which needs to be populated to get metrics 
- Continuous Model Evaluation supports many type of models. for image classification, text classification & object detection data labelling service is available but for general classification user has to provide ground truth label
- you need to mention few keys by which Data Labeling Service can extract necessary information.
  - Data key: input data key of JSON 
  - Data reference key: for image this is image path 
  - Prediction label key: for image classification this could be labels (key of dictionary)
  - Prediction score key: ex: confidence
  - Bounding box key
- When Data Labeling Service runs an evaluation job, it produces a set of evaluation metrics that vary depending on the specifics of your machine learning model
- you can also Compare mean average precision across models


# Issues while using Deep learning VM

- Quota exceeded: not enough GPU/TPU quota, request for quota increase
- Resource not found : trying to use GPU in region where GPU is not available 
- Preemptible instances:  can't create preemptible instance from the UI, even though you have quota. use command line argument

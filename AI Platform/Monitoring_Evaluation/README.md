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

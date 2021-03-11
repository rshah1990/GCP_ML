# Online versus batch prediction

| Online prediction	  | Batch prediction |
| ------------- | ------------- |
| Optimized to minimize the latency of serving predictions.  | Optimized to handle a high volume of instances in a job and to run more complex models.|
| Can process one or more instances per request.  | Can process one or more instances per request. |
| Predictions returned in the response message.	 | Predictions written to output files in a Cloud Storage location that you specify. |
| Input data passed directly as a JSON string. | Input data passed indirectly as one or more URIs of files in Cloud Storage locations. |
| Returns as soon as possible. | Asynchronous request. |
| Runs models deployed to AI Platform Prediction.| Runs models deployed to AI Platform Prediction or models stored in accessible Google Cloud Storage locations. |
| resource is allocated all the time.| allocates resource when request is sent |
|{"image": [0.0, 0.0, ... ], "key": 0} /n {"image": [0.0, 0.0, ... ], "key": 1} /n  {"image": [0.0, 0.0, ... ], "key": 2}| {"instances": [{"values": [1, 2, 3, 4], "key": 1}]}|

# Deployment

- whenever you update specification of POD new pod is created with the new specification so it can be controlled 
- if updated pods are not stable rollback pod to previous version
- pods can be scaled manually or auto scale 
- well suited for statless application 
- desired state is describe in deployment.YAML. once it is submitted to master it will convert into deployment controller
- below is the example for the sample deployment file where we have specified number of replicas & specification
- Deployment can be created using three ways 
  - $kubectl deployment -f [DEPLOYMENT_FILE]
  - $kubectl run [DEPLOYMENT_NAME] <br/>
                  --image [IMAGE:TAG]<br/>
                  -- replica 3 <br/>
                  --label [KEY]:[VALUE] <br/>
                  --port 8080
  - UI

- to inspect deployment: $kubectl get deployment [DEPLOYMENT_NAME]
- to get more details: $kubectl describe deployment [DEPLOYMENT_NAME]   

![deploy_yaml](https://user-images.githubusercontent.com/37735152/111058067-f20dca80-84b1-11eb-8d6f-100dbed46210.PNG)

# Scaling

- $kubectl scale deployment [DEPLOYMENT_NAME] - replicas 5
- Autoscale : $kubectl scale deployment [DEPLOYMENT_NAME]  -min 5 -max 15 --cpu-percent=75
- threshing : its problem with auto scaling when scale up & down fluctuates very fast. it happens when the matrix you measure to scale fluctuates very fast 

# Updating Deployment 

- if the base image of the pod changes than we can change YAML file & update the pods </br>
  $kubectl apply -f [DEPLOYMENT_FILE]

# Blue Green Deployments

- all the replicas will change at once
- you have two identical environments (infrastructure) with the “green” environment hosting the current production apps
- when you’re ready to make a change to app2 for example and upgrade it to v2, you’d do so in the “blue environment”.
-  In that environment you deploy the new version of the app, run smoke tests, and any other tests (including those to exercise/prime the OS, cache, CPU, etc). When things look good, you change the loadbalancer/reverse proxy/router to point to the blue environment.

![blue-green](https://user-images.githubusercontent.com/37735152/111058979-3f8d3600-84b8-11eb-83fc-e1838e417922.png)

# A/B Testing

- A/B testing is primarily used to review the effectiveness of a change and how the market reacts to the change

 
![A_B](https://user-images.githubusercontent.com/37735152/111059021-75cab580-84b8-11eb-94db-941c26881bfe.png)

- The new features will be rolled out to a certain set of users

# Canary releases

- A Canary release is moving a new product or feature to a certain community before fully rolling out to all customers
- subset of traffic can be directed to new version & gradually all traffic can be moved to new version

![canary](https://user-images.githubusercontent.com/37735152/111059034-8713c200-84b8-11eb-919c-92e57b044257.PNG)


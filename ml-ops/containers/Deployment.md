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

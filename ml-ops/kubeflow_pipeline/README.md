# Kubeflow 

- Kubeflow provides standardized platfom for building ML pipelines & build on top of kubernetes 
- kubeflow is build on three principle composability, protability & scalability

# Kubeflow Components

- hosted jupyter notebook: kubeflow installation comes with hosted jupyter notebook. it can dynamically scale resources
- katlib - used for automated hyperparameter tuning 
- kubeflow pipeline: based on containers so each step is portable. same pipeline code can be run across environment
- KFServing: helps to server ML model built on Knative. it can also be served using TF serving 
- metadata management: managing artifcates produces by ML pipelines & metadata (track runs,model info, dataset, description & types of model). it uses MLMD

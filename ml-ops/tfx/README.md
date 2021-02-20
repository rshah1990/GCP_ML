# Architecture 

<Image>

- TFX is production pipeline ML framework based on tensorflow
- TFX pipeline is sequence of components connected by channels in DAG of artifactes dependencies
- For each major phase of ML pipeline TFX has components available, all those components will be run by orchestration engine (Beam,Apache Airflow, Kubeflow)
- TFX supports four major deployment targets, its portal to on-premise or cloud service 
- TFX can scale up processing using dataflow for large scale processing 
- can run pipeline parallely (different set of splits, hyperparameter,architecture)
- TFX used ML metadata(MLMD API) store for artifactes management. its task & data aware pipeline i.e. if feature transformation is same than it wont calculate it again, just reuse the last one. its uses MY SQL or postgrad database

# How it works

- Each step of TFX pipeline (components) produces and consumes artifactes. this is how two components communicates in pipeline.
- each TFX components has five elements 
  - **Config file**: run time parameters & input/output artifactes
  - **Drivers**: coordinates job execution such as reading artifcates location from ML metadata store, retriving pipeline from pipeline artifactes store 
  - **Executor**: implements actual code such as data processing & model training 
  - **Publisher**: updates metadata store
  - **Component interface**: package component specification & executor for use in pipeline
  
  
  # TFX components
  
  ### **ExampleGen**: 
  - data ingestion pipeline,usually first component of pipeline
  - its supports CSV, TF record, Avro, Parquet & also customizable to new input format
  - It will split data into train & eval bydefault, can define output config file to customize the split
  - for different split it can version data 
  - convert examples in tf.Example format & copy data to TFX root directory for other component to access in TF record format
  - it uses Apache Beam for scalable data ingestion. 
  
  ### **StatisticGen**: 
  - computes statistics over dataset for data analysis 
  - it uses tensorflow data validation library & apache beam for processing 
 
  ### **SchemaGen**: 
   - generates schema on the basis on data statistics & it also uses data validation library 
   - it will take input as output of staticgen
   - Each feature in your dataset shows up as a row in the schema table, alongside its properties.
   - The schema also captures all the values that a categorical feature takes on, denoted as its domain

  ### **ExampleValidator**: 
    - detects anomalies in data, train-serve skew & data drift based on the expectations defined by the schema
    
  ### **Transform**: 
    - does feature engineering for both training & serving 
    - it takes input as examplegen, schemagen & python script for transform code
    - it produces two types of output. Tensorflow graph (can perform pre-processing operation ) & tensorflow examples (processed training & eval data) 
    
  ### **Trainer**:
    - Train model defined in Tensorflow. Default trainer supports estimator API , for Keras model specify generic trainer
    - takes input of schemagen , transformed graph , training parameters & user define code 
    - trainer artifcates can be analyzed using tensorboard
    - dumps one model in tensorflow saved model format & another model for evaluation which will be used by evaluator component 
    
  ### **Tuner**:
    - uses python keras tuner API for hyperparameter tuning 
    - can use cloud AI platform optimizer for distributed tuning 
    
  ### **Evaluator**:
    - uses tensorflow model evaluation llibrary across split & slices
    - validate model performance to flag if its good enough for production 
    - as an output it dumps model evaluation metrics & model blessing (ready for production)
   
  ### **InfraValidator**:
    - it will validate model 

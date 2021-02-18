# Basics
- Big query is fully managed data warehousing solution and not transactional 
- Big query structure -- Project -> Dataset ->Table -> Job (query)
- IAM role can be applied at project or dataset level but cant control at table level. 
- to share few specific tables, create view from those tables and define IAM role at view level 
- materilized view is also supported in big query (BETA)
- dataset can be public or for all authenticated users

# How big query works
- In big query storage and compute are separated and connected with petabit network called Jupiter
- It stores data in columnar format (in colossus) contrary to traditional RDBMS system which is stored row format (record oriented)
- Big query has extremely fast performance on read but poor on write 

# Cost saving in big query 
- How cost is calculated:
  - How many bytes read/written? (I/O operation)
  - How much passed between machine & next stage (Shuffle)
  - CPU work
- **Caching query**: Big query supports caching of a previous query which can save the cost.**Caching is per user only**
  - **Note: if want to create dashboard then create superuser and let all user access dashboard using super user so that query can be cached**
- **Import Data**: To import TB of data best performance is given by Avro- compressed format.  This will reduce IO operation
- **Data denormalization**: De-normalize data (group table together with repeated data) when possible which is good for read performance & not write
- **Query optimization**: 
  - Avoid select * 
  - Filter early and big with where clause. This will reduce since less data is passed to next stage
  - Do biggest join first 
- **Partitioning**:
  - consider a scenario where big retail chain dumps their sales data in big query to analyze further and create reports, most of the time they want to see last quarter sales. In this case partitioning data on the basis of Date will help so that big query won’t scan entire data. 
  - You can partition by CREATION DATE or other TIMESTAMP or DATE column.
  - The new partition is introduced is Time unit partitioning. This will give us much granular control over partition. So now partition can be created on Hour to Year basis (PARTITION BY timestamp_trunc(datetime, [HOUR/YEAR]))
- **Clustering**:
  - What if I want to partition on the basis of the text value, that’s when clustering comes into picture 
  -	Continuing previous scenario, let’s assume you want to query quarterly sales data for specific stores, so we can create clustering on the store name column. 
  -	We can cluster on multiple columns ex: store & product but order is really important (CLUSTER BY STORE, PRODUCT). In this case if user filter by STORE/ STORE+ PRODDUCT clustering will help but if user only filters by PRODUCT clustering won’t work

# ML with big query 

- **Train model**:
  
  CREATE MODEL `model name` \
  OPTIONS \
  (MODEL_TYPE=` `, INPUT_LABLE_COL = [‘Target col’]) \
  AS \
  (SELECT * FROM TABLE)
 
- **Training Metrics**: Click on model --> evaluation tab 
- **Evaluate on new data**: In background, bq has already splitted data in train/test set, when we run this query it returns test set results

  SELECT * FROM \
  ML.EVALUATE \
  (MODEL `model name`, \
  SELECT * FROM TABLE)
  
- **Predict on new data**:
 
  SELECT * FROM \
  ML.PREDICT \
  (MODEL `model name`, \
  SELECT * FROM TABLE)

- **Model deployment**:
  - **Data pre-processing/Feature creation is a part of code. Input features should be exactly same of data in table**
  - **deploy in local**:
       - Export model file in google cloud storage
       - All TensorFlow based model will be exported as TensorFlow Saved Model
       - AUTOML will be exported as container
       - XG Boost will be deployed as custom prediction routine. We can download and edit those files in Python as well
  - **deploy on cloud**:
       - Export model to google cloud storage
       - Use AI platform to deploy model for online prediction
       - AUTOML models does not supports this

- **Supported Model Type**:
    1.	Linear Regression 
    2.	Binary logistic regression 
    3.	Multi class logistic regression
    4.	K-means clustering 
    5.	Matrix factorization for recommendation system 
    6.	Time series 
    7.	Boosted tree
    8.	DNN
    9.	AUTOML tables 
    10.	Import previously trained TensorFlow models 

# Limitation:
- Can only export to cloud storage 
- Can only export up to 1GB per file, but can be split to multiple files using wild card 
(bq extract ‘projectid.dataset.table’ ‘gs://my-bucket/file-name-*.json)
- Load multiple files using command line and not from UI
- Limited to 1000 table per dataset

 



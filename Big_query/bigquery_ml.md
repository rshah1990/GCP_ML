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

# Use Delta Lake in Azure Databricks

Delta Lake is an open source relational storage area for Spark that you can use to implement a `data lakehouse architecture` in Azure Databricks.

**Data lakehouse architecture**
Provides advantages of a relational database system with the flexibility of data file storage in a data lake


## Introduction
- Describe core features and capabilities of Delta Lake.
- Create and use Delta Lake tables in Azure Databricks.
- Create Spark catalog tables for Delta Lake data.
- Use Delta Lake tables for streaming data.


## Get Started with Delta Lake
- Is an open-source `storage layer`
- Adds relational db semantics to Spark based datalake processing
- Supported in Azure Synapse Analytics
- Underlying data for Delta lake is stored in `Parquet format`
- Benefits
    - Relational tables that support querying and data modification (`CRUD`)
    - Support for `ACID` transactions
    - Data versioning and `time travel` (Retrieve prev-ver of row in query).
    - Support for batch and streaming data usign `Spark API`

## Creating a Delta Lake table from a dataframe

```python
# Load a file into a dataframe
df = spark.read.load('/data/mydata.csv', format='csv', header=True)

# Save the dataframe as a delta table
delta_table_path = "/delta/mydata"
df.write.format("delta").save(delta_table_path)

# replace an existing Delta Lake table with the contents of a dataframe by using the overwrite mode
new_df.write.format("delta").mode("overwrite").save(delta_table_path)

# Add rows from a dataframe to an existing table by using the append mode
new_rows_df.write.format("delta").mode("append").save(delta_table_path)

# Data modifications in a dataframe and then replace a Delta Lake table by overwriting it, a more common pattern in a database is to insert, update or delete rows in an existing table as discrete transactional operations, use  DeltaTable object in the Delta Lake API, which supports update, delete, and merge operations.

from delta.tables import *
from pyspark.sql.functions import *

# Create a deltaTable object
deltaTable = DeltaTable.forPath(spark, delta_table_path)

# Update the table (reduce price of accessories by 10%)
deltaTable.update(
    condition = "Category == 'Accessories'",
    set = { "Price": "Price * 0.9" })


# Querying a previous version of a table - time travel.
df = spark.read.format("delta").option("versionAsOf", 0).load(delta_table_path)

# specify a timestamp by using the timestampAsOf option:
df = spark.read.format("delta").option("timestampAsOf", '2022-01-01').load(delta_table_path)
```

## Create and query catalog tables

Delta Lake table instances created from dataframes and modified through the Delta Lake API. You can also define `Delta Lake tables` as `Catalog tables` in the `metastore` and `work with them using SQL`.

Two types of Tables:
- External
    - An external table is defined for a custom file location, where the data for the table is stored. The metadata for the table is defined in the Spark catalog. Dropping the table deletes the metadata from the catalog, but doesn't affect the data files.
- Managed
    - A managed table is defined without a specified location, and the data files are stored within the storage used by the metastore. Dropping the table not only removes its metadata from the catalog, but also deletes the folder in which its data files are stored.


```python
# Creating a catalog table from a dataframe
# Save a dataframe as a managed table
df.write.format("delta").saveAsTable("MyManagedTable")

## specify a path option to save as an external table
df.write.format("delta").option("path", "/mydata").saveAsTable("MyExternalTable")


# Creating a catalog table using SQL
spark.sql("CREATE TABLE MyExternalTable USING DELTA LOCATION '/mydata'")

# Using the DeltaTableBuilder API
from delta.tables import *

DeltaTable.create(spark) \
  .tableName("default.ManagedProducts") \
  .addColumn("Productid", "INT") \
  .addColumn("ProductName", "STRING") \
  .addColumn("Category", "STRING") \
  .addColumn("Price", "FLOAT") \
  .execute()


```

```SQL
%sql

CREATE TABLE MyExternalTable
USING DELTA
LOCATION '/mydata'

-- Defining the table schema
%sql

CREATE TABLE ManagedSalesOrders
(
    Orderid INT NOT NULL,
    OrderDate TIMESTAMP NOT NULL,
    CustomerName STRING,
    SalesTotal FLOAT NOT NULL
)
USING DELTA

-- Using catalog tables
%sql

SELECT orderid, salestotal
FROM ManagedSalesOrders
```

## Use Delta Lake for streaming data

- We've explored up to this point has been `static data in files`.
- Data analytics scenarios involve `streaming data` that must be processed in near real time
- `For example`, you might need to capture readings emitted by internet-of-things (IoT) devices and store them in a table as they occur.

1. Spark Structured Streaming
- constantly reading a stream of data from a source,
- optionally processing it to select specific fields, aggregate and group values
- writing the results to a sink
- All this using: Spark includes native support for streaming data through Spark Structured Streaming, an API
- A Spark Structured Streaming dataframe can read data from many different kinds of streaming source, including *network ports*, *real time message brokering services such as Azure Event Hubs or Kafka*, or *file system locations*.

2. Streaming with Delta Lake tables
- Use a Delta Lake table as a source or a sink for Spark Structured Streaming

- `Using a Delta Lake table as a streaming source`
    In the following PySpark example, a Delta Lake table is used to store details of Internet sales orders. A stream is created that reads data from the Delta Lake table folder as new data is appended.

    ```python
    from pyspark.sql.types import *
    from pyspark.sql.functions import *

    # Load a streaming dataframe from the Delta Table
    stream_df = spark.readStream.format("delta") \
        .option("ignoreChanges", "true") \
        .load("/delta/internetorders")

    # Now you can process the streaming data in the dataframe
    # for example, show it:
    stream_df.show()

    # Only append operations can be included in the stream. Data modifications will cause an error unless you specify the ignoreChanges or ignoreDeletes option
    ```

- `Using a Delta Lake table as a streaming source`
    In the following PySpark example, a stream of data is read from JSON files in a folder. The JSON data in each file contains the status for an IoT device in the format {"device":"Dev1","status":"ok"} New data is added to the stream whenever a file is added to the folder. The input stream is a boundless dataframe, which is then written in delta format to a folder location for a Delta Lake table.

    ```python
    from pyspark.sql.types import *
    from pyspark.sql.functions import *

    # Create a stream that reads JSON data from a folder
    streamFolder = '/streamingdata/'
    jsonSchema = StructType([
        StructField("device", StringType(), False),
        StructField("status", StringType(), False)
    ])
    stream_df = spark.readStream.schema(jsonSchema).option("maxFilesPerTrigger", 1).json(inputPath)

    # Write the stream to a delta table
    table_path = '/delta/devicetable'
    checkpoint_path = '/delta/checkpoint'
    delta_stream = stream_df.writeStream.format("delta").option("checkpointLocation", checkpoint_path).start(table_path)

    # To stop the stream of data being written to the delta table
    delta_stream.stop()
    ```

    To see the latest data in the sink Delta Table can be viewed by

    ```sql
    %sql

    CREATE TABLE DeviceTable
    USING DELTA
    LOCATION '/delta/devicetable';

    SELECT device, status
    FROM DeviceTable;
    ```

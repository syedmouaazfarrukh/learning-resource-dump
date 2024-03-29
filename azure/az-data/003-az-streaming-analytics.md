# Azure Streaming Analytics

Course Details:
- [Implement a Data Streaming Solution with Azure Stream Analytics](https://learn.microsoft.com/en-us/training/paths/implement-data-streaming-with-asa/)

## Get started with Azure Stream Analytics
- Cloud-based stream processing engine that you can use to filter, aggregate, and otherwise process a real-time stream of data from various sources
- PaaS service

- What is a Data Stream?
    - Series of data, typically related to specific point-in-time events
    - Need of Stream analytics
        - Continuously analyzing data to report issues or trends.
        - Understanding component or system behavior to help plan future enhancements.
        - Triggering specific actions/alerts when certain events occur or thresholds are exceeded.
    - Characteristics
        - Unbounded data stream
        - Each data object is timestamped
        - Data aggregation is performed over `Temporal windows`
        - ![Stream-Characteristics](src/stream-characteristics.png)

- Stream Analytics is for complex event processing/analysis of streaming data
    - Analytics is used to:
        - `Ingest data` from an input: *Azure IoT Hub*, or *Azure Storage blob container*.
        - `Process data` using a query
        - `Write outputs` to *Azure Data Lake Gen 2*, *Azure SQL Database*, *Azure Synapse Analytics* etc
    - Guarantees `once event processing` and `at-least once event delivery`
    - Provides checkpoints to maintain/check etl jobs

- ASA Jobs & Clusters
    - Jobs will process the data
    - Inputs
        - Azure Event Hubs
        - Azure IoT Hub
        - Azure Blob storage
        - Azure Data Lake Storage Gen2
        - *Can `reference inputs` used to ingest static data to augment the real-time event stream data.*
    - Outputs
        - Supports a wide range of outputs
            - loads them into a data lake or data warehouse
            - Append data to a dataset in Power BI
            - Writes the results of stream processing to an event hub.
    - Queries
        - EventProcessedUtcTime
        - When using an *Event Hubs input*, a field named EventQueuedUtcTime to record time of event queued in Hub

- Windows Function
    - To aggregate events into temporal intervals, or windows
        - EG: To count the number of social media posts per minute or to calculate the average rainfall per hour.
    - Five kinds
        - Tumbling: contiguous series of fixed-size, non-overlapping time segments, one event per tumbling window, `TumblingWindow()`
        - Hopping: models scheduled overlapping windows,  Tumbling windows that can overlap, have a hop size, events can belong to more windows, must have 3 parameters (1: time unit, 2: window size, 3: hop size , *4: offset*), `HoppingWindow()`
        - Sliding: generate events for points in time when the content of the window actually changes, `SlidingWindow()`
        - Session: functions cluster together events that arrive at similar times, filtering out periods of time where there's no data. It has three primary parameters: timeout, maximum duration, and partitioning key (optional). `SessionWindow()` 
        - Snapshot: groups events by identical timestamp values `System.Timestamp()`


### Ingest streaming data using `Azure Stream Analytics` and `Azure Synapse Analytics`

- Common stream ingestion scenarios for Azure Synapse Analytics.
    - A real-time source of data is captured in an event ingestor, such as Azure Event Hubs or Azure IoT Hub.
    - The captured data is perpetually filtered and aggregated by an Azure Stream Analytics query.
    - The results of the query are loaded into a data lake or data warehouse in Azure Synapse Analytics for subsequent analysis.

    - Two common approaches for large-scale data analytics:
        1. Data warehouse - Relational
            - Provides dedicated SQL pools(massively parallel processing (MPP)) for data warehouses
            - For Stream Analytics to write into such warehouse, output should be pointed/referenced to tables

        2. Data Lake - File storage
            - Atleast one storage device (Storage account container is common)
            - Files are organized hierarchically in directories (folders)
            - Azure Stream Analytics query must write its results to an output that references the location in the Azure Data Lake Gen2 storage container where you want to save the data files

- Configure inputs and outputs for an Azure Stream Analytics job.

- Define a query to ingest real-time data into Azure Synapse Analytics.
- Run a job to ingest real-time data, and consume that data in Azure Synapse Analytics.
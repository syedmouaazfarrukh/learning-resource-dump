# Azure Data Factory


1. **Pipelines:**
   - **Definition:** A set of data-driven and orchestrated activities. They represent a workflow how data is moved, transformed, and processed.
   - **Purpose:** Used to organize/manage the flow of data from various sources to destinations by data movement, transformation, and control flow activities. Some activities are:

        - `Move and transform`
            - For moving and transforming data
            - Used to
                - Copy data between different data stores
                - Transform the data during the copy process
                - Perform various data manipulation tasks.
            - Example: You have data in Azure SQL Database and need to transform it before loading it into Azure Data Lake Storage. The pipeline would include activities to copy data from SQL Database to Data Lake Storage and perform necessary transformations in between.

        - Synapse
            - Designed for integrating with Azure Synapse Analytics (formerly SQL Data Warehouse). Includes activities for data movement, data transformation, and control flow specific to Azure Synapse Analytics.

        - Azure Data Explorer
        - Azure Function
        - Batch Service
        - Databricks
        - Data Lake Analytics
        - General
        - HDInsight
        - Iteration & conditionals
        - Machine Learning
        - Power Query





2. **Change Data Capture (CDC):**
   - **Definition:** Change Data Capture is a feature that identifies and captures changes made to data in the source systems. It helps to identify the inserts, updates, and deletes in the source data.
   - **Purpose:** CDC is often used in data integration scenarios where you want to keep a target system synchronized with changes happening in the source system. It allows you to efficiently process only the changed data.

3. **Datasets:**
   - **Definition:** Datasets represent the structure of your data. They define the schema and location of the data, including the format and connection information.
   - **Purpose:** Datasets are used to provide a logical representation of the data you want to use in your data workflows. They abstract the underlying details of the data source and destination, making it easier to design and maintain data pipelines.

4. **Dataflows:**
   - **Definition:** Dataflows in Azure Data Factory represent a sequence of data transformation and preparation steps that can be applied to your data.
   - **Purpose:** Dataflows are used to clean, transform, and shape your data before it gets loaded into the destination. They are often used for Extract, Transform, Load (ETL) processes to ensure that the data meets the required standards and is ready for analysis or reporting.

5. **Power Query:**
   - **Definition:** Power Query is a data connection technology that enables you to discover, connect, combine, and refine data across various sources.
   - **Purpose:** Power Query is used for data preparation and transformation. It allows users to connect to different data sources, perform transformations, and shape the data before loading it into the target system. It's often used in conjunction with Dataflows.

Each of these components plays a crucial role in building end-to-end data solutions in Azure Data Factory, offering flexibility and scalability in handling diverse data integration scenarios.
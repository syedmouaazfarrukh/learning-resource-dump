# SAP HANA Basics For Developers: SQLScript

## 7.1: Part 7.1 SQLScript Simple Procedure

In the WebIDE:
    go to DB
        go to src
            create a new folder (procedures)
            create a new procedure (get_po_header_data.hdbprocedure)
            `https://github.com/SAP-samples/hana-xsa-opensap-hana7/blob/snippets_2.3.2/ex2/ex2_17`
            
            There is a `Definer` and a `User` who has rights to run/access data. for read only, READ SQL DATA as and for non-read only it should be like `AS`

            Ignore client side error messages, focus on build status

            ![alt text](image.png)

            To check status, go to data explorer and from there stored procedures and then `get_po_header_data`
            then generate call statement, run it and you'll get data form table via stored procedures


## Part 7.2 SQLScript Scalar UDF (User Defined Function)

Has a Single output scalar parameter
Can be impebbed in a SQL statement rather than calling separate Statement like stored procedure

Go in db/src/functions/ create a new function (get_full_name.hdbfunction ) and paste `https://github.com/SAP-samples/hana-xsa-opensap-hana7/blob/snippets_2.3.2/ex2/get_full_name.sql`
change the stored procedure with this code:
`https://github.com/SAP-samples/hana-xsa-opensap-hana7/blob/snippets_2.3.2/ex2/get_po_header_data.sql` and build `db` again

Can check this in data explorer

## Part 7.3 SQLScript Table UDF

- Table function (single table output) - Scalar UDF (single scalar output)
- Looks like a view and can perform SELECT and other complex things
- Go to db/src/functions/ create a new function (`get_po_counts.hdbfunction`) and paste the following code `https://github.com/SAP-samples/hana-xsa-opensap-hana7/blob/snippets_2.3.2/ex2/get_po_counts2.sql` and build the db again and check from data explorer

## Part 7.4 SQLScript Libraries

Allows you to pull multiple stored procedures into a library with some shared variables and stuff
Go to db/src/libraries/ create a new database artifact `MasterData` and paste the code from `https://github.com/SAP-samples/hana-xsa-opensap-hana7/blob/snippets_2.3.2/ex2/MasterData.sql`
To access a library, create a new stored procedure and eet code from `https://github.com/SAP-samples/hana-xsa-opensap-hana7/blob/snippets_2.3.2/ex2/get_master_data.sql`

## Part 7.5 SQLScript Built-In Libraries

Collections of ready-to-use functions and procedures.
They help perform common tasks like math operations or string manipulation.
Convenient for developers to use without writing everything from scratch.

[Video Link](https://www.youtube.com/watch?v=cIpjz-pTJ_E&list=PL6RpkC85SLQABOpzhd7WI-hMpy99PxUo0&index=105)

## Part 7.6 SQLScript Anonymous Blocks

Pieces of code executed on-the-fly without saving.
Handy for quick tasks or testing without cluttering the database.
They vanish once executed, keeping the database clean.

[Video Link](https://www.youtube.com/watch?v=jFYM2PR-3CE&list=PL6RpkC85SLQABOpzhd7WI-hMpy99PxUo0&index=104)

## Part 7.7 SQLScript Table Manipulation

Actions like adding, updating, or deleting data within tables.
Useful for managing database content directly from SQLScript.
Simplifies data handling within stored procedures or functions.

[Video Link](https://www.youtube.com/watch?v=RPxuUn-f3OU&list=PL6RpkC85SLQABOpzhd7WI-hMpy99PxUo0&index=103)


## Part 7.8 SQLScript Map Merge

Combines multiple key-value pairs into one map.
Helps unify data from different sources or resolve key conflicts.
Streamlines data consolidation tasks.

[Video Link](https://www.youtube.com/watch?v=5cgzwDBHh4U&list=PL6RpkC85SLQABOpzhd7WI-hMpy99PxUo0&index=102)


## Part 7.9 SQLScript Map Reduce

Method for processing large datasets in parallel.
Divides data into smaller chunks for processing across multiple nodes.
Efficient for tasks like aggregation or filtering on big data sets.

[Video Link](https://www.youtube.com/watch?v=r7EvRcUyfAc&list=PL6RpkC85SLQABOpzhd7WI-hMpy99PxUo0&index=101)


## Part 7.10 SQLScript Debugging (Debugger)

Tool for finding and fixing errors in SQLScript code.
Allows setting breakpoints, inspecting variables, and tracing execution flow.
Aids in identifying and resolving issues to ensure code runs smoothly.

[Video Link](https://www.youtube.com/watch?v=iCZWk4lGusk&list=PL6RpkC85SLQABOpzhd7WI-hMpy99PxUo0&index=100)


## Part 7.11 SQLScript Performance Analysis

Examination of SQLScript code execution for optimizing speed.
Includes analyzing query plans, resource usage, and profiling code.
Helps enhance code efficiency and database performance.

[Video Link](https://www.youtube.com/watch?v=JLZcUEQIYD4&list=PL6RpkC85SLQABOpzhd7WI-hMpy99PxUo0&index=99)
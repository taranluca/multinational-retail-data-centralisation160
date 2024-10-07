# Multinational Retail Data Centralisation

## There are three directories for each task

### 1. Python Cleaning
This contains three Python scripts use to load, extract, clean and upload data into postgres

#### Data Utils 
Used to load in the yaml file and collect the table names present

#### Data Extraction
Used to extract the tables from the YAML files as well as other tables from AWS S3 buckets and pdf's ect

#### Data Cleaning
Where all of the tables are collected, cleaned and then uploaded to PGAdmin locally

### 2. SQL Cleaning
Once all of the tables have been loaded into postgres these SQL codes clean the tables making sure
they are all in the correct format and datatypes for querying
Run each sql file individually taking away the comments from each each block of code
The primary_keys.sql is the last script that should be run to set the primary and foreign keys for the tables

### 3. SQL Querying
This is where separate sql scripts are for querying the data producing the desired output
open each file and run the script as it is to view the output of the query


## Installation
Download repo
Carry out the operations described in each section above
1. Python Cleaning
2. SQL Cleaning
3. SQL Querying


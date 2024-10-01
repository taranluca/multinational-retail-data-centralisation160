import pandas as pd
from database_utils import DatabaseConnector
from sqlalchemy import inspect
from pandasgui import show
from sqlalchemy import create_engine
import requests
import os.path
import tabula
import boto3
import numpy as np
from io import StringIO

class DataExtractor:
            
    def init_create_table(self,chosen_table):
        create_table = pd.read_sql_table(chosen_table, engine)
        return create_table
    
    def list_number_of_stores(self,API_header,API_endpoint_number_of_stores):
        number_of_stores_response = requests.get(API_endpoint_number_of_stores, headers = API_header)
        data = number_of_stores_response.json()
        number_of_stores = data["number_stores"]
        return number_of_stores

    def retrieve_stores_data(self,API_header,API_endpoint_store_details,number_of_stores):
        store_details_csv = 'store_details_df.csv'
        check_file = os.path.isfile(store_details_csv)
        if check_file == True:
            print("CSV found in local directory")
            store_details_df = pd.read_csv(store_details_csv)
        else:
            print("Waiting for CSV to download")
            stores_as_num = list(range(0,number_of_stores,1))
            df_list = []
            for store_number in stores_as_num:
                store_number = str(store_number)
                print(store_number)
                store_data = requests.get(API_endpoint_store_details+store_number, headers = API_header)
                store_data = store_data.json()
                single_store = pd.DataFrame(store_data, index =[0])
                df_list.append(single_store)
            store_details_df = pd.concat(df_list, ignore_index=True)
            store_details_df.to_csv(store_details_csv)
            print("CSV sucessfully loaded")
        store_details_df = pd.read_csv(store_details_csv)
        return store_details_df
    
    def extract_from_s3(self,s3_address):
        s3 = boto3.resource('s3')
        s3_address = s3_address.split("/")
        s3_object = s3.Bucket(s3_address[2]).Object(s3_address[3]).get()
        products_body = s3_object["Body"].read()
        products_list = products_body.decode()

        StringData = StringIO(products_list)
        products_df = pd.read_csv(StringData, sep =",")
        return products_df

    def extract_date_details(self):
        check_file = os.path.isfile('date_details.csv')
        if check_file == True:
            print("CSV found in local directory")
            date_details_df = pd.read_csv('date_details.csv')
        else:
            print("Waiting for CSV to download")
            date_details_df = pd.read_json('https://data-handling-public.s3.eu-west-1.amazonaws.com/date_details.json')
            date_details_df.to_csv('date_details.csv')
            print("CSV sucessfully loaded")
        return date_details_df



###table names
#['legacy_store_details', 'dim_card_details', 'legacy_users', 'orders_table']

filename = "db_creds.yaml"
db_connector = DatabaseConnector(filename)
db_extractor = DataExtractor()

###Extract user data

engine = db_connector.init_db_engine()
legacy_users = db_extractor.init_create_table('legacy_users')

###Extract store data

API_header = {"x-api-key":"yFBQbwXe9J3sd6zWVAMrK6lcxxr0q1lr2PT6DDMX"}
API_endpoint_number_of_stores = "https://aqj7u5id95.execute-api.eu-west-1.amazonaws.com/prod/number_stores"
number_of_stores = db_extractor.list_number_of_stores(API_header,API_endpoint_number_of_stores)
API_endpoint_store_details = "https://aqj7u5id95.execute-api.eu-west-1.amazonaws.com/prod/store_details/"
store_data = db_extractor.retrieve_stores_data(API_header,API_endpoint_store_details,number_of_stores)

###Extract product_data
s3_address = "s3://data-handling-public/products.csv"
s3_extractor = db_extractor.extract_from_s3(s3_address)

###Extract orders data
orders_table = db_extractor.init_create_table('orders_table')

###Extract date details
date_details = db_extractor.extract_date_details()
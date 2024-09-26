from data_extraction import DataExtractor
import numpy as np
import pandas as pd
from sqlalchemy import create_engine
import os.path
import tabula


class DataCleaning:
    
    def clean_user_data(self,legacy_users):
        null_legacy_users = legacy_users.replace('NULL', np.nan)
        drop_null_legacy_users = null_legacy_users.dropna(axis=0)

        selected_countries = ['Germany', 'United Kingdom', 'United States']
        countries_mask = drop_null_legacy_users['country'].str.contains('|'.join(selected_countries), case=False)
        filtered_countries_df = drop_null_legacy_users[countries_mask]

        filtered_country_codes_df = filtered_countries_df.replace('GGB', 'GB')

        filtered_country_codes_df['date_of_birth'] = pd.to_datetime(filtered_country_codes_df['date_of_birth'], format="mixed")
        filtered_country_codes_df['join_date'] = pd.to_datetime(filtered_country_codes_df['join_date'], format="mixed")

        cleaned_legacy_users = filtered_country_codes_df

        return cleaned_legacy_users
    
    def retrive_pdf_data(self,link):
        check_file = os.path.isfile("pdf_df.csv")
        if check_file == True:
            print("CSV found in local directory")
        else:
            print("Waiting for CSV to download")
            tabula.convert_into(link, "pdf_df.csv", output_format="csv",pages='all', stream=True)
            print("CSV sucessfully loaded")
        pdf_df = pd.read_csv("pdf_df.csv")
        return pdf_df       
    
    def clean_card_data(self,pdf_df ):

        remove_nulls = pdf_df.replace('NULL', np.nan)
        pdf_df_drop_nulls = remove_nulls.dropna(axis=0)

        unique_providers = ['Diners Club / Carte Blanche', 'American Express', 'JCB 16 digit', 'JCB 15 digit', 'Maestro' 'Mastercard', 'Discover', 'VISA 19 digit', 'VISA 16 digit', 'VISA 13 digit']
        providers_mask = pdf_df_drop_nulls['card_provider'].str.contains('|'.join(unique_providers), case=False)
        filtered_providers_df = pdf_df_drop_nulls[providers_mask]

        filtered_providers_df['date_payment_confirmed'] = pd.to_datetime(filtered_providers_df['date_payment_confirmed'], format="mixed")

        cleaned_card_details = filtered_providers_df
        cleaned_card_details.head()

        return cleaned_card_details
    
    def clean_store_data(self,store_details_df):
        
        store_details_df['staff_numbers'] = store_details_df['staff_numbers'].str.replace('\D', '', regex=True)
        
        store_details_df["lat"] = np.nan
        store_details_df = store_details_df.dropna(axis=1, how='all') 


        store_details_df["address"] = store_details_df["address"].str.replace('\n', ' ')

        store_details_df = store_details_df.replace('NULL', np.nan)
        store_details_df = store_details_df.dropna(axis=0)


        selected_countries = ['DE', 'GB', 'US']
        store_details_countries_mask = store_details_df['country_code'].str.contains('|'.join(selected_countries), case=False)
        store_details_df = store_details_df[store_details_countries_mask]

        store_details_df["continent"] = store_details_df["continent"].replace('eeEurope', 'Europe')
        store_details_df["continent"] = store_details_df["continent"].replace('eeAmerica', 'America')

        store_details_df['opening_date'] = pd.to_datetime(store_details_df['opening_date'], format="mixed")

        cleaned_store_data = store_details_df
        return cleaned_store_data

    def clean_product_data(self,products_df):
        products_df = products_df.replace('NULL', np.nan)
        products_df = products_df.dropna(axis=0)

        still_available_removed = ['Still_avaliable', 'Removed']
        still_available_removed_mask = products_df['removed'].str.contains('|'.join(still_available_removed), case=False)
        products_df = products_df[still_available_removed_mask]

        products_df['date_added'] = pd.to_datetime(products_df['date_added'], format="mixed")

        cleaned_products_df = products_df
        return cleaned_products_df
    
    def convert_product_weights(self,cleaned_products_df):
        def g_to_kg(weight):
            if "x" in weight:
                weight = str(weight)
                weight = weight.split("x")
                just_weight = weight[1].split("g")
                weight_as_float =float(just_weight[0])
                if weight_as_float < 10:
                    weight_as_float = weight_as_float / 1000
                    weight_in_kg = f"{weight_as_float:.5f}"
                    weight_in_kg = str(weight_in_kg)
                else:
                    weight_in_kg = weight_as_float / 1000
                weight_with_quantity = (f"{weight_in_kg} x {weight[0]} ")    
                weight_with_quantity = str(weight_with_quantity)
                return weight_with_quantity
            elif "ml" in weight:
                weight = str(weight)
                weight = weight.split("ml")
                weight_as_float =float(weight[0])
                if weight_as_float < 10:
                    weight_as_float = weight_as_float / 1000
                    weight_in_kg = f"{weight_as_float:.5f}"
                    weight_in_kg = str(weight_in_kg)
                else:
                    weight_in_kg = weight_as_float / 1000
                weight_in_kg = str(weight_in_kg)
                return weight_in_kg
            elif "kg" in weight:
                weight = str(weight)
                weight = weight.split("kg")
                weight = weight[0]
                return weight
            elif "g" in weight:
                weight = str(weight)
                weight = weight.split("g")
                weight_as_float =float(weight[0])
                if weight_as_float < 10:
                    weight_as_float = weight_as_float / 1000
                    weight_in_kg = f"{weight_as_float:.5f}"
                    weight_in_kg = str(weight_in_kg)
                else:
                    weight_in_kg = weight_as_float / 1000
                    weight_in_kg = str(weight_in_kg)
                return weight_in_kg
            elif "oz" in weight:
                weight = str(weight)
                weight = weight.split("oz")
                weight_as_float =float(weight[0])
                weight_in_kg = weight_as_float/35.274
                weight_in_kg = f"{weight_in_kg:.5f}"
                weight_in_kg = str(weight_in_kg)
                return weight_in_kg
            else:
                return weight 

        cleaned_products_df['weight'] = cleaned_products_df['weight'].apply(lambda x: g_to_kg(x))
        
        cleaned_products_df[['new_weight','quantity']] = cleaned_products_df['weight'].str.split("x", expand=True)
        cleaned_products_df['quantity'] = cleaned_products_df['quantity'].fillna(value=1)

        cleaned_products_df = cleaned_products_df.drop('weight', axis=1)
        cleaned_products_df = cleaned_products_df.rename(columns={'new_weight': 'weight'})

        cleaned_products_df = cleaned_products_df[['Unnamed: 0','product_name','product_price','weight','quantity','category', 'EAN', 'date_added', 'uuid', 'removed', 'product_code']]  
        
        cleaned_weight_normalised_products_df = cleaned_products_df
        return cleaned_weight_normalised_products_df
    
    def clean_orders_data(self,orders_table_df):
        orders_table_df["first_name"] = np.nan
        orders_table_df["last_name"] = np.nan
        orders_table_df["1"] = np.nan
        orders_table_df["level_0"] = np.nan
        orders_table_df = orders_table_df.dropna(axis=1, how='all') 
        return orders_table_df
    
    def clean_date_details(self,date_details_df):
        date_details_df = date_details_df.replace('NULL', np.nan)
        date_details_df = date_details_df.dropna(axis=0)

        selected_time_period = ['Evening', 'Morning', 'Midday', 'Late_Hours']
        time_period_mask = date_details_df['time_period'].str.contains('|'.join(selected_time_period), case=False)
        date_details_df = date_details_df[time_period_mask]

        date_details_df['month'] = pd.to_datetime(date_details_df['month'], format="%m").dt.month
        date_details_df['year'] = pd.to_datetime(date_details_df['year'], format="%Y").dt.year
        date_details_df['day'] = pd.to_datetime(date_details_df['day'], format="%d").dt.day
        date_details_df['timestamp'] = pd.to_datetime(date_details_df['timestamp'], format="%H:%M:%S").dt.time 
        return date_details_df       
    
    def upload_to_db(self,cleaned_data,table_name):
        upload_engine = create_engine(f"{'postgresql'}+{'psycopg2'}://{'postgres'}:{'postgres'}@{'localhost'}:{5432}/{'sales_data'}")
        upload_engine.execution_options(isolation_level='AUTOCOMMIT').connect()
        cleaned_data.to_sql(table_name, upload_engine, if_exists='replace')
        

db_extractor = DataExtractor()
db_cleaner = DataCleaning()

###Clean user data
legacy_users = db_extractor.init_create_table('legacy_users')
cleaned_legacy_users = db_cleaner.clean_user_data(legacy_users)
db_cleaner.upload_to_db(cleaned_legacy_users,'dim_users')


###Clean card data
pdf_link = "https://data-handling-public.s3.eu-west-1.amazonaws.com/card_details.pdf"
retrieve_pdf = db_cleaner.retrive_pdf_data(pdf_link)
cleaned_card_details =db_cleaner.clean_card_data(retrieve_pdf)
db_cleaner.upload_to_db(cleaned_card_details,"dim_card_details")


###Clean store data
API_header = {"x-api-key":"yFBQbwXe9J3sd6zWVAMrK6lcxxr0q1lr2PT6DDMX"}
API_endpoint_number_of_stores = "https://aqj7u5id95.execute-api.eu-west-1.amazonaws.com/prod/number_stores"
number_of_stores = db_extractor.list_number_of_stores(API_header,API_endpoint_number_of_stores)
API_endpoint_store_details = "https://aqj7u5id95.execute-api.eu-west-1.amazonaws.com/prod/store_details/"
store_data = db_extractor.retrieve_stores_data(API_header,API_endpoint_store_details,number_of_stores)
cleaned_store_data = db_cleaner.clean_store_data(store_data)
db_cleaner.upload_to_db(cleaned_store_data,"dim_store_details")

###Clean product data
s3_address = "s3://data-handling-public/products.csv"
s3_extractor = db_extractor.extract_from_s3(s3_address)
product_cleaner = db_cleaner.clean_product_data(s3_extractor)
cleaned_convert_weights_product = db_cleaner.convert_product_weights(product_cleaner)
db_cleaner.upload_to_db(cleaned_convert_weights_product,"dim_products")

###Clean orders table
orders_table = db_extractor.init_create_table('orders_table')
clean_orders = db_cleaner.clean_orders_data(orders_table)
db_cleaner.upload_to_db(clean_orders,"orders_table")

###Clean date details
date_details = db_extractor.extract_date_details()
clean_dates = db_cleaner.clean_date_details(date_details)
db_cleaner.upload_to_db(clean_dates,"dim_date_times")

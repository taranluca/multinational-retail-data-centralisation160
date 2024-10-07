/*
dim_card_details = card_number
dim_date_times = date_uuid
dim_products = product_code
dim_store_details = store_code
dim_users = user_uuid
*/


/*
ALTER TABLE dim_card_details
ADD CONSTRAINT card_number_pk PRIMARY KEY (card_number)
*/

/*
ALTER TABLE dim_date_times
ADD CONSTRAINT date_uuid_pk PRIMARY KEY (date_uuid)
*/

/*
ALTER TABLE dim_products
ADD CONSTRAINT product_code_pk PRIMARY KEY (product_code)
*/

/*
ALTER TABLE dim_store_details
ADD CONSTRAINT store_code_pk PRIMARY KEY (store_code)
*/

/*
ALTER TABLE dim_users
ADD CONSTRAINT user_uuid_pk PRIMARY KEY (user_uuid)
*/

/*
ALTER TABLE orders_table
ADD CONSTRAINT index_pk PRIMARY KEY (index)
*/

/*
ALTER TABLE orders_table
ADD CONSTRAINT card_number_fk
FOREIGN KEY (card_number) REFERENCES dim_card_details (card_number)
*/

/*
ALTER TABLE orders_table
ADD CONSTRAINT date_uuid_fk
FOREIGN KEY (date_uuid) REFERENCES dim_date_times (date_uuid)
*/

/*
ALTER TABLE orders_table
ADD CONSTRAINT product_code_fk
FOREIGN KEY (product_code) REFERENCES dim_products (product_code)
*/


/*
ALTER TABLE orders_table
ADD CONSTRAINT store_code_fk
FOREIGN KEY (store_code) REFERENCES dim_store_details (store_code)
*/

/*
ALTER TABLE orders_table
ADD CONSTRAINT user_uuid_fk
FOREIGN KEY (user_uuid) REFERENCES dim_users (user_uuid)
*/
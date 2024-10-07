/*
UPDATE dim_products SET product_price = REPLACE(product_price, '£', '')
*/

/*
ALTER TABLE dim_products
ADD COLUMN weight_class VARCHAR(16)
*/

/*
UPDATE dim_products
SET weight_class = 'Light'
WHERE total_weight < 2
*/

/*
UPDATE dim_products
SET weight_class = 'Mid_Sized'
WHERE total_weight >=2 AND total_weight < 40 
*/

/*
UPDATE dim_products
SET weight_class = 'Heavy'
WHERE total_weight >=40 AND total_weight < 140 
*/

/*
UPDATE dim_products
SET weight_class = 'Truck_Required'
WHERE total_weight >=140
*/

/*
ALTER TABLE dim_products
ALTER COLUMN product_price SET DATA TYPE Float USING product_price::FLoat;
*/

/*
SELECT LENGTH("EAN") FROM dim_products
ORDER BY LENGTH("EAN") DESC
LIMIT 1
*/

/*
ALTER TABLE dim_products
ALTER COLUMN "EAN" SET DATA TYPE VARCHAR(17)
*/

/*
SELECT LENGTH(product_code) FROM dim_products
ORDER BY LENGTH(product_code) DESC
LIMIT 1
*/

/*
ALTER TABLE dim_products
ALTER COLUMN product_code SET DATA TYPE VARCHAR(11)
*/

/*
ALTER TABLE dim_products
ALTER COLUMN date_added SET DATA TYPE DATE
*/

/*
ALTER TABLE dim_products
ALTER COLUMN uuid SET DATA TYPE UUID USING uuid::UUID;
*/

/*
ALTER TABLE dim_products
ALTER COLUMN still_available SET DATA TYPE BOOL USING still_available::BOOL;
*/

/*
ALTER TABLE dim_products
SET still_available = REPLACE(still_available, 'Still_available', 'TRUE')
*/

/*
ALTER TABLE dim_products
RENAME still_available TO removed
*/

/*
ALTER TABLE dim_products
ADD COLUMN still_available boolean
*/

/*
UPDATE dim_products
SET still_available = TRUE
WHERE removed LIKE 'Still%'
*/

/*
UPDATE dim_products
SET still_available = FALSE
WHERE removed LIKE 'Removed%'
*/

/*
ALTER TABLE dim_products
DROP COLUMN removed
*/


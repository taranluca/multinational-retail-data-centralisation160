/*
SELECT LENGTH(longitude) FROM dim_store_details
ORDER BY LENGTH(longitude) DESC
LIMIT 1
*/

/*
ALTER TABLE dim_store_details
ALTER COLUMN longitude SET DATA TYPE Float USING longitude::FLoat;
*/

/*
ALTER TABLE dim_store_details
ALTER COLUMN locality SET DATA TYPE VARCHAR(255)
*/

/*
SELECT LENGTH(store_code) FROM dim_store_details
ORDER BY LENGTH(store_code) DESC
LIMIT 1
*/

/*
ALTER TABLE dim_store_details
ALTER COLUMN store_code SET DATA TYPE VARCHAR(12)
*/


/*
ALTER TABLE dim_store_details
ALTER COLUMN staff_numbers SET DATA TYPE smallint USING staff_numbers::smallint;
*/

/*
ALTER TABLE dim_store_details
ALTER COLUMN opening_date SET DATA TYPE DATE
*/

/*
ALTER TABLE dim_store_details
ALTER COLUMN store_type SET DATA TYPE VARCHAR(255)
*/

/*
ALTER TABLE dim_store_details
ALTER COLUMN latitude SET DATA TYPE Float USING latitude::FLoat;
*/

/*
SELECT LENGTH(country_code) FROM dim_store_details
ORDER BY LENGTH(country_code) DESC
LIMIT 1
*/

/*
ALTER TABLE dim_store_details
ALTER COLUMN country_code SET DATA TYPE VARCHAR(2)
*/

/*
ALTER TABLE dim_store_details
ALTER COLUMN continent SET DATA TYPE VARCHAR(255)
*/

/*
SELECT DISTINCT store_code FROM dim_store_details
*/
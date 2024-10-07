/*
ALTER TABLE orders_table
ALTER COLUMN date_uuid SET DATA TYPE UUID USING date_uuid::UUID;
*/


/*
ALTER TABLE orders_table
ALTER COLUMN user_uuid SET DATA TYPE UUID USING user_uuid::UUID;
*/


/*
SELECT LENGTH(card_number) FROM orders_table
ORDER BY LENGTH(card_number) DESC
LIMIT 1
*/

/*ALTER TABLE orders_table
ALTER COLUMN card_number SET DATA TYPE VARCHAR(19)
*/

/*
SELECT LENGTH(store_code) FROM orders_table
ORDER BY LENGTH(store_code) DESC
LIMIT 1
*/

/*
ALTER TABLE orders_table
ALTER COLUMN store_code SET DATA TYPE VARCHAR(12)
*/

/*
SELECT LENGTH(product_code) FROM orders_table
ORDER BY LENGTH(product_code) DESC
LIMIT 1
*/

/*
ALTER TABLE orders_table
ALTER COLUMN product_code SET DATA TYPE VARCHAR(11)
*/

/*
ALTER TABLE orders_table
ALTER COLUMN product_quantity SET DATA TYPE smallint
*/
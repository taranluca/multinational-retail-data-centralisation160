/*
SELECT LENGTH(card_number) FROM dim_card_details
ORDER BY LENGTH(card_number) DESC
LIMIT 1
*/

/*
ALTER TABLE dim_card_details
ALTER COLUMN card_number SET DATA TYPE VARCHAR(19)
*/

/*
SELECT LENGTH(expiry_date) FROM dim_card_details
ORDER BY LENGTH(expiry_date) DESC
LIMIT 1
*/

/*
ALTER TABLE dim_card_details
ALTER COLUMN expiry_date SET DATA TYPE VARCHAR(5)
*/

/*
ALTER TABLE dim_card_details
ALTER COLUMN date_payment_confirmed SET DATA TYPE DATE
*/

/*
SELECT DISTINCT card_number FROM dim_card_details
*/
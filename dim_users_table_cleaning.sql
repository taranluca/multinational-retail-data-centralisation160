/*
ALTER TABLE dim_users
ALTER COLUMN first_name SET DATA TYPE VARCHAR(255)
*/

/*
ALTER TABLE dim_users
ALTER COLUMN last_name SET DATA TYPE VARCHAR(255)
*/

/*
ALTER TABLE dim_users
ALTER COLUMN date_of_birth SET DATA TYPE DATE
*/

/*
SELECT LENGTH(country_code) FROM dim_users
ORDER BY LENGTH(country_code) DESC
LIMIT 1
*/

/*
ALTER TABLE dim_users
ALTER COLUMN country_code SET DATA TYPE VARCHAR(2)
*/

/*
ALTER TABLE dim_users
ALTER COLUMN user_uuid SET DATA TYPE UUID USING user_uuid::UUID;
*/

/*
ALTER TABLE dim_users
ALTER COLUMN join_date SET DATA TYPE DATE
*/
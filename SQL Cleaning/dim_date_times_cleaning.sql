/*
ALTER TABLE dim_date_times
ALTER COLUMN month SET DATA TYPE VARCHAR(2)
*/

/*
ALTER TABLE dim_date_times
ALTER COLUMN year SET DATA TYPE VARCHAR(4)
*/

/*
ALTER TABLE dim_date_times
ALTER COLUMN day SET DATA TYPE VARCHAR(2)
*/

/*
SELECT LENGTH(time_period) FROM dim_date_times
ORDER BY LENGTH(time_period) DESC
LIMIT 1
*/

/*
ALTER TABLE dim_date_times
ALTER COLUMN time_period SET DATA TYPE VARCHAR(10)
*/

/*
ALTER TABLE dim_date_times
ALTER COLUMN date_uuid SET DATA TYPE UUID USING date_uuid::UUID;
*/

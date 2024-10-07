WITH average_time AS(
    SELECT
    year,
    LEAD(CAST(CONCAT(year,'-',month,'-',day,' ',timestamp) AS TIMESTAMP)) OVER (ORDER BY CAST(CONCAT(year,'-',month,'-',day,' ',timestamp) AS TIMESTAMP)) - CAST(CONCAT(year,'-',month,'-',day,' ',timestamp) AS TIMESTAMP) AS time_difference
    FROM dim_date_times
    ORDER BY year
)

SELECT
    year,
    AVG(time_difference) AS actual_time_taken
FROM average_time
GROUP BY year
ORDER BY actual_time_taken DESC
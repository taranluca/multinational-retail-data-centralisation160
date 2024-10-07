SELECT
        store_type,
        CAST(SUM(dim_products.product_price * product_quantity) as DECIMAL(9,2)) AS total_sales,
        CAST(COUNT( * ) / CAST((SELECT COUNT( * ) FROM orders_table) AS NUMERIC) * 100 as DECIMAL(4,2)) as "percentage_total(%)"
FROM orders_table
INNER JOIN dim_store_details ON orders_table.store_code = dim_store_details.store_code
INNER JOIN dim_products ON orders_table.product_code = dim_products.product_code
GROUP BY store_type
ORDER BY "percentage_total(%)" DESC


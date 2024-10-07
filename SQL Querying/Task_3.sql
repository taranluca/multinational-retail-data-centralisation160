SELECT
        cast(SUM(dim_products.product_price * product_quantity) as DECIMAL(8,2)) AS total_sales,
        month
FROM orders_table
INNER JOIN dim_date_times ON orders_table.date_uuid = dim_date_times.date_uuid
INNER JOIN dim_products ON orders_table.product_code = dim_products.product_code
GROUP BY month
ORDER BY total_sales DESC
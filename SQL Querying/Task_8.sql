SELECT
        cast(SUM(dim_products.product_price * product_quantity) as DECIMAL(9,2)) AS total_sales,
        store_type,
        country_code
FROM orders_table
INNER JOIN dim_products ON orders_table.product_code = dim_products.product_code
INNER JOIN dim_store_details ON orders_table.store_code = dim_store_details.store_code
WHERE country_code = 'DE'
GROUP BY store_type, country_code
ORDER BY total_sales ASC
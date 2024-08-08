-- Write your PostgreSQL query statement below
SELECT   
    products.product_name,  
    SUM(orders.unit) AS unit  
FROM   
    orders  
JOIN   
    products ON products.product_id = orders.product_id   
WHERE   
    TO_CHAR(orders.order_date, 'YYYY-MM') = '2020-02'  
GROUP BY   
    products.product_id, products.product_name
HAVING SUM(orders.unit) >= 100;
WITH latest_prices AS (  
    SELECT   
        p.product_id,  
        p.new_price,  
        p.change_date,  
        ROW_NUMBER() OVER (PARTITION BY p.product_id ORDER BY p.change_date DESC) AS rn  
    FROM   
        Products p  
    WHERE   
        p.change_date <= DATE '2019-08-16'  
)  
SELECT   
    distinct prod.product_id,  
    COALESCE(lp.new_price, 10) AS price  
FROM   
    Products prod  
LEFT JOIN   
    latest_prices lp ON prod.product_id = lp.product_id AND lp.rn = 1;
-- Write your PostgreSQL query statement below
select product.product_name, 
    sales.year,
    sales.price
    from Sales
    Join Product on Sales.product_id = product.product_id;

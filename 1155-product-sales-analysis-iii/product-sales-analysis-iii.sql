-- Write your PostgreSQL query statement below
select 
    a.product_id,
    a.first_year,
    b.quantity,
    b.price
from (Select 
        product_id,
        min(year) first_year
    from 
        Sales
    group by 
        product_id
    ) a join Sales b
on 
    a.product_id = b.product_id 
    and 
    b.year = a.first_year;

-- Write your PostgreSQL query statement below
Select 
    Sell_date,
    count(distinct product) as num_sold,
    STRING_AGG(distinct product, ',' order by product) as products
from Activities 
group by sell_date
order by sell_date
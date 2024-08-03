-- Write your PostgreSQL query statement below
Select 
    customer_id
from 
    Customer
group by customer_id
having count(distinct product_key) = (Select count(*) from Product)
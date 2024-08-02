-- Write your PostgreSQL query statement below
Select *
from Cinema c
where c.id % 2 = 1 and c.description != 'boring'
order by c.rating desc;
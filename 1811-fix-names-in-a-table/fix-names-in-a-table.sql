-- Write your PostgreSQL query statement below
select 
    User_id,
    Upper(left(name, 1)) || Lower(right(name, length(name) - 1)) as name
from
    Users
order by user_id
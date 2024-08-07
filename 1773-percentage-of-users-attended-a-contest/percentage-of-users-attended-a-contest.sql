-- Write your PostgreSQL query statement below
Select 
    contest_id, 
    round(count(distinct user_id) * 100 / (select count(*) from users)::decimal, 2) as "percentage"
from Register
    group by contest_id
order by "percentage" desc, contest_id;

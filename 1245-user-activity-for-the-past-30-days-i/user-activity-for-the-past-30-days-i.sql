-- Write your PostgreSQL query statement below
Select 
    activity_date as day,
    count(distinct user_id) active_users
from Activity
    where 
        activity_date <= date('2019-07-27') and activity_date > date('2019-07-27') - 30
group by 
    activity_date
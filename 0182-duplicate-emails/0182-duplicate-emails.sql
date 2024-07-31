# Write your MySQL query statement below
with counter as (
    select  email, 
    count(email) as c_e
    from person
    group by email
)
select Email 
from counter
where c_e >= 2;



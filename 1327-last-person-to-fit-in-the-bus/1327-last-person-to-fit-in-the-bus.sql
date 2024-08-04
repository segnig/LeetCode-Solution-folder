# Write your MySQL query statement below
Select 
    person_name 
from(
    Select 
        person_name, 
        sum(weight) over(order by turn) as coun_turn
    from
        Queue
    order by turn desc
)  a
where coun_turn <= 1000
limit 1
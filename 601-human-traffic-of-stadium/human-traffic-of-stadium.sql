-- Write your PostgreSQL query statement below
with test as(
    select 
        *,
        row_number() over(order by visit_date) as rt,
        id - row_number() over(order by visit_date) grp
    from stadium 
    where people >= 100
)

Select 
    id,
    visit_date,
    people
from test 
where grp in (
    Select 
        grp
    from test
    group by grp 
    having count(*) >= 3
)

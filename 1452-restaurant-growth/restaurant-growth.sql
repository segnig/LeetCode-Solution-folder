-- Write your PostgreSQL query statement below
With cte as(
    Select 
        visited_on, 
        sum(amount) as amount
    from Customer
    group by visited_on
)
select 
    a.visited_on, 
    round(sum(b.amount), 2) as amount,
    round(avg(b.amount), 2) as average_amount
from cte a, cte b
where a.visited_on - b.visited_on BETWEEN 0 and 6
group by a.visited_on
having count(*) > 6
order by a.visited_on

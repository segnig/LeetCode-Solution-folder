-- Write your PostgreSQL query statement below
Select
    a.Employee_id,
    a.name, 
    count(b.Employee_id) reports_count,
    Round(avg(b.age), 0) average_age
from Employees a
Join Employees b 
    on a.employee_id = b.reports_to 
group by a.Employee_id,a.name 
order by a.Employee_id
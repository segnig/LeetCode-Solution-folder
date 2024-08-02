-- Write your PostgreSQL query statement below
Select 
em.unique_id, 
e.name 
from public.Employees e
left join public.EmployeeUNI em
on e.id = em.id;
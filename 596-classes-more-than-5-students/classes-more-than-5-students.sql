-- Write your PostgreSQL query statement below
Select 
    class
from 
    Courses
Group by 
    class
having count(student) >= 5;
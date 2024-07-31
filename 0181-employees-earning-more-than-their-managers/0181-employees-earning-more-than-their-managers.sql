# Write your MySQL query statement below
Select emp2.name Employee
from Employee emp1
JOIN  Employee emp2
on emp1.id = emp2.managerId
where  emp1.salary < emp2.salary;

 /*
SELECT e2.name as Employee
FROM employee e1
INNER JOIN employee e2 ON e1.id = e2.managerID
WHERE
e1.salary < e2.salary

 */
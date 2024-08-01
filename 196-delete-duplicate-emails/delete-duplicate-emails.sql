# Write your MySQL query statement below
Delete per1 from Person per1, Person per2
Where per1.email = per2.email and per1.id > per2.id;
# Write your MySQL query statement below
/*
Select 
Email from 
Person 
group by Email 
having count(*) > 1;

*/

Select distinct Email 
from Person
where Email In (
    Select Email
    from Person 
    Group by Email
    having Count(*) > 1
) ;


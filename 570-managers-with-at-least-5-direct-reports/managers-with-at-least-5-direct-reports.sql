-- Write your PostgreSQL query statement below
SELECT em2.name   
FROM Employee em   
JOIN Employee em2   
    ON em.managerId = em2.id  
GROUP BY em2.id, em2.name  
HAVING COUNT(em.id) > 4;
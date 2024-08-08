-- Write your PostgreSQL query state
WITH temp AS (  
    SELECT  
        Id,  
        name,        
        salary,  
        departmentId,  
        DENSE_RANK() OVER (PARTITION BY departmentId ORDER BY salary DESC) AS rnk  
    FROM Employee  
)

SELECT 
    depart.name Department,
    temp.name Employee,
    temp.salary Salary
FROM temp
join Department depart 
on temp.departmentID = depart.id
WHERE temp.rnk <= 3  
ORDER BY temp.departmentId, temp.rnk;  
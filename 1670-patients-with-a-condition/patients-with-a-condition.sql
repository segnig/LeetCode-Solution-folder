-- Write your PostgreSQL query statement below
SELECT *  
FROM patients  
WHERE conditions LIKE '% DIAB1%' or conditions LIKE 'DIAB1%';
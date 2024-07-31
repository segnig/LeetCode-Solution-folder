# Write your MySQL query statement below
SELECT  
    score,  
    Dense_RANK() OVER (ORDER BY score DESC) AS "rank"
FROM  
    scores ;
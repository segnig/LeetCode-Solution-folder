WITH all_parents AS (  
    SELECT DISTINCT p_id FROM tree WHERE p_id IS NOT NULL  
)  
SELECT  
    id,  
    CASE  
        WHEN p_id IS NULL THEN 'Root'  
        WHEN id IN (SELECT * FROM all_parents) THEN 'Inner'  
        ELSE 'Leaf'  
    END AS "type"  
FROM tree;
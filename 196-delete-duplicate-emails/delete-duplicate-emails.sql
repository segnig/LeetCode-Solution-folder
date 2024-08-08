DELETE FROM Person  
WHERE id IN (  
    SELECT per1.id  
    FROM Person per1  
    JOIN Person per2 ON per1.email = per2.email  
    WHERE per1.id > per2.id  
);
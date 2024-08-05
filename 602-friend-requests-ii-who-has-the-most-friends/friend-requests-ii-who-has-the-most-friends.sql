WITH ct1 AS (  
    SELECT   
        accepter_id,  
        requester_id  
    FROM   
        RequestAccepted  
    UNION ALL  
    SELECT   
        requester_id AS accepter_id,  
        accepter_id AS requester_id  
    FROM   
        RequestAccepted  
)  
SELECT   
    accepter_id AS id,  
    COUNT(requester_id) AS num  
FROM   
    ct1  
GROUP BY   
    accepter_id  
ORDER BY   
    num DESC  
LIMIT 1;
SELECT   
    machine_id,   
    ROUND(AVG(ranges)::numeric, 3) AS processing_time  
FROM (  
    SELECT   
        machine_id,  
        MAX(timestamp) - MIN(timestamp) AS ranges  
    FROM   
        Activity  
    GROUP BY   
        machine_id, process_id  
) AS subquery  
GROUP BY   
    machine_id;
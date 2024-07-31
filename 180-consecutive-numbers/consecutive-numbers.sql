SELECT distinct t1.num as ConsecutiveNums
FROM logs t1
JOIN logs t2 ON t1.id + 1 = t2.id
JOIN logs t3 ON t1.id + 2 = t3.id
WHERE t1.num = t2.num and t2.num = t3.num
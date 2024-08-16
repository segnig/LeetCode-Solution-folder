# Write your MySQL query statement below

SELECT 
    transaction_date,
    sum(case when amount % 2 = 1 then amount else 0 end) odd_sum,
    sum(case when amount % 2 = 0 then amount else 0 end) even_sum
FROM transactions
    GROUP BY transaction_date
order by transaction_date
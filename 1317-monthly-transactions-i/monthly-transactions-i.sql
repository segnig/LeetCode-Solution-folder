-- Write your PostgreSQL query statement below
with Trans as(
    SELECT   
        substring(trans_date::text, 1, 7) AS month,
        country,
        state,
        amount    
    FROM   
        Transactions
    )
select 
    month, 
    country,
    count(*) as trans_count,
    Sum(case when "state" = 'approved' then 1 else 0 end) as approved_count,
    sum(amount) as trans_total_amount,
    Sum(case when "state" = 'approved' then amount else 0 end) as approved_total_amount
from 
    trans
group by
    month, country;

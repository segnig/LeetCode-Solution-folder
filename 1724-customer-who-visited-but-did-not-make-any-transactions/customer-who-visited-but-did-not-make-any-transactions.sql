-- Write your PostgreSQL query statement below
Select 
    v.customer_id, 
    Count(v.customer_id) as count_no_trans
    from Visits v
    Left Join Transactions t
    On v.visit_id = t.visit_id
    where transaction_id is null
    group by v.customer_id
     order by count_no_trans;
-- Write your PostgreSQL query statement below
select name
    from SalesPerson
    where sales_id not in
(Select 
    sales_id
From orders o
join Company c
    on c.com_id = o.com_id
where c.name = 'RED')
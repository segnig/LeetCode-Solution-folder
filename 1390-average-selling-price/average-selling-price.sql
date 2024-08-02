-- Write your PostgreSQL query statement below
select 
    prices.product_id, 
    coalesce(
        round(sum(prices.price * u.units)/sum(u.units)::decimal,2), 0
    ) as average_price

    from  Prices 
    left join UnitsSold u
    on prices.product_id = u.product_id and 
        u.purchase_date >= prices.start_date and 
        u.purchase_date <= prices.end_date 
    group by prices.product_id;


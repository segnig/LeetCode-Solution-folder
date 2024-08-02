select
query_name,
round(avg(cast(rating as decimal) / position), 2) as quality,
round(sum(case when rating < 3 then 1 else 0 end) * 100::decimal / count(*), 2) as poor_query_percentage
from
queries
where query_name is not null
group by
query_name;
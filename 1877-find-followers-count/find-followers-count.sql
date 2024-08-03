-- Write your PostgreSQL query statement below
Select 
    User_id,
    count(follower_id) as followers_count
From 
    Followers
group by user_id
order by user_id

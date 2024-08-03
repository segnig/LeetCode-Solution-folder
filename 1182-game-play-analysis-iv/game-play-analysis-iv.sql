-- Write your PostgreSQL query statement below
Select 
    Round(count(Distinct Player_id) :: decimal / (Select Count(Distinct Player_id) from Activity ), 2) as fraction
from 
    Activity 
    where (player_id, event_date - 1) IN
    (
        Select player_id, min(event_date)
        from Activity 
        Group by 
            player_id
    )
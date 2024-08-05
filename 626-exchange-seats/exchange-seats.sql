Select 
    (case 
        when id < (Select max(id) from Seat) then
            case when id % 2 = 0 then id -1 else id + 1 end
            else
            case when id % 2 = 0 then id -1 else id end  
            end      
            ) as id, 
        student
        from Seat 
        order by id;
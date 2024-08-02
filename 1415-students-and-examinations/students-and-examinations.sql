-- Write your PostgreSQL query statement below  
with ss as(
    select
    s.student_id,
    s.student_name,
    su.subject_name
    from Students s
    Cross Join 
        subjects su
)
select 
    ss.student_id,
    ss.student_name,
    ss.subject_name,
    Coalesce(count(e.subject_name), 0) as attended_exams
    from ss
    Left join Examinations e
    on e.student_id = ss.student_id and 
        e.subject_name = ss.subject_name
    group by 
        ss.student_id,
        ss.student_name,
        ss.subject_name
    order by
        ss.student_id,
        ss.subject_name

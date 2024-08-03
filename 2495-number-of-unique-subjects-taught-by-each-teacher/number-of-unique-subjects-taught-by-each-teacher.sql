-- Write your PostgreSQL query statement below
select teacher_id, count(Distinct subject_id) cnt
from Teacher
    where (Subject_id, dept_id) IN (
        Select subject_id, dept_id from Teacher group by Subject_id, dept_id having count(teacher_id) = 1
    )
group by teacher_id
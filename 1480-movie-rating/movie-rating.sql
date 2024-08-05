-- Write your PostgreSQL query statement below
(SELECT name as results
FROM
    (SELECT user_id, name, COUNT(*) rating_cnt
    FROM MovieRating LEFT JOIN Users USING (user_id)
    GROUP BY user_id, name) users_
ORDER BY rating_cnt DESC, name
LIMIT 1)

UNION ALL

(SELECT title as results
FROM
    (SELECT movie_id, title, AVG(rating) avg_rating
    FROM MovieRating LEFT JOIN Movies USING (movie_id)
    WHERE to_char(created_at, 'YYYY-MM') = '2020-02'
    GROUP BY movie_id, title) movies_
ORDER BY avg_rating DESC, title
LIMIT 1)
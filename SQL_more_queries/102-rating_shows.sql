-- Lists all shows from hbtn_0d_tvshows_rate by their rating sum.
-- Displays title and rating sum, sorted descending by rating.
SELECT tv_shows.title, COALESCE(SUM(tv_show_ratings.rating), 0) AS rating
FROM tv_shows
LEFT JOIN tv_show_ratings ON tv_shows.id = tv_show_ratings.show_id
GROUP BY tv_shows.id
ORDER BY rating DESC;

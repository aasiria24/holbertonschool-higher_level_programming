-- Lists all genres in the database hbtn_0d_tvshows_rate by their rating sum.
-- Displays genre name and rating sum, sorted descending by rating.
SELECT tv_genres.name, COALESCE(SUM(tv_show_ratings.rating), 0) AS rating
FROM tv_genres
LEFT JOIN tv_show_genres ON tv_genres.id = tv_show_genres.genre_id
LEFT JOIN tv_show_ratings ON tv_show_genres.show_id = tv_show_ratings.show_id
GROUP BY tv_genres.id
ORDER BY rating DESC;

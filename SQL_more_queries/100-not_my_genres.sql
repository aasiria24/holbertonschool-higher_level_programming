-- Lists all genres not linked to the show Dexter from the database hbtn_0d_tvshows.
-- Results sorted in ascending order by genre name.
SELECT tv_genres.name
FROM tv_genres
LEFT JOIN tv_show_genres ON tv_genres.id = tv_show_genres.genre_id
    AND tv_show_genres.show_id = (SELECT id FROM tv_shows WHERE title = 'Dexter')
WHERE tv_show_genres.show_id IS NULL
ORDER BY tv_genres.name ASC;

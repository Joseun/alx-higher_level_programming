-- Lists all shows in hbtn_0d_tvshows that have at least one genre linked.
-- Records are sorted by ascending tv_shows.title and tv_show_genres.genre_id.
SELECT `tv_genres`.`name` AS genre, COUNT(`tv_shows_genres`.`genre_id`) AS number_of_shows
FROM `tv_genres`
RIGHT JOIN `tv_show_genres`
ON `tv_genres`.`id` = `tv_show_genres`.`genre_id`
GROUP BY genre
ORDER BY number_of_shows DESC;

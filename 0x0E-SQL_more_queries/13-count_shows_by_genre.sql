-- Lists all shows in hbtn_0d_tvshows that have at least one genre linked.
-- Records are sorted by ascending tv_shows.title and tv_show_genres.genre_id.
SELECT `tv_genres`.`name` AS genre, COUNT(`tv_shows_genres`.`genre_id`) AS number_of_shows
FROM `tv_genres` AS g
INNER JOIN `tv_show_genres` AS s
ON g.`id` = s.`show_id`
GROUP BY genre
ORDER BY number_of_shows DESC;

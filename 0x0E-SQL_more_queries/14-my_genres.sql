-- Lists all shows in hbtn_0d_tvshows that have at least one genre linked.
-- Records are sorted by ascending tv_shows.title and tv_show_genres.genre_id.
SELECT `tv_genres`.`name`
FROM `tv_genres`
INNER JOIN `tv_show_genres`
      ON `tv_show_genres`.`genre_id` = `tv_genres`.`id`
INNER JOIN `tv_shows`
      ON `tv_shows`.`id` = `tv_show_genres`.`show_id`
WHERE `tv_shows`.`title` = 'Dexter'
ORDER BY `tv_genres`.`name`;

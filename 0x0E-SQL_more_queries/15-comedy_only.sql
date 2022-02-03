-- Lists all shows in hbtn_0d_tvshows that have at least one genre linked.
-- Records are sorted by ascending tv_shows.title and tv_show_genres.genre_id.
SELECT `tv_shows`.`title`
FROM `tv_shows`
INNER JOIN `tv_show_genres`
      ON  `tv_show_genres`.`show_id` = `tv_shows`.`id`
INNER JOIN `tv_genres`
      ON `tv_show_genres`.`genre_id` = `tv_genres`.`id`
WHERE `tv_genres`.`name` = 'Comedy'
ORDER BY `tv_shows`.`title`;

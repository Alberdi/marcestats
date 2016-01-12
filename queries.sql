-- STRICTLY COMPETITIVE PERCENTAGES
SELECT p.name, (100.0*SUM(t.winner) / COUNT(*)) AS 'Wins %', COUNT(*) AS 'Plays'
FROM bgplays_player p
INNER JOIN bgplays_team_players tp on p.id = tp.player_id
INNER JOIN bgplays_team t ON tp.team_id = t.id
WHERE t.play_id IN (
        -- NOT ALL WINNERS/LOSERS
	SELECT play_id FROM bgplays_team
	WHERE winner IS NOT NULL
	GROUP BY play_id
	HAVING MAX(winner) != MIN(winner)
)
AND t.play_id IN (
        -- NOT SAME PLAYER ON DIFFERENT TEAMS
	SELECT DISTINCT t.play_id FROM bgplays_team t
	INNER JOIN bgplays_team_players tp ON tp.team_id = t.id
	GROUP BY t.play_id, tp.player_id
	HAVING COUNT(*) == 1
)
GROUP BY p.name;

-- STRICTLY SOLO/COOPERATIVE PERCENTAGES
SELECT sub.name, (100.0*SUM(sub.winner) / COUNT(*)) AS 'Wins %', COUNT(*) AS 'Plays'
FROM (
	SELECT p.name, t.play_id, MAX(t.winner) AS 'winner'
	FROM bgplays_player p
	INNER JOIN bgplays_team_players tp on p.id = tp.player_id
	INNER JOIN bgplays_team t ON tp.team_id = t.id
	INNER JOIN bgplays_play play ON play.id = t.play_id
	INNER JOIN bgplays_game g ON play.game_id = g.id
	WHERE t.play_id IN (
	        -- COOPERATIVE = ALL WON OR ALL LOST
		SELECT play_id FROM bgplays_team
		WHERE winner IS NOT NULL
		GROUP BY play_id
		HAVING MAX(winner) == MIN(winner)
	)
	AND g.name != 'Hanabi'
	GROUP BY p.name, t.play_id
) AS sub
GROUP BY sub.name;

-- GAMES PLAYED BY G+S+M IN 2015
SELECT g.name, play.date, COUNT(*)
FROM bgplays_play play
INNER JOIN bgplays_game g ON play.game_id = g.id
WHERE play.date LIKE '2015%'
AND play.id IN (
	SELECT play.id
	FROM bgplays_play play
	INNER JOIN bgplays_team t ON play.id = t.play_id
	INNER JOIN bgplays_team_players tp ON t.id = tp.team_id
	INNER JOIN bgplays_player p ON p.id = tp.player_id
	WHERE p.name = 'Marcelino'
)
AND play.id IN (
	SELECT play.id
	FROM bgplays_play play
	INNER JOIN bgplays_team t ON play.id = t.play_id
	INNER JOIN bgplays_team_players tp ON t.id = tp.team_id
	INNER JOIN bgplays_player p ON p.id = tp.player_id
	WHERE p.name = 'Guillermo'
)
AND play.id IN (
	SELECT play.id
	FROM bgplays_play play
	INNER JOIN bgplays_team t ON play.id = t.play_id
	INNER JOIN bgplays_team_players tp ON t.id = tp.team_id
	INNER JOIN bgplays_player p ON p.id = tp.player_id
	WHERE p.name = 'Sito'
)
GROUP BY g.name, play.date;

-- PLAYS BY G+S+M BY DATE
SELECT play.date, COUNT(*)
FROM bgplays_play play
WHERE play.id IN (
	SELECT play.id
	FROM bgplays_play play
	INNER JOIN bgplays_team t ON play.id = t.play_id
	INNER JOIN bgplays_team_players tp ON t.id = tp.team_id
	INNER JOIN bgplays_player p ON p.id = tp.player_id
	WHERE p.name = 'Marcelino' OR p.name = 'Guillermo' OR p.name = 'Sito'
	GROUP BY play.id
	HAVING COUNT(*) = 3 OR COUNT(*) = 6 --HACK FOR SPACE HULK: DEATH ANGEL
	-- FIXME: SH:DA is being counted also for solo games
)
GROUP BY play.date;

-- WIN% 1vs1
SELECT p.name, (100.0*SUM(t.winner) / COUNT(*)) AS 'Wins %', COUNT(*) AS 'Plays'
FROM bgplays_player p
INNER JOIN bgplays_team_players tp on p.id = tp.player_id
INNER JOIN bgplays_team t ON tp.team_id = t.id
WHERE t.play_id IN (
	SELECT play.id
	FROM bgplays_play play
	INNER JOIN bgplays_team t ON play.id = t.play_id
	INNER JOIN bgplays_team_players tp ON t.id = tp.team_id
	INNER JOIN bgplays_player p ON p.id = tp.player_id
	WHERE p.name = 'Marcelino'
	INTERSECT
	SELECT play.id
	FROM bgplays_play play
	INNER JOIN bgplays_team t ON play.id = t.play_id
	INNER JOIN bgplays_team_players tp ON t.id = tp.team_id
	INNER JOIN bgplays_player p ON p.id = tp.player_id
	WHERE p.name = 'Sito'
	INTERSECT
	-- TWO PLAYER COMPETITIVE GAMES
	SELECT t.play_id
	FROM bgplays_team t
	INNER JOIN bgplays_team_players tp ON t.id = tp.team_id
	WHERE t.winner IS NOT NULL
	GROUP BY t.play_id
	HAVING MAX(t.winner) != MIN(t.winner) AND COUNT(tp.player_id) = 2
)
GROUP BY p.name;

-- SCORE DIFFERENCE IN EACH PLAY
SELECT t.play_id, MAX(t.points)-MIN(t.points) 'diff'
FROM bgplays_play play
INNER JOIN bgplays_team t ON play.id = t.play_id
WHERE t.points IS NOT NULL
GROUP BY t.play_id
ORDER BY diff;

-- AMOUNT OF COMPETITIVE SECOND PLACES
SELECT p.name, COUNT(*)
FROM bgplays_play play
INNER JOIN bgplays_team t ON play.id = t.play_id
INNER JOIN bgplays_team_players tp ON t.id = tp.team_id
INNER JOIN bgplays_player p ON p.id = tp.player_id
WHERE t.play_id IN (
        -- NOT ALL WINNERS/LOSERS
	SELECT play_id FROM bgplays_team
	WHERE winner IS NOT NULL
	GROUP BY play_id
	HAVING MAX(winner) != MIN(winner)
)
AND t.play_id IN (
        -- NOT SAME PLAYER ON DIFFERENT TEAMS
	SELECT DISTINCT t2.play_id FROM bgplays_team t2
	INNER JOIN bgplays_team_players tp2 ON tp2.team_id = t2.id
	GROUP BY t2.play_id, tp2.player_id
	HAVING COUNT(*) == 1
)
AND t.play_id IN (
        -- AT LEAST THREE TEAMS
	SELECT play3.id
	FROM bgplays_play play3
	INNER JOIN bgplays_team t3 ON play3.id = t3.play_id
	GROUP BY play3.id
	HAVING COUNT(t3.id) > 2
)
AND t.points IN (
	-- HIGHEST LOSER SCORE
	SELECT MAX(t4.points) FROM bgplays_team t4
	WHERE t4.play_id = t.play_id AND t4.winner = 0
)
AND t.winner = 0
GROUP BY p.name;

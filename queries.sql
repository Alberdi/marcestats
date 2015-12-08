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
)
GROUP BY play.date;


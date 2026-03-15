"""Reusable SQL templates for Analytics Lab and fan question pages."""

analytics_query_templates: dict[str, str] = {
    "best_powerplay_batters": """
        SELECT p.full_name,
               COUNT(*) AS balls,
               SUM(b.runs_batter) AS runs,
               ROUND(100.0 * SUM(b.runs_batter)::numeric / NULLIF(COUNT(*), 0), 2) AS strike_rate
        FROM ball_by_ball b
        JOIN players p ON p.id = b.striker_player_id
        JOIN matches m ON m.id = b.match_id
        WHERE b.phase = 'POWERPLAY'
          AND m.format = :format
          AND EXTRACT(YEAR FROM m.start_time) BETWEEN :start_year AND :end_year
        GROUP BY p.full_name
        HAVING COUNT(DISTINCT m.id) >= :min_matches
        ORDER BY strike_rate DESC
        LIMIT 50
    """,
    "best_death_bowlers": """
        SELECT p.full_name,
               COUNT(*) AS balls,
               SUM(b.runs_total) AS runs_conceded,
               ROUND(6.0 * SUM(b.runs_total)::numeric / NULLIF(COUNT(*), 0), 2) AS economy
        FROM ball_by_ball b
        JOIN players p ON p.id = b.bowler_player_id
        JOIN matches m ON m.id = b.match_id
        WHERE b.phase = 'DEATH'
          AND m.format = :format
        GROUP BY p.full_name
        HAVING COUNT(DISTINCT m.id) >= :min_matches
        ORDER BY economy ASC
        LIMIT 50
    """,
    "best_odi_chasers": """
        SELECT p.full_name,
               COUNT(*) AS chases,
               SUM(pms.runs) AS chase_runs,
               ROUND(AVG(pms.runs)::numeric, 2) AS chase_avg
        FROM player_match_stats pms
        JOIN players p ON p.id = pms.player_id
        JOIN matches m ON m.id = pms.match_id
        WHERE m.format = 'ODI'
          AND m.status = 'COMPLETED'
        GROUP BY p.full_name
        HAVING COUNT(*) >= :min_matches
        ORDER BY chase_avg DESC, chase_runs DESC
        LIMIT 50
    """,
}

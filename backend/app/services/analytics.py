"""Reusable SQL templates and in-memory analytics helpers for Analytics Lab."""

from __future__ import annotations

from collections import defaultdict
from typing import Any

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
        GROUP BY p.full_name
        ORDER BY strike_rate DESC
        LIMIT 20
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
        ORDER BY economy ASC
        LIMIT 20
    """,
    "highest_strike_rates": """
        SELECT p.full_name,
               SUM(pms.runs) AS runs,
               SUM(pms.balls_faced) AS balls,
               ROUND(100.0 * SUM(pms.runs)::numeric / NULLIF(SUM(pms.balls_faced), 0), 2) AS strike_rate
        FROM player_match_stats pms
        JOIN players p ON p.id = pms.player_id
        GROUP BY p.full_name
        HAVING SUM(pms.balls_faced) > 0
        ORDER BY strike_rate DESC
        LIMIT 20
    """,
}


def compute_analytics_from_balls(
    ball_by_ball: list[dict[str, Any]], player_match_stats: list[dict[str, Any]], players: list[dict[str, Any]]
) -> dict[str, list[dict[str, Any]]]:
    """Generate analytics JSON payloads for the frontend when DB is not attached."""

    player_name = {player["id"]: player["full_name"] for player in players}

    powerplay = defaultdict(lambda: {"balls": 0, "runs": 0})
    death = defaultdict(lambda: {"balls": 0, "runs_conceded": 0})

    for ball in ball_by_ball:
        if ball["phase"] == "POWERPLAY" and ball.get("striker_player_id"):
            stats = powerplay[ball["striker_player_id"]]
            stats["balls"] += 1
            stats["runs"] += ball["runs_batter"]

        if ball["phase"] == "DEATH" and ball.get("bowler_player_id"):
            stats = death[ball["bowler_player_id"]]
            stats["balls"] += 1
            stats["runs_conceded"] += ball["runs_total"]

    best_powerplay_batters = [
        {
            "player": player_name[player_id],
            "balls": row["balls"],
            "runs": row["runs"],
            "strike_rate": round((row["runs"] * 100) / row["balls"], 2),
        }
        for player_id, row in powerplay.items()
        if row["balls"]
    ]
    best_powerplay_batters.sort(key=lambda row: row["strike_rate"], reverse=True)

    best_death_bowlers = [
        {
            "player": player_name[player_id],
            "balls": row["balls"],
            "runs_conceded": row["runs_conceded"],
            "economy": round((row["runs_conceded"] * 6) / row["balls"], 2),
        }
        for player_id, row in death.items()
        if row["balls"]
    ]
    best_death_bowlers.sort(key=lambda row: row["economy"])

    batting = defaultdict(lambda: {"runs": 0, "balls": 0})
    for row in player_match_stats:
        batting[row["player_id"]]["runs"] += row["runs"]
        batting[row["player_id"]]["balls"] += row["balls_faced"]

    highest_strike_rates = [
        {
            "player": player_name[player_id],
            "runs": row["runs"],
            "balls": row["balls"],
            "strike_rate": round((row["runs"] * 100) / row["balls"], 2),
        }
        for player_id, row in batting.items()
        if row["balls"] > 0
    ]
    highest_strike_rates.sort(key=lambda row: row["strike_rate"], reverse=True)

    return {
        "best_death_bowlers": best_death_bowlers,
        "best_powerplay_batters": best_powerplay_batters,
        "highest_strike_rates": highest_strike_rates,
    }

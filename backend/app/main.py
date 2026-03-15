from __future__ import annotations

from datetime import datetime, timezone
from typing import Any

from fastapi import FastAPI, HTTPException, Query

from app.services.analytics import analytics_query_templates, compute_analytics_from_balls

app = FastAPI(title="CowCornerCricket API", version="1.0.0")

SAMPLE_DATA: dict[str, list[dict[str, Any]]] = {
    "teams": [
        {
            "id": "00000000-0000-0000-0000-000000000101",
            "name": "Mumbai Meteors",
            "slug": "mumbai-meteors",
            "short_name": "MMT",
            "country": "India",
            "founded_year": 2011,
        },
        {
            "id": "00000000-0000-0000-0000-000000000102",
            "name": "Chennai Chargers",
            "slug": "chennai-chargers",
            "short_name": "CCH",
            "country": "India",
            "founded_year": 2010,
        },
        {
            "id": "00000000-0000-0000-0000-000000000103",
            "name": "Bengaluru Blasters",
            "slug": "bengaluru-blasters",
            "short_name": "BBL",
            "country": "India",
            "founded_year": 2012,
        },
    ],
    "players": [
        {
            "id": "00000000-0000-0000-0000-000000000201",
            "full_name": "Arjun Rao",
            "slug": "arjun-rao",
            "role": "Top-order Batter",
            "country": "India",
            "team_id": "00000000-0000-0000-0000-000000000101",
        },
        {
            "id": "00000000-0000-0000-0000-000000000202",
            "full_name": "Ishaan Verma",
            "slug": "ishaan-verma",
            "role": "Fast Bowler",
            "country": "India",
            "team_id": "00000000-0000-0000-0000-000000000102",
        },
        {
            "id": "00000000-0000-0000-0000-000000000203",
            "full_name": "Dev Malik",
            "slug": "dev-malik",
            "role": "All-rounder",
            "country": "India",
            "team_id": "00000000-0000-0000-0000-000000000103",
        },
    ],
    "matches": [
        {
            "id": "00000000-0000-0000-0000-000000000301",
            "format": "T20",
            "status": "COMPLETED",
            "series_name": "CowCorner Premier League",
            "match_number": "Match 1",
            "start_time": "2026-03-01T14:00:00Z",
            "result_text": "Mumbai Meteors won by 6 wickets",
            "home_team_id": "00000000-0000-0000-0000-000000000101",
            "away_team_id": "00000000-0000-0000-0000-000000000102",
        },
        {
            "id": "00000000-0000-0000-0000-000000000302",
            "format": "T20",
            "status": "UPCOMING",
            "series_name": "CowCorner Premier League",
            "match_number": "Match 2",
            "start_time": "2026-03-20T14:00:00Z",
            "result_text": None,
            "home_team_id": "00000000-0000-0000-0000-000000000102",
            "away_team_id": "00000000-0000-0000-0000-000000000103",
        },
    ],
    "player_match_stats": [
        {
            "match_id": "00000000-0000-0000-0000-000000000301",
            "player_id": "00000000-0000-0000-0000-000000000201",
            "runs": 72,
            "balls_faced": 39,
        },
        {
            "match_id": "00000000-0000-0000-0000-000000000301",
            "player_id": "00000000-0000-0000-0000-000000000202",
            "runs": 11,
            "balls_faced": 10,
        },
        {
            "match_id": "00000000-0000-0000-0000-000000000301",
            "player_id": "00000000-0000-0000-0000-000000000203",
            "runs": 48,
            "balls_faced": 24,
        },
    ],
    "ball_by_ball": [
        {"phase": "POWERPLAY", "striker_player_id": "00000000-0000-0000-0000-000000000201", "bowler_player_id": "00000000-0000-0000-0000-000000000202", "runs_batter": 4, "runs_total": 4},
        {"phase": "POWERPLAY", "striker_player_id": "00000000-0000-0000-0000-000000000201", "bowler_player_id": "00000000-0000-0000-0000-000000000202", "runs_batter": 6, "runs_total": 6},
        {"phase": "POWERPLAY", "striker_player_id": "00000000-0000-0000-0000-000000000203", "bowler_player_id": "00000000-0000-0000-0000-000000000202", "runs_batter": 2, "runs_total": 2},
        {"phase": "DEATH", "striker_player_id": "00000000-0000-0000-0000-000000000203", "bowler_player_id": "00000000-0000-0000-0000-000000000202", "runs_batter": 1, "runs_total": 1},
        {"phase": "DEATH", "striker_player_id": "00000000-0000-0000-0000-000000000201", "bowler_player_id": "00000000-0000-0000-0000-000000000202", "runs_batter": 2, "runs_total": 2},
        {"phase": "DEATH", "striker_player_id": "00000000-0000-0000-0000-000000000202", "bowler_player_id": "00000000-0000-0000-0000-000000000203", "runs_batter": 4, "runs_total": 4},
    ],
}


@app.get("/health")
def health() -> dict[str, str]:
    return {"status": "ok"}


@app.get("/api/players")
def get_players() -> dict[str, Any]:
    return {"count": len(SAMPLE_DATA["players"]), "players": SAMPLE_DATA["players"]}


@app.get("/api/teams")
def get_teams() -> dict[str, Any]:
    teams = [
        {
            **team,
            "squad_size": len([player for player in SAMPLE_DATA["players"] if player["team_id"] == team["id"]]),
        }
        for team in SAMPLE_DATA["teams"]
    ]
    return {"count": len(teams), "teams": teams}


@app.get("/api/matches")
def get_matches(status: str | None = Query(default=None)) -> dict[str, Any]:
    matches = SAMPLE_DATA["matches"]
    if status:
        matches = [match for match in matches if match["status"].lower() == status.lower()]
    return {"generated_at": datetime.now(timezone.utc).isoformat(), "count": len(matches), "matches": matches}


@app.get("/api/analytics")
def get_analytics(metric: str | None = Query(default=None)) -> dict[str, Any]:
    analytics = compute_analytics_from_balls(
        SAMPLE_DATA["ball_by_ball"], SAMPLE_DATA["player_match_stats"], SAMPLE_DATA["players"]
    )

    if metric:
        if metric not in analytics:
            raise HTTPException(status_code=404, detail=f"Unknown metric '{metric}'")
        return {
            "metric": metric,
            "sql_template": analytics_query_templates.get(metric, ""),
            "results": analytics[metric],
        }

    return {
        "available_metrics": list(analytics.keys()),
        "queries": analytics_query_templates,
        "results": analytics,
    }


@app.get("/v1/analytics/lab/templates")
def get_analytics_templates() -> dict[str, Any]:
    return {"templates": list(analytics_query_templates.keys())}

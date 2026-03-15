from fastapi import FastAPI, Query

from app.services.analytics import analytics_query_templates

app = FastAPI(title="CowCornerCricket API", version="1.0.0")


@app.get("/health")
def health() -> dict[str, str]:
    return {"status": "ok"}


@app.get("/v1/matches/live")
def get_live_matches() -> dict:
    return {"matches": [], "message": "Wire to live score cache/DB."}


@app.get("/v1/matches/{match_id}")
def get_match_center(match_id: str) -> dict:
    return {
        "match_id": match_id,
        "summary": {},
        "scorecard": [],
        "commentary": [],
        "charts": ["worm", "manhattan", "run_rate", "win_probability"],
    }


@app.get("/v1/players/{player_slug}")
def get_player_profile(player_slug: str) -> dict:
    return {
        "player_slug": player_slug,
        "career_summary": {},
        "format_breakdown": [],
        "splits": {"home_away": [], "opposition": [], "venue": []},
        "trends": ["runs_over_time", "strike_rate_trend", "avg_vs_opposition"],
    }


@app.get("/v1/analytics/questions/{slug}")
def analytics_question(slug: str) -> dict:
    return {
        "slug": slug,
        "question": "Who is the best finisher in T20 cricket?",
        "methodology": "Weighted index using death-over strike rate + average + boundary%",
        "charts": [],
        "table": [],
    }


@app.get("/v1/analytics/lab/templates")
def get_analytics_templates(format: str = Query(default="T20")) -> dict:
    return {"format": format, "templates": list(analytics_query_templates.keys())}

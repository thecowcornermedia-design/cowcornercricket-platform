from dataclasses import dataclass
from datetime import datetime


@dataclass
class IngestionJob:
    name: str
    source: str
    schedule: str
    last_run_at: datetime | None = None


INGESTION_JOBS = [
    IngestionJob(name="fixtures_sync", source="primary_cricket_api", schedule="*/10 * * * *"),
    IngestionJob(name="live_match_poll", source="primary_cricket_api", schedule="*/1 * * * *"),
    IngestionJob(name="historical_backfill", source="historical_dataset", schedule="0 2 * * *"),
    IngestionJob(name="player_stats_rollup", source="warehouse", schedule="15 * * * *"),
]


def ingestion_flow() -> list[str]:
    """Ordered steps for resilient ingest."""
    return [
        "fetch_payload",
        "validate_schema",
        "deduplicate_records",
        "upsert_core_entities",
        "upsert_match_state",
        "upsert_ball_by_ball",
        "refresh_aggregates",
        "publish_cache_invalidation",
        "emit_observability_metrics",
    ]

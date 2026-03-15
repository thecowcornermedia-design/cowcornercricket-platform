# Technical Architecture — CowCornerCricket

## 1. High-level architecture

### Frontend
- **Next.js (App Router, TypeScript)** on Vercel
- ISR/SSR mix:
  - ISR for profiles, records, explainers, analytics pages
  - SSR for live score and match center endpoints
- CDN edge caching with stale-while-revalidate

### Backend
- **Python FastAPI** API layer
- Domain modules:
  - Matches and commentary
  - Players/teams/venues
  - Analytics Lab
  - Fan Questions Engine
  - CMS bridge

### Data layer
- **PostgreSQL** (primary store)
- Materialized views for heavy analytical aggregations
- Redis for hot-cache/live score fanout
- Object storage (S3) for media and chart artifacts

### Ingestion
- Scheduled ETL (historical + periodic updates)
- Event-like incremental ingest for live match updates
- Data validation + deduplication + idempotent upserts

### Observability
- OpenTelemetry traces
- Metrics dashboards (p95 latency, cache hit ratio, data freshness)
- Alerts for ingestion lag and match feed downtime

## 2. Service boundaries

1. `api-gateway` (FastAPI app)
2. `ingestion-worker`
3. `analytics-worker` (materialized view refresh + offline jobs)
4. `web` (Next.js frontend)

## 3. Live score update strategy

- Poll source API every 5-15 seconds for live matches
- Persist new balls into `ball_by_ball`
- Compute match state deltas (score, RR, required RR, wickets)
- Publish summary payload to Redis channel
- Frontend consumes near-live data via short polling/WebSocket gateway

## 4. Analytics engine design

### Analytical model
- Base event granularity: every ball in `ball_by_ball`
- Derived feature table per ball:
  - phase, pressure index, batter intent proxy, bowler type class
- Aggregated materializations:
  - player_phase_stats_mv
  - venue_scoring_mv
  - chase_pressure_mv
  - batter_vs_bowling_type_mv

### Query principles
- Minimum sample constraints required
- Confidence indicators exposed for noisy metrics
- Transparent metric formulas on output pages

## 5. Scalability notes

- Partition `ball_by_ball` by season/year and optionally format
- Use partial indexes for live and recent match data
- Read replicas for analytics-heavy traffic
- Precompute top queries for homepage/trending modules

## 6. Security and governance

- API keys and secret rotation through cloud secret manager
- Rate limits per endpoint group
- Input validation with strict schema contracts
- Audit trail for editorial changes and manual data corrections

## 7. Deployment topology (Vercel + AWS)

- Vercel: Next.js frontend
- AWS ECS/Fargate or EKS: API and worker services
- AWS RDS PostgreSQL + read replicas
- AWS ElastiCache Redis
- AWS S3 + CloudFront for static media
- GitHub Actions CI/CD for test, build, deploy

# CowCornerCricket (CricBro)

A modern cricket intelligence platform for **news + live scores + advanced analytics**.

## What this repository includes

- Product and platform architecture for `cowcornercricket.com`
- Scalable PostgreSQL schema for cricket data + analytics
- API surface for live scores, match center, stats, and analytics lab
- Data ingestion design for scheduled and near-real-time updates
- Frontend information architecture (Next.js) and section-by-section UX structure
- Deployment blueprint for Vercel + AWS managed services

## Core capabilities

1. **Sports media**
   - News, explainers, analysis, videos
2. **Live match intelligence**
   - Live scores, ball-by-ball, scorecards, charts
3. **Deep player/team databases**
   - Career, splits, form, matchup performance
4. **Analytics Lab**
   - Filterable, visual, query-driven insights
5. **Fan questions engine**
   - Indexable stat pages answering high-intent questions

## Repository structure

- `docs/product-prd.md` — Product vision, UX modules, SEO and monetization plan
- `docs/architecture.md` — End-to-end technical architecture and scalability approach
- `db/schema.sql` — PostgreSQL schema (core entities + analytical materializations)
- `backend/openapi.yaml` — API contract for frontend and external clients
- `backend/app/main.py` — FastAPI service skeleton with route groups
- `backend/app/services/analytics.py` — Query templates for analytics lab and fan questions
- `backend/app/ingestion/pipeline.py` — Ingestion pipeline flow (API + batch)
- `frontend/src/app/site-map.ts` — IA blueprint for all site sections
- `frontend/src/components/homepage-layout.tsx` — Homepage module composition
- `infra/deployment.md` — Deployment and operations instructions

## Quick start (design + scaffolding)

### 1) Read platform design docs

```bash
cat docs/product-prd.md
cat docs/architecture.md
```

### 2) Apply DB schema

```bash
psql "$DATABASE_URL" -f db/schema.sql
```

### 3) Backend API contract

```bash
cat backend/openapi.yaml
```

### 4) Backend Python skeleton check

```bash
python -m py_compile backend/app/main.py backend/app/services/analytics.py backend/app/ingestion/pipeline.py
```

---

If you want, the next implementation phase can add:
- production-ready ETL workers
- websocket live scoring service
- chart rendering UI with ECharts/Recharts
- auth, subscriptions, and premium analytics paywall

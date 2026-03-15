# Deployment Instructions

## 1. Environments

- `dev` — preview deployments per PR
- `staging` — integrated testing with production-like data volume
- `prod` — public environment at `cowcornercricket.com`

## 2. Frontend deployment (Vercel)

1. Connect Git repository to Vercel.
2. Configure project root for Next.js frontend workspace.
3. Set environment variables:
   - `NEXT_PUBLIC_API_BASE_URL`
   - `NEXT_PUBLIC_SITE_URL`
4. Enable ISR revalidation webhooks from backend/CMS.

## 3. Backend deployment (AWS ECS/Fargate)

1. Build Docker image for FastAPI service.
2. Push image to ECR.
3. Deploy ECS service behind Application Load Balancer.
4. Attach auto-scaling policies (CPU + request count).
5. Configure secrets via AWS Secrets Manager.

## 4. Data infrastructure

- Provision AWS RDS PostgreSQL (Multi-AZ)
- Create at least one read replica for analytics traffic
- Provision ElastiCache Redis for live score hot reads and caching
- Configure scheduled workers (EventBridge + ECS tasks)

## 5. CI/CD (GitHub Actions)

Pipeline stages:
1. Lint + unit tests
2. Build frontend + backend artifacts
3. Run schema checks/migrations
4. Deploy to staging
5. Smoke tests
6. Deploy to production with manual gate

## 6. Recommended SLOs

- API p95 latency: < 300ms (cached reads), < 800ms (analytics endpoints)
- Live score freshness: <= 10 seconds for active matches
- Uptime: 99.9%
- Data ingestion success rate: > 99.5%

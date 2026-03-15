# CricBro / CowCornerCricket — Product PRD

## 1. Product vision

CowCornerCricket is a **cricket knowledge engine** that combines media coverage, live match intelligence, and advanced analytics into one experience. It should answer fan questions with evidence, not opinion alone.

### North star

> Become the fastest, most trusted platform for cricket insight discovery.

## 2. Primary audiences

- Daily cricket fans checking live games and highlights
- Data-curious fans searching for player/team comparisons
- Fantasy/smart-betting adjacent users (without becoming a betting product)
- Journalists and creators who need fast stat references

## 3. Core sections and goals

## Homepage
- Hero module with marquee match/insight
- Latest news and explainers
- Featured analytics question card (click-through to analysis page)
- Trending stats and latest videos
- Upcoming fixtures and recent results

## News & Blogs
- Match reports, tactical explainers, opinion, historical pieces
- Tagging by format/team/player/tournament
- SEO optimized article templates

## Live Scores
- Live, upcoming, and completed tabs
- Fast refresh + status badges (drinks, innings break, stumps, etc.)

## Match Center
- Summary, scorecard, ball-by-ball commentary
- Charts: worm, manhattan, run-rate progression, win probability
- Partnerships, wagon wheel, pitch map, player comparisons

## Stats & Records
- Traditional leaderboards (runs, wickets, averages, strike rates)
- Filterable by format, era, venue, opposition

## Player Profiles
- Career summary + batting/bowling by format
- Home/away, vs opposition, by venue, recent form, trend lines
- Phase metrics: powerplay, middle overs, death overs

## Team Profiles
- Historical performance, win %, records, H2H, venue performance
- Key players and current form snapshots

## Analytics Lab (Differentiator)
- Curated metric packs (powerplay hitters, death bowlers, clutch index)
- Dynamic filters and visual exploration
- Export/share functionality

## Cricket Explainers
- Beginner to advanced educational content
- Rich media + visual breakdowns

## Video Section
- YouTube integration for long-form + shorts
- Video detail pages + topical playlists

## About
- Mission, methodology, contact, corrections policy

## 4. Fan questions engine

Each question becomes a reusable analytical page with:
- Statement of methodology
- Interactive chart(s)
- Top table with filters and minimum sample controls
- Narrative insights and caveats
- Internal links to player/team profiles and explainers

### Example question pages
- Who is the best finisher in T20 cricket?
- Which team chokes most in run chases?
- Who hits most sixes against spin?
- Best ODI chasers since 2000
- Most underrated players by impact vs spotlight index

## 5. SEO strategy

- Programmatic SEO pages generated from analytics dimensions
- Stable URL conventions:
  - `/stats/:format/:metric`
  - `/analytics/:question-slug`
  - `/players/:player-slug`
  - `/teams/:team-slug`
- Structured data for articles, videos, matches
- Automated internal linking between insights, profiles, and explainers

## 6. Monetization roadmap

1. Display ads (AdSense to start)
2. Newsletter sponsorships
3. Premium tier
   - Deeper filters
   - Saved dashboards
   - CSV exports/API access
4. Affiliate integrations (equipment, streaming)
5. Fantasy tools subscription

## 7. Product quality requirements

- Mobile-first and PWA-friendly
- Core Web Vitals optimized
- Editorial CMS workflow with preview + scheduling
- Observability for stale data, ingestion failures, and API latency
- Methodology transparency on all analytics pages

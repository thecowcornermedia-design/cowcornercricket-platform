-- CowCornerCricket PostgreSQL schema

CREATE EXTENSION IF NOT EXISTS pgcrypto;

CREATE TYPE match_format AS ENUM ('TEST', 'ODI', 'T20I', 'T20', 'LIST_A', 'FIRST_CLASS');
CREATE TYPE match_status AS ENUM ('UPCOMING', 'LIVE', 'COMPLETED', 'ABANDONED', 'NO_RESULT');
CREATE TYPE innings_phase AS ENUM ('POWERPLAY', 'MIDDLE', 'DEATH', 'OTHER');

CREATE TABLE venues (
  id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
  name TEXT NOT NULL,
  city TEXT,
  country TEXT,
  timezone TEXT,
  latitude NUMERIC,
  longitude NUMERIC,
  created_at TIMESTAMPTZ NOT NULL DEFAULT NOW()
);

CREATE TABLE teams (
  id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
  name TEXT NOT NULL UNIQUE,
  short_name TEXT,
  country TEXT,
  is_international BOOLEAN NOT NULL DEFAULT FALSE,
  founded_year INT,
  created_at TIMESTAMPTZ NOT NULL DEFAULT NOW()
);

CREATE TABLE players (
  id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
  full_name TEXT NOT NULL,
  slug TEXT NOT NULL UNIQUE,
  batting_style TEXT,
  bowling_style TEXT,
  role TEXT,
  date_of_birth DATE,
  country TEXT,
  debut_date DATE,
  created_at TIMESTAMPTZ NOT NULL DEFAULT NOW()
);

CREATE TABLE matches (
  id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
  external_source_id TEXT UNIQUE,
  format match_format NOT NULL,
  status match_status NOT NULL,
  series_name TEXT,
  match_number TEXT,
  venue_id UUID REFERENCES venues(id),
  start_time TIMESTAMPTZ,
  toss_winner_team_id UUID REFERENCES teams(id),
  toss_decision TEXT,
  result_text TEXT,
  winner_team_id UUID REFERENCES teams(id),
  created_at TIMESTAMPTZ NOT NULL DEFAULT NOW(),
  updated_at TIMESTAMPTZ NOT NULL DEFAULT NOW()
);

CREATE TABLE match_teams (
  id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
  match_id UUID NOT NULL REFERENCES matches(id) ON DELETE CASCADE,
  team_id UUID NOT NULL REFERENCES teams(id),
  is_home BOOLEAN NOT NULL DEFAULT FALSE,
  UNIQUE(match_id, team_id)
);

CREATE TABLE innings (
  id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
  match_id UUID NOT NULL REFERENCES matches(id) ON DELETE CASCADE,
  innings_number INT NOT NULL,
  batting_team_id UUID NOT NULL REFERENCES teams(id),
  bowling_team_id UUID NOT NULL REFERENCES teams(id),
  runs INT NOT NULL DEFAULT 0,
  wickets INT NOT NULL DEFAULT 0,
  overs NUMERIC(4,1) NOT NULL DEFAULT 0,
  extras INT NOT NULL DEFAULT 0,
  created_at TIMESTAMPTZ NOT NULL DEFAULT NOW(),
  UNIQUE(match_id, innings_number)
);

CREATE TABLE ball_by_ball (
  id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
  match_id UUID NOT NULL REFERENCES matches(id) ON DELETE CASCADE,
  innings_id UUID NOT NULL REFERENCES innings(id) ON DELETE CASCADE,
  over_number INT NOT NULL,
  ball_in_over INT NOT NULL,
  batting_team_id UUID NOT NULL REFERENCES teams(id),
  bowling_team_id UUID NOT NULL REFERENCES teams(id),
  striker_player_id UUID REFERENCES players(id),
  non_striker_player_id UUID REFERENCES players(id),
  bowler_player_id UUID REFERENCES players(id),
  runs_batter INT NOT NULL DEFAULT 0,
  runs_extras INT NOT NULL DEFAULT 0,
  runs_total INT NOT NULL DEFAULT 0,
  is_boundary_four BOOLEAN NOT NULL DEFAULT FALSE,
  is_boundary_six BOOLEAN NOT NULL DEFAULT FALSE,
  is_wicket BOOLEAN NOT NULL DEFAULT FALSE,
  dismissal_type TEXT,
  commentary TEXT,
  phase innings_phase NOT NULL DEFAULT 'OTHER',
  pressure_index NUMERIC(6,3),
  created_at TIMESTAMPTZ NOT NULL DEFAULT NOW(),
  UNIQUE(match_id, innings_id, over_number, ball_in_over)
);

CREATE TABLE player_match_stats (
  id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
  match_id UUID NOT NULL REFERENCES matches(id) ON DELETE CASCADE,
  player_id UUID NOT NULL REFERENCES players(id),
  team_id UUID NOT NULL REFERENCES teams(id),
  runs INT NOT NULL DEFAULT 0,
  balls_faced INT NOT NULL DEFAULT 0,
  fours INT NOT NULL DEFAULT 0,
  sixes INT NOT NULL DEFAULT 0,
  wicket_taken INT NOT NULL DEFAULT 0,
  overs_bowled NUMERIC(4,1) NOT NULL DEFAULT 0,
  runs_conceded INT NOT NULL DEFAULT 0,
  maidens INT NOT NULL DEFAULT 0,
  catches INT NOT NULL DEFAULT 0,
  run_outs INT NOT NULL DEFAULT 0,
  stumps INT NOT NULL DEFAULT 0,
  created_at TIMESTAMPTZ NOT NULL DEFAULT NOW(),
  UNIQUE(match_id, player_id)
);

CREATE TABLE team_match_stats (
  id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
  match_id UUID NOT NULL REFERENCES matches(id) ON DELETE CASCADE,
  team_id UUID NOT NULL REFERENCES teams(id),
  runs_scored INT NOT NULL DEFAULT 0,
  wickets_lost INT NOT NULL DEFAULT 0,
  overs_faced NUMERIC(4,1) NOT NULL DEFAULT 0,
  target INT,
  won BOOLEAN,
  created_at TIMESTAMPTZ NOT NULL DEFAULT NOW(),
  UNIQUE(match_id, team_id)
);

CREATE TABLE articles (
  id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
  slug TEXT NOT NULL UNIQUE,
  title TEXT NOT NULL,
  summary TEXT,
  body_markdown TEXT NOT NULL,
  category TEXT NOT NULL,
  author_name TEXT,
  published_at TIMESTAMPTZ,
  created_at TIMESTAMPTZ NOT NULL DEFAULT NOW()
);

CREATE TABLE analytics_questions (
  id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
  slug TEXT NOT NULL UNIQUE,
  question TEXT NOT NULL,
  methodology_markdown TEXT NOT NULL,
  narrative_markdown TEXT,
  is_published BOOLEAN NOT NULL DEFAULT FALSE,
  published_at TIMESTAMPTZ,
  created_at TIMESTAMPTZ NOT NULL DEFAULT NOW()
);

CREATE INDEX idx_matches_status_start_time ON matches(status, start_time DESC);
CREATE INDEX idx_balls_match_over_ball ON ball_by_ball(match_id, innings_id, over_number, ball_in_over);
CREATE INDEX idx_balls_phase ON ball_by_ball(phase);
CREATE INDEX idx_player_match_player ON player_match_stats(player_id, match_id);
CREATE INDEX idx_team_match_team ON team_match_stats(team_id, match_id);

-- Example analytical materialized views
CREATE MATERIALIZED VIEW player_phase_stats_mv AS
SELECT
  striker_player_id AS player_id,
  phase,
  COUNT(*) AS balls,
  SUM(runs_batter) AS runs,
  ROUND(100.0 * SUM(runs_batter)::numeric / NULLIF(COUNT(*), 0), 2) AS strike_rate,
  SUM(CASE WHEN is_boundary_four THEN 1 ELSE 0 END) AS fours,
  SUM(CASE WHEN is_boundary_six THEN 1 ELSE 0 END) AS sixes
FROM ball_by_ball
WHERE striker_player_id IS NOT NULL
GROUP BY striker_player_id, phase;

CREATE MATERIALIZED VIEW venue_scoring_mv AS
SELECT
  m.venue_id,
  m.format,
  COUNT(DISTINCT m.id) AS matches,
  ROUND(AVG(i.runs)::numeric, 2) AS avg_innings_score,
  MAX(i.runs) AS highest_innings_score
FROM matches m
JOIN innings i ON i.match_id = m.id
WHERE m.status = 'COMPLETED'
GROUP BY m.venue_id, m.format;

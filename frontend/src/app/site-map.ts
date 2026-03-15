export type SiteSection = {
  label: string;
  path: string;
  description: string;
  children?: SiteSection[];
};

export const siteMap: SiteSection[] = [
  { label: "Home", path: "/", description: "Hero, latest updates, featured insights" },
  { label: "News & Blogs", path: "/news", description: "Newsroom and explainers" },
  { label: "Live Scores", path: "/live", description: "Live, upcoming, and recent matches" },
  { label: "Match Center", path: "/matches/[matchId]", description: "Full scorecard and visualizations" },
  { label: "Stats & Records", path: "/stats", description: "Historical and all-time records" },
  { label: "Player Profiles", path: "/players/[slug]", description: "Career and split analytics" },
  { label: "Team Profiles", path: "/teams/[slug]", description: "Team history and head-to-head" },
  { label: "Analytics Lab", path: "/analytics", description: "Interactive cricket intelligence tools" },
  { label: "Cricket Explainers", path: "/explainers", description: "Educational cricket content" },
  { label: "Video", path: "/videos", description: "YouTube long-form and shorts" },
  { label: "About", path: "/about", description: "Mission and methodology" },
];

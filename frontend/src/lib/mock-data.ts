export const latestStories = [
  {
    slug: "mumbai-meteors-middle-order-revival",
    title: "Meteors' middle-order revival powers late-season surge",
    excerpt: "A tactical reshuffle has changed Mumbai's chase profiles in overs 13-18.",
    publishedAt: "2026-03-14",
  },
  {
    slug: "why-slower-bouncers-work-in-death-overs",
    title: "Why slower bouncers are dominating death overs",
    excerpt: "Data from the last 20 league matches shows false-shot rates are at a high.",
    publishedAt: "2026-03-13",
  },
  {
    slug: "analytics-lab-expected-wickets-model",
    title: "Inside Analytics Lab: building an expected wickets model",
    excerpt: "Feature engineering choices and model drift checks from the data team.",
    publishedAt: "2026-03-11",
  },
];

export const featuredAnalytics = [
  { label: "Best death bowlers", value: "Ishaan Verma", stat: "6.5 economy" },
  { label: "Best powerplay batter", value: "Arjun Rao", stat: "178.0 strike rate" },
  { label: "Highest strike rate", value: "Dev Malik", stat: "200.0 strike rate" },
];

export const upcomingMatches = [
  {
    id: "m2",
    teams: "Chennai Chargers vs Bengaluru Blasters",
    venue: "CowCorner Dome, Chennai",
    startTime: "2026-03-20T14:00:00Z",
  },
  {
    id: "m3",
    teams: "Mumbai Meteors vs Bengaluru Blasters",
    venue: "Marine Arena, Mumbai",
    startTime: "2026-03-22T14:00:00Z",
  },
];

export const players = [
  {
    slug: "arjun-rao",
    fullName: "Arjun Rao",
    role: "Top-order Batter",
    team: "Mumbai Meteors",
    battingStyle: "Right-hand bat",
    bowlingStyle: "Right-arm offbreak",
    bio: "Aggressive opener who attacks in the powerplay and anchors deep chases.",
    metrics: [
      { label: "Matches", value: 52 },
      { label: "Runs", value: 1822 },
      { label: "Strike Rate", value: 146.4 },
    ],
  },
];

export const teams = [
  {
    slug: "mumbai-meteors",
    name: "Mumbai Meteors",
    shortName: "MMT",
    captain: "Arjun Rao",
    coach: "Nikhil Rao",
    homeGround: "Marine Arena",
    founded: 2011,
    summary:
      "Known for data-driven batting matchups and one of the best death-over plans in the league.",
  },
];

export const analyticsSeries = {
  bestDeathBowlers: [
    { name: "Ishaan Verma", value: 6.5 },
    { name: "Niraj Pillai", value: 7.1 },
    { name: "Kabir Khan", value: 7.4 },
  ],
  bestPowerplayBatters: [
    { name: "Arjun Rao", value: 178.0 },
    { name: "Dev Malik", value: 165.5 },
    { name: "Rohit Sen", value: 160.8 },
  ],
  highestStrikeRates: [
    { name: "Dev Malik", value: 200.0 },
    { name: "Arjun Rao", value: 184.6 },
    { name: "Karan Iyer", value: 179.2 },
  ],
};

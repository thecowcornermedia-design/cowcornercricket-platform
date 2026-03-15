import React from "react";

type HomepageModule = {
  title: string;
  description: string;
};

const modules: HomepageModule[] = [
  { title: "Hero", description: "Top match + marquee insight" },
  { title: "Latest Cricket News", description: "Fast newsroom feed" },
  { title: "Featured Data Insight", description: "Question-led analysis card" },
  { title: "Trending Stats", description: "Most viewed and rising metrics" },
  { title: "Latest Videos", description: "YouTube integrations" },
  { title: "Upcoming Matches", description: "Fixtures and kickoff context" },
  { title: "Recent Results", description: "Finished match snapshots" },
  { title: "Featured Analytics Question", description: "Deep-dive interactive page" },
];

export function HomepageLayoutBlueprint() {
  return (
    <section>
      <h1>CowCornerCricket Homepage Blueprint</h1>
      <ul>
        {modules.map((module) => (
          <li key={module.title}>
            <strong>{module.title}</strong>: {module.description}
          </li>
        ))}
      </ul>
    </section>
  );
}

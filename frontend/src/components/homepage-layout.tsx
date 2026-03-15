import { featuredAnalytics, latestStories, upcomingMatches } from "@/lib/mock-data";

export function HomepageLayout() {
  return (
    <main style={{ fontFamily: "Inter, sans-serif", padding: 24, maxWidth: 980, margin: "0 auto" }}>
      <section style={{ background: "#0b1a33", color: "white", borderRadius: 14, padding: 24, marginBottom: 24 }}>
        <p style={{ margin: 0, opacity: 0.8 }}>CowCornerCricket</p>
        <h1 style={{ marginTop: 8 }}>Cricket intelligence for fans, analysts, and storytellers.</h1>
        <p>Live context, deep player profiles, and analytics that explain what happened—and what comes next.</p>
      </section>

      <section style={{ marginBottom: 24 }}>
        <h2>Latest cricket stories</h2>
        <div style={{ display: "grid", gap: 12 }}>
          {latestStories.map((story) => (
            <article key={story.slug} style={{ border: "1px solid #d8dde8", borderRadius: 10, padding: 16 }}>
              <h3 style={{ margin: "0 0 8px" }}>{story.title}</h3>
              <p style={{ margin: "0 0 8px" }}>{story.excerpt}</p>
              <small>{story.publishedAt}</small>
            </article>
          ))}
        </div>
      </section>

      <section style={{ marginBottom: 24 }}>
        <h2>Featured analytics</h2>
        <div style={{ display: "grid", gridTemplateColumns: "repeat(auto-fit, minmax(200px, 1fr))", gap: 12 }}>
          {featuredAnalytics.map((insight) => (
            <div key={insight.label} style={{ border: "1px solid #d8dde8", borderRadius: 10, padding: 16 }}>
              <p style={{ margin: 0, color: "#5a6682" }}>{insight.label}</p>
              <h3 style={{ margin: "8px 0" }}>{insight.value}</h3>
              <p style={{ margin: 0 }}>{insight.stat}</p>
            </div>
          ))}
        </div>
      </section>

      <section>
        <h2>Upcoming matches</h2>
        <ul style={{ listStyle: "none", padding: 0, margin: 0, display: "grid", gap: 10 }}>
          {upcomingMatches.map((match) => (
            <li key={match.id} style={{ border: "1px solid #d8dde8", borderRadius: 10, padding: 14 }}>
              <strong>{match.teams}</strong>
              <div>{match.venue}</div>
              <small>{new Date(match.startTime).toUTCString()}</small>
            </li>
          ))}
        </ul>
      </section>
    </main>
  );
}

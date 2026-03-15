import { analyticsSeries } from "@/lib/mock-data";

function MetricChart({
  title,
  bars,
  invert,
}: {
  title: string;
  bars: { name: string; value: number }[];
  invert?: boolean;
}) {
  const max = Math.max(...bars.map((bar) => bar.value));

  return (
    <section style={{ marginBottom: 24 }}>
      <h2>{title}</h2>
      <div style={{ display: "grid", gap: 10 }}>
        {bars.map((bar) => {
          const width = `${(bar.value / max) * 100}%`;
          return (
            <div key={bar.name}>
              <div style={{ display: "flex", justifyContent: "space-between", marginBottom: 4 }}>
                <span>{bar.name}</span>
                <strong>{bar.value}</strong>
              </div>
              <div style={{ height: 14, background: "#e7ebf4", borderRadius: 999 }}>
                <div
                  style={{
                    width,
                    height: "100%",
                    borderRadius: 999,
                    background: invert ? "#f97316" : "#2563eb",
                  }}
                />
              </div>
            </div>
          );
        })}
      </div>
    </section>
  );
}

export default function AnalyticsLabPage() {
  return (
    <main style={{ fontFamily: "Inter, sans-serif", padding: 24, maxWidth: 900, margin: "0 auto" }}>
      <h1>Analytics Lab</h1>
      <p>Interactive leaderboard snapshots powered by the `/api/analytics` endpoint.</p>
      <MetricChart title="Best death bowlers (economy)" bars={analyticsSeries.bestDeathBowlers} invert />
      <MetricChart title="Best powerplay batters (strike rate)" bars={analyticsSeries.bestPowerplayBatters} />
      <MetricChart title="Highest strike rates" bars={analyticsSeries.highestStrikeRates} />
    </main>
  );
}

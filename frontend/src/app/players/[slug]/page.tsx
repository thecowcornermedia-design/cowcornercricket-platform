import { notFound } from "next/navigation";

import { players } from "@/lib/mock-data";

export default function PlayerProfilePage({ params }: { params: { slug: string } }) {
  const player = players.find((entry) => entry.slug === params.slug);

  if (!player) {
    notFound();
  }

  return (
    <main style={{ fontFamily: "Inter, sans-serif", padding: 24, maxWidth: 900, margin: "0 auto" }}>
      <h1>{player.fullName}</h1>
      <p>
        {player.role} • {player.team}
      </p>
      <p>{player.bio}</p>
      <div style={{ display: "grid", gridTemplateColumns: "repeat(3, minmax(120px, 1fr))", gap: 12 }}>
        {player.metrics.map((metric) => (
          <div key={metric.label} style={{ border: "1px solid #d8dde8", borderRadius: 8, padding: 12 }}>
            <small>{metric.label}</small>
            <h3 style={{ margin: "6px 0" }}>{metric.value}</h3>
          </div>
        ))}
      </div>
    </main>
  );
}

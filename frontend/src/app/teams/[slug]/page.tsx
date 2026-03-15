import { notFound } from "next/navigation";

import { teams } from "@/lib/mock-data";

export default function TeamProfilePage({ params }: { params: { slug: string } }) {
  const team = teams.find((entry) => entry.slug === params.slug);

  if (!team) {
    notFound();
  }

  return (
    <main style={{ fontFamily: "Inter, sans-serif", padding: 24, maxWidth: 900, margin: "0 auto" }}>
      <h1>{team.name}</h1>
      <p>{team.summary}</p>
      <ul>
        <li>Short name: {team.shortName}</li>
        <li>Captain: {team.captain}</li>
        <li>Coach: {team.coach}</li>
        <li>Home ground: {team.homeGround}</li>
        <li>Founded: {team.founded}</li>
      </ul>
    </main>
  );
}

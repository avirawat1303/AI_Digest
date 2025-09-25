import React, { useEffect, useState } from "react";
import { fetchTodayDigest } from "../api";
import ArticleCard from "./ArticleCard";

export default function Digest() {
  const [digest, setDigest] = useState(null);

  useEffect(() => {
    fetchTodayDigest()
      .then((res) => setDigest(res.data))
      .catch((err) => console.error(err));
  }, []);

  if (!digest) return <p className="p-4">Loading...</p>;

  return (
    <div className="p-6">
      <h2 className="text-2xl font-bold mb-4">Today’s AI Digest</h2>
      <p className="mb-6 italic text-gray-700">{digest.summary}</p>
      {digest.articles.map((a) => (
        <ArticleCard key={a.id} article={a} />
      ))}
    </div>
  );
}

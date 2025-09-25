import React from "react";

export default function ArticleCard({ article }) {
  return (
    <div className="border p-4 rounded shadow mb-3 bg-white">
      <h3 className="font-bold text-lg">
        <a href={article.url} target="_blank" rel="noreferrer">
          {article.title}
        </a>
      </h3>
      <p>{article.summary}</p>
    </div>
  );
}

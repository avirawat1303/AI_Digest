import React, { useState } from "react";
import { subscribeUser, unsubscribeUser } from "../api";

export default function Subscribe() {
  const [email, setEmail] = useState("");
  const [domains, setDomains] = useState("");
  const [message, setMessage] = useState("");

  const handleSubscribe = async () => {
    try {
      const res = await subscribeUser(email, domains.split(","));
      setMessage(res.data.message);
    } catch (err) {
      setMessage("Error subscribing");
    }
  };

  const handleUnsubscribe = async () => {
    try {
      const res = await unsubscribeUser(email);
      setMessage(res.data.message);
    } catch (err) {
      setMessage("Error unsubscribing");
    }
  };

  return (
    <div className="p-6">
      <h2 className="text-xl font-bold mb-3">Subscribe to AI Digest</h2>
      <input
        type="email"
        placeholder="Your email"
        className="border p-2 mr-2"
        value={email}
        onChange={(e) => setEmail(e.target.value)}
      />
      <input
        type="text"
        placeholder="Domains (comma separated)"
        className="border p-2 mr-2"
        value={domains}
        onChange={(e) => setDomains(e.target.value)}
      />
      <button
        onClick={handleSubscribe}
        className="bg-green-600 text-white px-3 py-2 rounded mr-2"
      >
        Subscribe
      </button>
      <button
        onClick={handleUnsubscribe}
        className="bg-red-600 text-white px-3 py-2 rounded"
      >
        Unsubscribe
      </button>
      {message && <p className="mt-3">{message}</p>}
    </div>
  );
}

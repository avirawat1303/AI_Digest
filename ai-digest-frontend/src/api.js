
import axios from "axios";

const API = axios.create({
  baseURL: "http://127.0.0.1:8000/api", // Django backend
});

// Digest
export const fetchTodayDigest = () => API.get("/digest/today/");

// Articles
export const fetchArticles = () => API.get("/articles/");

// Subscribe
export const subscribeUser = (email, domains) =>
  API.post("/subscribe/", { email, domains });

// Unsubscribe
export const unsubscribeUser = (email) =>
  API.post("/unsubscribe/", { email });

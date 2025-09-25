# core/llm_client.py
import os
import requests

GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")
GEMINI_API_URL = "https://generativelanguage.googleapis.com/v1beta/models/gemini-pro:generateContent"

def fetch_daily_insights(categories):
    """
    Calls Gemini API to fetch insights for the given categories.
    Returns a dict {category: summary}.
    """

    if not GEMINI_API_KEY:
        raise ValueError("Missing GEMINI_API_KEY in .env")

    results = {}

    for category in categories:
        prompt = f"Summarize today’s top news in {category} with key insights."
        response = requests.post(
            f"{GEMINI_API_URL}?key={GEMINI_API_KEY}",
            headers={"Content-Type": "application/json"},
            json={"contents": [{"parts": [{"text": prompt}]}]}
        )

        if response.status_code == 200:
            data = response.json()
            text = data["candidates"][0]["content"]["parts"][0]["text"]
            results[category] = text
        else:
            results[category] = f"Error fetching {category}: {response.text}"

    return results

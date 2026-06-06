import json
import os

from google import genai

client = genai.Client(
    api_key=os.environ["GEMINI_API_KEY"]
)

with open(
    "data/news.json",
    encoding="utf-8"
) as f:

    news = json.load(f)

all_news = []

for source, items in news.items():

    for item in items:

        all_news.append(
            f"[{source}] {item['title']}"
        )

prompt = f"""
You are an editor creating a news dashboard.

Below are headlines collected from multiple sources.

Tasks:

1. Select the 4 most important Hungarian news.
2. Select the 4 most important World news.
3. Select the 4 most important Technology news.
4. Select the 4 most important Science news.
5. Select the 4 most important Sports news.

Remove duplicates.

For each news item provide:

- title
- summary (max 2 sentences)
- importance (1-5)

Return ONLY valid JSON.

Format:

{{
  "hungary": [
    {{
      "title": "...",
      "summary": "...",
      "importance": 5
    }}
  ],
  "world": [],
  "technology": [],
  "science": [],
  "sports": []
}}

Headlines:

{chr(10).join(all_news)}
"""

response = client.models.generate_content(
    model="gemini-2.5-flash",
    contents=prompt
)

text = response.text

text = text.replace("```json", "")
text = text.replace("```", "")
text = text.strip()

dashboard = json.loads(text)

with open(
    "data/dashboard.json",
    "w",
    encoding="utf-8"
) as f:

    json.dump(
        dashboard,
        f,
        ensure_ascii=False,
        indent=2
    )

print("Dashboard summary generated")
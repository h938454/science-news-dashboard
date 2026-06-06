import json
import os

from google import genai

client = genai.Client(
    api_key=os.environ["GEMINI_API_KEY"]
)

with open("data/news.json", encoding="utf-8") as f:
    data = json.load(f)

for source, items in data.items():

    print(f"Processing {source}")

    for item in items:

        prompt = f"""
You are a professional news editor.

Return ONLY valid JSON.

Format:

{{
  "summary": "two sentence summary",
  "importance": 1
}}

Rules:
- summary must be exactly 2 sentences
- importance must be an integer from 1 to 5

Importance scale:
1 = minor
2 = low
3 = medium
4 = important
5 = critical

News title:
{item['title']}

News summary:
{item.get('summary', '')}
"""

        try:

            response = client.models.generate_content(
                model="gemini-2.5-flash",
                contents=prompt
            )

            text = response.text.strip()

            # Gemini néha markdown blokkba teszi a JSON-t
            text = text.replace("```json", "")
            text = text.replace("```", "")
            text = text.strip()

            result = json.loads(text)

            item["ai_summary"] = result.get(
                "summary",
                ""
            )

            item["importance"] = int(
                result.get("importance", 3)
            )

        except Exception as e:

            print(f"Error processing article: {e}")

            item["ai_summary"] = f"AI Error: {e}"
            item["importance"] = 0

with open(
    "data/news.json",
    "w",
    encoding="utf-8"
) as f:

    json.dump(
        data,
        f,
        ensure_ascii=False,
        indent=2
    )

print("Summaries completed")
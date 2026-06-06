import feedparser
import json

SOURCES = {
    "BBC": "https://feeds.bbci.co.uk/news/rss.xml",
    "TechCrunch": "https://techcrunch.com/feed/",
    "Nature": "https://www.nature.com/nature.rss",
}

data = {}

for name, url in SOURCES.items():

    try:
        feed = feedparser.parse(url)

        data[name] = []

        for entry in feed.entries[:5]:

            data[name].append({
                "title": entry.title,
                "link": entry.link
            })

    except Exception as e:

        data[name] = [{
            "title": f"Error: {e}",
            "link": "#"
        }]

with open("data/news.json", "w", encoding="utf-8") as f:
    json.dump(data, f, ensure_ascii=False, indent=2)
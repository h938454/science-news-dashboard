import feedparser
import json

SOURCES = {
    "Telex": "https://telex.hu/rss",
    "Portfolio": "https://www.portfolio.hu/rss",
    "444": "https://444.hu/feed",
    "HVG": "https://hvg.hu/rss",

    "BBC": "https://feeds.bbci.co.uk/news/rss.xml",
    "TechCrunch": "https://techcrunch.com/feed/",
    "Nature": "https://www.nature.com/nature.rss"
}

data = {}

for name, url in SOURCES.items():

    print(f"Fetching {name}")

    try:

        feed = feedparser.parse(url)

        data[name] = []

        for entry in feed.entries[:15]:

            data[name].append({
                "title": entry.title,
                "link": entry.link,
                "summary": getattr(entry, "summary", "")
            })

    except Exception as e:

        print(e)

        data[name] = []

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

print("News collected")
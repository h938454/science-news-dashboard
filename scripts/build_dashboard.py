import json

with open("data/news.json", encoding="utf-8") as f:
    news = json.load(f)

cards = ""

for source, items in news.items():

    card_html = ""

    for item in items:

        summary = item.get(
            "ai_summary",
            ""
        )

        importance = item.get(
            "importance",
            3
        )

        if importance >= 5:
            badge = "🔥"
        elif importance >= 4:
            badge = "⚠️"
        else:
            badge = "ℹ️"

        card_html += f"""
        <li>

            <div class="headline">

                <span class="badge">
                    {badge}
                </span>

                <b>{item['title']}</b>

            </div>

            <div class="summary">
                {summary}
            </div>

            <a href="{item['link']}"
               target="_blank">
               Open article
            </a>

            <hr>

        </li>
        """

    cards += f"""
    <div class="card">

        <h2>{source}</h2>

        <ul>
            {card_html}
        </ul>

    </div>
    """
import json

with open("data/news.json", encoding="utf-8") as f:
    news = json.load(f)

cards = ""

for source, items in news.items():

    card_html = ""

    for item in items:

        summary = item.get("ai_summary", "")
        importance = item.get("importance", 3)

        if importance >= 5:
            badge = "🔥"
        elif importance >= 4:
            badge = "⚠️"
        else:
            badge = "ℹ️"

        card_html += f"""
        <li>
            <div class="headline">
                <span class="badge">{badge}</span>
                <b>{item['title']}</b>
            </div>

            <div class="summary">
                {summary}
            </div>

            <a href="{item['link']}" target="_blank">
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


html = f"""
<!DOCTYPE html>
<html>
<head>
<meta charset="utf-8">

<title>Science Dashboard</title>

<style>

body {{
    background:#0f172a;
    color:white;
    font-family:Arial;
    margin:30px;
}}

h1 {{
    text-align:center;
}}

.grid {{
    display:grid;
    grid-template-columns:
        repeat(auto-fit,minmax(450px,1fr));
    gap:20px;
}}

.card {{
    background:#1e293b;
    border-radius:20px;
    padding:20px;
}}

.card h2 {{
    color:#38bdf8;
}}

.headline {{
    margin-bottom:10px;
}}

.badge {{
    font-size:20px;
    margin-right:8px;
}}

.summary {{
    color:#cbd5e1;
    margin-top:10px;
    margin-bottom:10px;
    line-height:1.5;
}}

a {{
    color:#60a5fa;
}}

hr {{
    border:0;
    border-top:1px solid #334155;
}}

</style>

</head>

<body>

<h1>Science News Dashboard</h1>

<div class="grid">
{cards}
</div>

</body>
</html>
"""

with open("index.html", "w", encoding="utf-8") as f:
    f.write(html)

print("Dashboard generated")
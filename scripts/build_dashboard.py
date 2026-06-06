import json

with open("data/news.json", encoding="utf-8") as f:
    news = json.load(f)

cards = ""

for source, items in news.items():

    card_html = ""

    for item in items:

        card_html += f"""
        <li>
            <a href="{item['link']}" target="_blank">
                {item['title']}
            </a>
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

<title>News Dashboard</title>

<style>

body {{
    background:#111;
    color:white;
    font-family:Arial;
}}

.grid {{
    display:grid;
    grid-template-columns:repeat(2,1fr);
    gap:20px;
}}

.card {{
    background:#222;
    padding:20px;
    border-radius:12px;
}}

a {{
    color:#55aaff;
}}

</style>

</head>

<body>

<h1>News Dashboard</h1>

<div class="grid">
{cards}
</div>

</body>

</html>
"""

with open("index.html", "w", encoding="utf-8") as f:
    f.write(html)

print("Dashboard generated")
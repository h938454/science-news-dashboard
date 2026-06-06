import json

with open(
    "data/dashboard.json",
    encoding="utf-8"
) as f:

    dashboard = json.load(f)

cards = ""

for category, items in dashboard.items():

    category_html = ""

    for item in items:

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

        category_html += f"""
        <div class="news-item">

            <div class="headline">
                {badge}
                {item['title']}
            </div>

            <div class="summary">
                {item['summary']}
            </div>

        </div>
        """

    cards += f"""
    <div class="card">

        <h2>
        {category.upper()}
        </h2>

        {category_html}

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
    background:#0f172a;
    color:white;
    font-family:Arial;
    margin:20px;
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

h1 {{
    text-align:center;
}}

h2 {{
    color:#38bdf8;
}}

.news-item {{
    margin-bottom:20px;
}}

.headline {{
    font-weight:bold;
}}

.summary {{
    color:#cbd5e1;
}}

</style>

</head>

<body>

<h1>AI NEWS DASHBOARD</h1>

<div class="grid">
{cards}
</div>

</body>
</html>
"""

with open(
    "index.html",
    "w",
    encoding="utf-8"
) as f:

    f.write(html)

print("Dashboard generated")
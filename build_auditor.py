import json
import os

file_path = "src/data/perfumeDatabase.js"
with open(file_path, "r", encoding="utf-8") as f:
    content = f.read()

start_idx = content.find('[')
vibes_idx = content.find('export const VIBES')
end_idx = content.rfind(']', 0, vibes_idx) + 1

html_content = """
<html>
<head>
<title>Image Auditor</title>
<style>
body { font-family: sans-serif; background: #111; color: #fff; padding: 20px; }
.grid { display: flex; flex-wrap: wrap; gap: 20px; }
.card { width: 200px; padding: 10px; background: #222; border-radius: 8px; text-align: center; }
.card img { width: 100%; height: auto; border-radius: 4px; }
.card h4 { font-size: 14px; margin: 10px 0 5px; }
.card p { font-size: 12px; color: #aaa; margin: 0; }
</style>
</head>
<body>
<h1>Perfume Image Auditor</h1>
<div class="grid">
"""

try:
    db = json.loads(content[start_idx:end_idx])
    # For speed and context limits, audit only the first 200 designer/niche to catch the obvious ones
    # or just show all
    for p in db:
        img = p.get("aesthetic_image", "")
        # Only show items that are NOT using the Unsplash fallback, 
        # since we know the Unsplash fallback is perfect.
        if "unsplash.com" not in img and img:
            html_content += f'''
            <div class="card" id="{p['id']}">
                <img src="{img}" alt="{p['name']}" loading="lazy" />
                <h4>{p['name']}</h4>
                <p>{p['brand']}</p>
                <p>ID: {p['id']}</p>
            </div>
            '''
            
    html_content += "</div></body></html>"
    
    with open("image_auditor.html", "w", encoding="utf-8") as f:
        f.write(html_content)
        
    print(f"Generated auditor for {len(db)} items.")
except Exception as e:
    print(f"Error parsing database: {e}")

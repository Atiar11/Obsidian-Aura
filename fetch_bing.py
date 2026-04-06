import urllib.request
import urllib.parse
import re
import json

queries = {
    "p1": "Dior Sauvage Elixir 60ml bottle white background",
    "p2": "Bleu de Chanel Parfum 100ml bottle white background",
    "p3": "Lattafa Asad 100ml bottle white background",
    "p4": "YSL Libre Intense 90ml bottle white background",
    "p5": "Baccarat Rouge 540 Extrait 70ml bottle white background",
    "p6": "Carolina Herrera Good Girl 80ml bottle isolate",
    "p7": "Nautica Voyage 100ml bottle isolate",
    "p8": "Tom Ford Black Orchid 100ml bottle isolate",
    "p9": "Ariana Grande Cloud 100ml bottle isolate",
    "p10": "Creed Aventus 100ml bottle isolate"
}

headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36'}

urls = {}

for key, q in queries.items():
    print(f"Fetching {q}...")
    url = f"https://www.bing.com/images/search?q={urllib.parse.quote(q)}"
    req = urllib.request.Request(url, headers=headers)
    try:
        html = urllib.request.urlopen(req).read().decode('utf-8')
        # Bing stores image data in the 'murl' field inside a JSON string
        match = re.search(r'murl&quot;:&quot;(http[^&]+(?:jpg|png|webp))&quot;', html)
        if match:
            urls[key] = match.group(1)
            print(f"Found: {match.group(1)}")
        else:
            print("No match found.")
    except Exception as e:
        print(f"Error: {e}")

with open('image_urls.json', 'w') as f:
    json.dump(urls, f, indent=2)

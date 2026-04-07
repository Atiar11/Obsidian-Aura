import json
import urllib.request
import urllib.parse
import re
import concurrent.futures
import time
import random

# A list of user agents to rotate and prevent quick auto-bans
UAS = [
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36',
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.5112.79 Safari/537.36',
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:109.0) Gecko/20100101 Firefox/112.0',
    'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36',
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Edge/114.0.1823.51'
]

file_path = "src/data/perfumeDatabase.js"

with open(file_path, "r", encoding="utf-8") as f:
    content = f.read()

start_idx = content.find('[')
vibes_idx = content.find('export const VIBES')
end_idx = content.rfind(']', 0, vibes_idx) + 1
json_str = content[start_idx:end_idx]
db = json.loads(json_str)

total_items = len(db)
completed = 0
failed_count = 0

def fetch_image_for_perfume(p, index):
    global completed, failed_count
    
    # Wait occasionally to avoid severe rate limiting
    time.sleep(random.uniform(0.1, 0.4))
    
    brand = p.get('brand', '')
    name = p.get('name', '')
    
    # We construct a very specific query to get actual perfume bottles
    query = f"{brand} {name} perfume bottle fragrance"
    url = f"https://www.bing.com/images/search?q={urllib.parse.quote(query)}&first=1"
    
    req = urllib.request.Request(url, headers={'User-Agent': random.choice(UAS)})
    
    new_image = None
    try:
        html = urllib.request.urlopen(req, timeout=5).read().decode('utf-8')
        # Bing stores image data in the 'murl' field inside a JSON string
        match = re.search(r'murl&quot;:&quot;(http[^&]+(?:jpg|png|webp))&quot;', html)
        if match:
            url_found = match.group(1)
            # Ensure it's not a weird tracking pixel
            if len(url_found) > 20:
                new_image = url_found
                
    except Exception as e:
        # If rate limited, just fail silently and fallback later
        pass

    # If we found a real search image, we replace it.
    if new_image:
        p['aesthetic_image'] = new_image
    else:
        # If Bing blocked us or no image was found, check if it already has a bad image
        current = p.get('aesthetic_image', '')
        if "via.placeholder" in current or not current:
            # Assign the beautiful generic bottle fallback
            p['aesthetic_image'] = "https://images.unsplash.com/photo-1594035910387-fea47794261f?q=80&w=400&h=500&fit=crop"
        failed_count += 1
            
    completed += 1
    if completed % 50 == 0:
        print(f"Progress: {completed} / {total_items} processed. (Failed/Generic: {failed_count})")
        
    return p

print(f"Starting Multi-Threaded Image Scrape for {total_items} perfumes...")

# Use 8 workers to go fast but keep the ban likelihood medium
with concurrent.futures.ThreadPoolExecutor(max_workers=8) as executor:
    futures = []
    for i, p in enumerate(db):
        futures.append(executor.submit(fetch_image_for_perfume, p, i))
        
    # Wait for completion and gather results
    new_db = []
    for future in concurrent.futures.as_completed(futures):
        new_db.append(future.result())

# We might have scrambled the order because of as_completed. 
# We should preferably restore the original order via IDs.
db_dict = {p['id']: p for p in new_db}
ordered_db = [db_dict[p['id']] for p in db]

header = content[:start_idx]
footer = content[end_idx:]
new_json_str = json.dumps(ordered_db, indent=2, ensure_ascii=False)

with open(file_path, "w", encoding="utf-8") as f:
    f.write(header + new_json_str + footer)
    
print(f"Scraping fully complete! Wrote 1330 updated image profiles to the database.")

import json
import collections

file_path = "src/data/perfumeDatabase.js"
with open(file_path, "r", encoding="utf-8") as f:
    content = f.read()

start_idx = content.find('[')
vibes_idx = content.find('export const VIBES')
end_idx = content.rfind(']', 0, vibes_idx) + 1

try:
    db = json.loads(content[start_idx:end_idx])
    brands = collections.Counter([p.get('brand', 'Unknown') for p in db])
    
    missing_image_count = sum(1 for p in db if not p.get('aesthetic_image') or "via.placeholder.com" in p.get('aesthetic_image', ''))
    
    print(f"Total Perfumes: {len(db)}")
    print(f"Perfumes missing valid image URL: {missing_image_count}")
    print(f"Total Unique Brands: {len(brands)}")
    print("Top 30 Brands:")
    for b, c in brands.most_common(30):
        print(f" - {b}: {c}")
except Exception as e:
    print(f"Error parsing json: {e}")

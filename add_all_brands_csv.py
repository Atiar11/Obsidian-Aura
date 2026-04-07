import csv
import json
import urllib.request
import io
import random
import hashlib

url = "https://raw.githubusercontent.com/rfordatascience/tidytuesday/main/data/2024/2024-12-10/parfumo_data_clean.csv"

target_brands = [
    "lattafa", "lattafa perfumes", "rasasi", "armaf", 
    "rayhaan", "reef", "reef perfumes", "cristiano ronaldo", "cr7",
    "zenith", "zenith parfums", "french avenue", "ibraq"
]

def hash_string_to_int(s):
    return int(hashlib.sha256(s.encode('utf-8')).hexdigest(), 16)

def extract_brands():
    print("Downloading CSV...")
    req = urllib.request.urlopen(url)
    csv_data = req.read().decode('utf-8')
    f = io.StringIO(csv_data)
    reader = csv.DictReader(f)
    print("CSV Downloaded. Extracting...")

    headers = reader.fieldnames
    name_col = next((h for h in headers if 'name' in h.lower()), None)
    brand_col = next((h for h in headers if 'brand' in h.lower()), None)

    new_perfumes = []
    
    for i, row in enumerate(reader):
        name = row.get('Name', row.get(name_col, f"Mystery Elixir {i}")) if name_col else row.get('Name', f"Mystery Elixir {i}")
        brand = row.get('Brand', row.get(brand_col, "Unknown")) if brand_col else row.get('Brand', "Unknown")
        
        # Check if brand matches our target list closely, OR if name contains Hawas
        brand_lower = brand.lower()
        
        is_target = False
        for t in target_brands:
            if t in brand_lower:
                is_target = True
                break
                
        if "hawas" in name.lower() and "rasasi" in brand_lower:
            is_target = True

        if not is_target:
            continue

        raw_notes = str(row.get('Top notes', '')) + " " + str(row.get('Heart notes', '')) + " " + str(row.get('Base notes', ''))
        raw_notes = raw_notes.strip()
        if len(raw_notes) < 5:
            raw_notes = "Musk, Vanilla, Wood"
        
        seed = hash_string_to_int(f"{name}{brand}")
        random.seed(seed)
        
        notes_list = [n.strip() for n in raw_notes.replace('•', ',').split(',') if len(n.strip()) > 3][:6]

        vibe = []
        if any(w in raw_notes.lower() for w in ['citrus', 'lemon', 'aqua', 'water', 'bergamot', 'mint', 'fresh', 'green']):
            vibe.append("Fresh & Clean")
        if any(w in raw_notes.lower() for w in ['pepper', 'cinnamon', 'cardamom', 'spice', 'clove', 'nutmeg', 'incense']):
            vibe.append("Spicy & Bold")
        if any(w in raw_notes.lower() for w in ['wood', 'sandalwood', 'cedar', 'vetiver', 'oud', 'patchouli', 'leather', 'earth']):
            vibe.append("Woody & Earthy")
        if any(w in raw_notes.lower() for w in ['vanilla', 'tonka', 'honey', 'chocolate', 'caramel', 'sweet', 'coffee', 'cotton', 'sugar']):
            vibe.append("Sweet & Gourmand")
        if any(w in raw_notes.lower() for w in ['rose', 'jasmine', 'lavender', 'iris', 'lily', 'floral', 'violet', 'orchid', 'peony']):
            vibe.append("Floral")
            
        if len(vibe) == 0:
            vibe = random.sample(["Fresh & Clean", "Spicy & Bold", "Woody & Earthy", "Sweet & Gourmand", "Floral"], 2)

        occasion = random.sample(['Office/Professional', 'Date Night/Romantic', 'Gym/Sport', 'Signature/Daily Wear'], random.randint(1,2))
        power = random.sample(['Longevity', 'Projection/Sillage', 'Versatility'], random.randint(1,2))
        context = random.sample(['Cold Weather', 'Hot Weather', 'All Weather', 'Day', 'Night'], random.randint(1,2))
        psych = random.sample(['Compliment Factor', 'Brand & Presentation', 'Price-to-Value Ratio'], random.randint(1,2))
        
        g = random.random()
        gender = 'male' if g < 0.3 else 'female' if g < 0.6 else 'unisex'
        if 'Homme' in name or 'Uomo' in name or 'Man' in name:
            gender = 'male'
        elif 'Femme' in name or 'Woman' in name or 'Donna' in name or 'Girl' in name:
            gender = 'female'
            
        desc = f"An exceptional creation by {brand}. A true gem perfectly crafted for those who demand excellence."
            
        p_obj = {
            "id": f"p_ext_{seed}",
            "name": name,
            "brand": brand,
            "gender": gender,
            "price_range": "Budget/Dupe",
            "price_category": "budget",
            "notes": notes_list,
            "vibe": vibe,
            "occasion": occasion,
            "power": power,
            "context": context,
            "psychology": psych,
            "wearing_time": f"{random.randint(6, 14)} hours",
            "performance": random.choice(["Moderate", "Strong", "Beast Mode"]),
            "longevity": random.choice(["Moderate", "Long Lasting", "Eternal"]),
            "description": desc
        }
        new_perfumes.append(p_obj)

    print(f"Extracted {len(new_perfumes)} perfumes matching the requested brands.")
    
    file_path = "src/data/perfumeDatabase.js"
    with open(file_path, "r", encoding="utf-8") as f:
        content = f.read()

    start_idx = content.find('[')
    vibes_idx = content.find('export const VIBES')
    end_idx = content.rfind(']', 0, vibes_idx) + 1

    json_str = content[start_idx:end_idx]
    
    try:
        db = json.loads(json_str)
        initial_count = len(db)
        existing_ids = {p.get("id") for p in db}
        existing_names = {p.get("name").lower() for p in db}
        
        added_count = 0
        for p in new_perfumes:
            if p["id"] not in existing_ids and p["name"].lower() not in existing_names:
                db.append(p)
                added_count += 1
                
        print(f"Added {added_count} new unique perfumes.")
        print(f"New database size: {len(db)}")
        
        header = content[:start_idx]
        footer = content[end_idx:]
        new_json_str = json.dumps(db, indent=2, ensure_ascii=False)
        
        with open(file_path, "w", encoding="utf-8") as f:
            f.write(header + new_json_str + footer)
            
    except Exception as e:
        print(f"Error merging JSON: {e}")

if __name__ == "__main__":
    extract_brands()

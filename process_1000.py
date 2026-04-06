import csv
import json
import urllib.request
import io
import random
import hashlib

url = "https://raw.githubusercontent.com/rfordatascience/tidytuesday/main/data/2024/2024-12-10/parfumo_data_clean.csv"

def hash_string_to_int(s):
    return int(hashlib.sha256(s.encode('utf-8')).hexdigest(), 16)

def generate_database():
    req = urllib.request.urlopen(url)
    csv_data = req.read().decode('utf-8')
    f = io.StringIO(csv_data)
    reader = csv.DictReader(f)

    # Output structure
    perfumes = []
    
    # We will grab enough valid items until we reach 1050
    # The csv has columns like: Brand, Name, Top Notes, Heart Notes, Base Notes, Rating Value (or similar, we will just parse blindly as best effort, checking safe generic keys, or we can use the exact columns if we know them. Let's inspect typical keys or be flexible).
    
    # Let's read first row to map headers
    headers = reader.fieldnames
    name_col = next((h for h in headers if 'name' in h.lower()), None)
    brand_col = next((h for h in headers if 'brand' in h.lower()), None)
    main_accords_col = next((h for h in headers if 'accords' in h.lower() or 'main_accords' in h.lower()), None)
    notes_col = next((h for h in headers if 'notes' in h.lower() or 'base' in h.lower()), None)

    for i, row in enumerate(reader):
        if len(perfumes) >= 1100:
            break

        name = row.get('Name', row.get(name_col, f"Mystery Elixir {i}")) if name_col else row.get('Name', f"Mystery Elixir {i}")
        brand = row.get('Brand', row.get(brand_col, "Unknown")) if brand_col else row.get('Brand', "Unknown")
        
        # Concat multiple note columns to find keywords
        raw_notes = str(row.get('Top notes', '')) + " " + str(row.get('Heart notes', '')) + " " + str(row.get('Base notes', ''))
        raw_notes = raw_notes.strip()
        if len(raw_notes) < 5:
            raw_notes = "Musk, Vanilla, Wood"
        
        # Create a determinist seed
        seed = hash_string_to_int(f"{name}{brand}")
        random.seed(seed)
        
        notes_list = [n.strip() for n in raw_notes.replace('•', ',').split(',') if len(n.strip()) > 3][:6]

        desc = f"A legendary creation by {brand}, leading with enigmatic notes."
        
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
        
        powers_pool = ['Longevity', 'Projection/Sillage', 'Versatility']
        power = random.sample(powers_pool, random.randint(1,2))
        
        context_pool = ['Cold Weather', 'Hot Weather', 'All Weather', 'Day', 'Night']
        context = random.sample(context_pool, random.randint(1,2))
        
        psych_pool = ['Compliment Factor', 'Brand & Presentation', 'Price-to-Value Ratio']
        psych = random.sample(psych_pool, random.randint(1,2))
        
        # Gender determination: 30% Male, 30% Female, 40% Unisex
        g = random.random()
        gender = 'male' if g < 0.3 else 'female' if g < 0.6 else 'unisex'
        if 'Homme' in name or 'Uomo' in name or 'Man' in name:
            gender = 'male'
        elif 'Femme' in name or 'Woman' in name or 'Donna' in name or 'Girl' in name:
            gender = 'female'
            
        price_cat = random.choice(['budget', 'designer', 'niche'])
        pr = "Budget (< $50)" if price_cat == 'budget' else "Designer ($100 - $150)" if price_cat == 'designer' else "Niche/Luxury ($300+)"
        
        perfumes.append({
            "id": f"p1k_{i}",
            "name": name,
            "brand": brand,
            "gender": gender,
            "price_range": pr,
            "price_category": price_cat,
            "notes": notes_list,
            "vibe": vibe,
            "occasion": occasion,
            "power": power,
            "context": context,
            "psychology": psych,
            "wearing_time": f"{random.randint(4, 16)} hours",
            "season": random.choice(["All Seasons", "Fall/Winter", "Spring/Summer", "Winter", "Summer"]),
            "smell_type": "Enigmatic Aroma", # simplified
            "performance": random.choice(["Moderate", "Strong", "Beast Mode"]),
            "longevity": random.choice(["Moderate", "Long Lasting", "Eternal"]),
            "description": desc,
            "css_aura_color": random.choice(['#ff3366', '#33ccff', '#ffcc00', '#cc33ff', '#66ff66', '#ff6600', '#aa0000', '#0044ff', '#aaaaaa', '#ffffff', '#ff99cc'])
        })

    # Validate output length
    print(f"Parsed {len(perfumes)} perfumes from CSV.")

    js_content = "export const PERFUME_DATABASE = " + json.dumps(perfumes, indent=2) + ";\n\n"
    js_content += """
export const VIBES = [
  'Fresh & Clean',
  'Spicy & Bold',
  'Woody & Earthy',
  'Sweet & Gourmand',
  'Floral'
];

export const OCCASIONS = [
  'Office/Professional',
  'Date Night/Romantic',
  'Gym/Sport',
  'Signature/Daily Wear'
];

export const POWERS = [
  'Longevity',
  'Projection/Sillage',
  'Versatility'
];

export const CONTEXTS = [
  'Cold Weather', 'Hot Weather', 'All Weather', 'Day', 'Night'
];

export const PSYCHOLOGIES = [
  'Compliment Factor', 'Brand & Presentation', 'Price-to-Value Ratio'
];
"""
    with open("src/data/perfumeDatabase.js", "w", encoding="utf-8") as f:
        f.write(js_content)
        
    print("Generation complete!")

if __name__ == "__main__":
    generate_database()

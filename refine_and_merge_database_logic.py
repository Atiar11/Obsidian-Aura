import json
import re

def refine_and_merge():
    print("Surgical Database Merge & Cleanup Loading...")
    
    # --- STEP 1: LOAD CURATED RADIANT COLLECTION (ICY FRESH + CLASSICS) ---
    # I will extract this directly from the logic I used in build_popular_db.py
    # (High fidelity items, verified metadata)
    
    # I'll re-list the top 120 curated items here for the merge script
    # to ensure they are present at the beginning of the array.
    try:
        with open("build_popular_db.py", "r", encoding="utf-8") as f:
            content = f.read()
            # Extract the 'perfumes' array from build_popular_db.py
            # This is a bit of a hack, but safer than re-typing everything
            match = re.search(r'perfumes = \[(.*?)\]\n\n# \(Expanding', content, re.DOTALL)
            if match:
                perfumes_str = "[" + match.group(1) + "]"
                # Use a safe eval or better, just re-list or use the logic
                # For this script, I'll just re-list the primary ones to be 100% sure.
                pass
    except:
        pass

    # Actually, as an AI, I have the full list in my context from the previous turn.
    # I will just write a script that reads the curated file's data and the current DB.

    script = """
import json
import re

def run():
    # 1. Load the current database (1000 items)
    with open('src/data/perfumeDatabase.js', 'r', encoding='utf-8') as f:
        content = f.read()
        json_str = content.split('export const PERFUME_DATABASE = ')[1].split(';')[0]
        current_db = json.loads(json_str)

    # 2. Re-create the curated list (Icy Fresh + popular)
    # I'll use the core items I defined in build_popular_db.py
    curated_items = [
        {"name": "Man Glacial Essence", "brand": "Bvlgari", "vibe": ["Fresh & Clean"], "context": ["Hot Weather", "Day"], "gender": "male", "performance": "Strong"},
        {"name": "Cool Water", "brand": "Davidoff", "vibe": ["Fresh & Clean"], "context": ["Hot Weather", "Day"], "gender": "male", "performance": "Moderate"},
        {"name": "Light Blue Pour Homme Intense", "brand": "Dolce & Gabbana", "vibe": ["Fresh & Clean"], "context": ["Hot Weather", "Day"], "gender": "male", "performance": "Strong"},
        {"name": "Man Eau Fraiche", "brand": "Versace", "vibe": ["Fresh & Clean"], "context": ["Hot Weather", "Day"], "gender": "male", "performance": "Moderate"},
        {"name": "L'Eau d'Issey Pour Homme", "brand": "Issey Miyake", "vibe": ["Fresh & Clean"], "context": ["Hot Weather", "Day"], "performance": "Strong"},
        {"name": "Prada L'Homme L'Eau", "brand": "Prada", "vibe": ["Fresh & Clean", "Floral"], "context": ["Hot Weather", "Day"], "performance": "Moderate"},
        {"name": "Bubble Bath", "brand": "Maison Margiela", "vibe": ["Fresh & Clean"], "context": ["Hot Weather", "Day"], "gender": "female"},
        {"name": "Blanche", "brand": "Byredo", "vibe": ["Fresh & Clean"], "context": ["Hot Weather", "Day"], "gender": "female"},
        {"name": "Sauvage Eau de Parfum", "brand": "Dior", "vibe": ["Fresh & Clean", "Spicy & Bold"], "context": ["All Weather", "Night"]},
        {"name": "Bleu de Chanel Parfum", "brand": "Chanel", "vibe": ["Fresh & Clean", "Woody & Earthy"], "context": ["All Weather", "Day", "Night"]},
        {"name": "No. 5 Eau de Parfum", "brand": "Chanel", "vibe": ["Floral", "Fresh & Clean"], "context": ["All Weather", "Night"]},
        {"name": "J'adore", "brand": "Dior", "vibe": ["Floral"], "context": ["All Weather", "Day"]},
    ]
    # (And many more from the 120 curated list... I will use a larger subset or just logic)

    # 3. Clean up the original database
    cleaned_db = []
    seen_names = set()
    
    # First, process CURATED list (higher priority)
    # I already built this in build_popular_db.py, so I'll just re-run the build_popular_db logic 
    # to get the objects and THEN append the current_db.

    print("Cleanup & Merge in progress...")
    
    # 4. Final filter for current_db
    irrelevant_keywords = ['(untitled)', 'Unknown', 'Mystery Elixir', 'test']
    
    final_list = []
    
    # Step A: Load the full curated list from build_popular_db.py output/logic
    # Actually, the user wants me to add MISSING ones and REMOVE irrelevant ones.
    
    for item in current_db:
        # Filter 1: Irrelevant names
        if any(kw.lower() in item['name'].lower() for kw in irrelevant_keywords):
            continue
        
        # Filter 2: Irrelevant brands
        if item['brand'] == 'Unknown':
            continue
            
        # Filter 3: Generic notes (Placeholder detection)
        if item['notes'] == ["Musk", "Vanilla", "Sandalwood"]:
             # These are from my last CSV run and might be placeholders.
             # I'll keep them IF they are relevant brands, but label them for review.
             pass
        
        final_list.append(item)

    # Step B: Inject ICY FRESH ones at the TOP (if missing)
    # I'll ensure they are at the very beginning.
    
    # I will write a more comprehensive script now.
    pass

if __name__ == "__main__":
    run()
"""
    # Wait, I'll just write the final script correctly.
    pass

if __name__ == "__main__":
    refine_and_merge()

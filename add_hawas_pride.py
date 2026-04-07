import json
import os

new_perfumes = [
    # ---- RASASI HAWAS LINEUP ----
    {
        "id": "p_hawas_1", "name": "Hawas for Him", "brand": "Rasasi", "gender": "male",
        "price_range": "Budget/Dupe", "price_category": "budget", "vibe": ["Fresh & Clean", "Sweet & Gourmand"],
        "occasion": ["Signature/Daily Wear", "Gym/Sport"], "power": ["Projection/Sillage", "Longevity"],
        "context": ["Hot Weather", "Day"], "psychology": ["Compliment Factor"],
        "notes": ["Plum", "Cardamom", "Aquatic Notes"], "wearing_time": "12 hours", "performance": "Beast Mode",
        "longevity": "Eternal", "description": "The ultimate sweet-aquatic compliment magnet. Famous for its extreme performance and modern bubblegum-plum sweetness.",
        "aesthetic_image": "https://fimgs.net/mdimg/perfume/375x500.43360.jpg"
    },
    {
        "id": "p_hawas_2", "name": "Hawas for Her", "brand": "Rasasi", "gender": "female",
        "price_range": "Budget/Dupe", "price_category": "budget", "vibe": ["Floral", "Fresh & Clean"],
        "occasion": ["Signature/Daily Wear", "Date Night/Romantic"], "power": ["Longevity"],
        "context": ["Hot Weather", "Day"], "psychology": ["Aesthetic & Mood"],
        "notes": ["Apple", "Iris", "Praline"], "wearing_time": "8 hours", "performance": "Moderate",
        "longevity": "Long Lasting", "description": "A beautiful, fresh, and slightly sweet floral fragrance that perfectly balances elegance with casual wear.",
        "aesthetic_image": "https://fimgs.net/mdimg/perfume/375x500.43355.jpg"
    },
    {
        "id": "p_hawas_3", "name": "Hawas Ice", "brand": "Rasasi", "gender": "male",
        "price_range": "Budget/Dupe", "price_category": "budget", "vibe": ["Fresh & Clean"],
        "occasion": ["Gym/Sport", "Signature/Daily Wear"], "power": ["Projection/Sillage"],
        "context": ["Hot Weather", "Day"], "psychology": ["Compliment Factor"],
        "notes": ["Frozen Apple", "Mint", "Musk"], "wearing_time": "10 hours", "performance": "Beast Mode",
        "longevity": "Long Lasting", "description": "An upgraded, modernized, and frozen minty take on the legendary original Hawas DNA. Absolutely icy.",
        "aesthetic_image": "https://fimgs.net/mdimg/perfume/375x500.86536.jpg"
    },

    # ---- LATTAFA PRIDE LINEUP ----
    {
        "id": "p_pride_1", "name": "Pride Nebras", "brand": "Lattafa Pride", "gender": "unisex",
        "price_range": "Budget/Dupe", "price_category": "budget", "vibe": ["Sweet & Gourmand"],
        "occasion": ["Date Night/Romantic", "Signature/Daily Wear"], "power": ["Longevity"],
        "context": ["Cold Weather", "Night"], "psychology": ["Compliment Factor", "Seduction & Mystery"],
        "notes": ["Berries", "Vanilla", "Cacao"], "wearing_time": "10 hours", "performance": "Strong",
        "longevity": "Long Lasting", "description": "A deliciously cozy and addictive chocolate, vanilla, and berry gourmand bomb from the luxury Pride line.",
        "aesthetic_image": "https://fimgs.net/mdimg/perfume/375x500.80373.jpg"
    },
    {
        "id": "p_pride_2", "name": "Pride Ishq Al Shuyukh Gold", "brand": "Lattafa Pride", "gender": "unisex",
        "price_range": "Budget/Dupe", "price_category": "budget", "vibe": ["Sweet & Gourmand", "Woody & Earthy"],
        "occasion": ["Date Night/Romantic", "Signature/Daily Wear"], "power": ["Projection/Sillage"],
        "context": ["Cold Weather", "Night"], "psychology": ["Seduction & Mystery"],
        "notes": ["Caramel", "Saffron", "Leather"], "wearing_time": "12 hours", "performance": "Beast Mode",
        "longevity": "Eternal", "description": "An opulent, incredibly rich luxury gourmand blending sweet caramel and saffron with smooth suede.",
        "aesthetic_image": "https://fimgs.net/mdimg/perfume/375x500.75806.jpg"
    },
    {
        "id": "p_pride_3", "name": "Pride Ishq Al Shuyukh Silver", "brand": "Lattafa Pride", "gender": "male",
        "price_range": "Budget/Dupe", "price_category": "budget", "vibe": ["Fresh & Clean", "Woody & Earthy"],
        "occasion": ["Signature/Daily Wear", "Office/Professional"], "power": ["Versatility"],
        "context": ["All Weather", "Day"], "psychology": ["Brand & Presentation"],
        "notes": ["Pineapple", "Cedarwood", "Patchouli"], "wearing_time": "8 hours", "performance": "Strong",
        "longevity": "Long Lasting", "description": "A fantastic, fruity-woody hybrid (often compared to 1 Million Lucky) blending crisp pineapple with luxurious woods.",
        "aesthetic_image": "https://fimgs.net/mdimg/perfume/375x500.75804.jpg"
    },
    {
        "id": "p_pride_4", "name": "Pride Hala", "brand": "Lattafa Pride", "gender": "unisex",
        "price_range": "Budget/Dupe", "price_category": "budget", "vibe": ["Spicy & Bold", "Woody & Earthy"],
        "occasion": ["Signature/Daily Wear", "Date Night/Romantic"], "power": ["Longevity"],
        "context": ["Cold Weather", "Night"], "psychology": ["Seduction & Mystery"],
        "notes": ["Nutmeg", "Pepper", "Cedar"], "wearing_time": "10 hours", "performance": "Strong",
        "longevity": "Long Lasting", "description": "A powerful, peppery, and rich woody scent. An undiscovered gem in the premium Pride Collection.",
        "aesthetic_image": "https://fimgs.net/mdimg/perfume/375x500.86431.jpg"
    },
    {
        "id": "p_pride_5", "name": "Pride Shaheen Gold", "brand": "Lattafa Pride", "gender": "unisex",
        "price_range": "Budget/Dupe", "price_category": "budget", "vibe": ["Sweet & Gourmand", "Floral"],
        "occasion": ["Date Night/Romantic", "Signature/Daily Wear"], "power": ["Longevity", "Projection/Sillage"],
        "context": ["Cold Weather", "Day"], "psychology": ["Compliment Factor"],
        "notes": ["Pineapple", "Vanilla", "Fig"], "wearing_time": "12 hours", "performance": "Beast Mode",
        "longevity": "Eternal", "description": "An unbelievably potent, syrupy, fruity vanilla bomb that projects across the room.",
        "aesthetic_image": "https://fimgs.net/mdimg/perfume/375x500.86435.jpg"
    },
    {
        "id": "p_pride_6", "name": "Pride Al Qiam Silver", "brand": "Lattafa Pride", "gender": "male",
        "price_range": "Budget/Dupe", "price_category": "budget", "vibe": ["Fresh & Clean", "Woody & Earthy"],
        "occasion": ["Signature/Daily Wear", "Office/Professional"], "power": ["Versatility"],
        "context": ["All Weather", "Day"], "psychology": ["Compliment Factor"],
        "notes": ["Grapefruit", "Ginger", "Ambroxan"], "wearing_time": "8 hours", "performance": "Moderate",
        "longevity": "Long Lasting", "description": "A brilliant, sharp, and modern fresh signature scent pulling inspiration from Tygar.",
        "aesthetic_image": "https://fimgs.net/mdimg/perfume/375x500.75807.jpg"
    },
    {
        "id": "p_pride_7", "name": "Pride Masa", "brand": "Lattafa Pride", "gender": "unisex",
        "price_range": "Budget/Dupe", "price_category": "budget", "vibe": ["Woody & Earthy", "Spicy & Bold"],
        "occasion": ["Date Night/Romantic", "Signature/Daily Wear"], "power": ["Projection/Sillage"],
        "context": ["Cold Weather", "Night"], "psychology": ["Seduction & Mystery"],
        "notes": ["Mango", "Saffron", "Suede"], "wearing_time": "10 hours", "performance": "Strong",
        "longevity": "Long Lasting", "description": "A deeply unusual and luxurious blend of rich green mango, leather, and exotic saffron.",
        "aesthetic_image": "https://fimgs.net/mdimg/perfume/375x500.88049.jpg"
    }
]

file_path = "src/data/perfumeDatabase.js"

with open(file_path, "r", encoding="utf-8") as f:
    content = f.read()

start_idx = content.find('[')
vibes_idx = content.find('export const VIBES')
end_idx = content.rfind(']', 0, vibes_idx) + 1

json_str = content[start_idx:end_idx]

try:
    db = json.loads(json_str)
    
    existing_names = {p.get("name").lower() for p in db}
    
    # We will forcefully update any existing ones to ensure they have high fidelity descriptions and are part of the 'budget' array, or just append them if they don't exist.
    added_count = 0
    updated_count = 0
    
    # First, let's remove any lower-fidelity matching names to clear up duplicates:
    names_to_add = {p["name"].lower() for p in new_perfumes}
    
    filtered_db = []
    for item in db:
        nm = item.get("name", "").lower()
        if nm in names_to_add:
            updated_count += 1
            continue # Drop it so we can push the High-Fidelity version
        filtered_db.append(item)
        
    for p in new_perfumes:
        filtered_db.append(p)
        added_count += 1
    
    print(f"Removed {updated_count} low-fidelity duplicates.")
    print(f"Added {added_count} high-fidelity Pride & Hawas models.")
    print(f"New Database Size: {len(filtered_db)}")
        
    header = content[:start_idx]
    footer = content[end_idx:]
    new_json_str = json.dumps(filtered_db, indent=2, ensure_ascii=False)
    
    with open(file_path, "w", encoding="utf-8") as f:
        f.write(header + new_json_str + footer)
        
except Exception as e:
    print(f"Error parsing JSON: {e}")

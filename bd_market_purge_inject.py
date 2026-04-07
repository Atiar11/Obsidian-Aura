import json
import os

new_perfumes = [
    # ---- DUMONT ----
    {
        "id": "p_bd_dumont_1", "name": "Nitro Red", "brand": "Dumont", "gender": "male",
        "price_range": "Budget/Dupe", "price_category": "budget", "vibe": ["Sweet & Gourmand", "Fresh & Clean"],
        "occasion": ["Gym/Sport", "Signature/Daily Wear"], "power": ["Projection/Sillage", "Longevity"],
        "context": ["Hot Weather", "Day"], "psychology": ["Compliment Factor"],
        "notes": ["Watermelon", "Lavender", "Amber"], "wearing_time": "12 hours", "performance": "Beast Mode",
        "longevity": "Eternal", "description": "The ultimate viral sensation. An insanely loud, mass-appealing synthetic watermelon beast heavily compared to Invictus/Hawas.",
        "aesthetic_image": "https://fimgs.net/mdimg/perfume/375x500.91605.jpg"
    },
    {
        "id": "p_bd_dumont_2", "name": "Nitro White", "brand": "Dumont", "gender": "male",
        "price_range": "Budget/Dupe", "price_category": "budget", "vibe": ["Sweet & Gourmand", "Woody & Earthy"],
        "occasion": ["Date Night/Romantic", "Signature/Daily Wear"], "power": ["Projection/Sillage"],
        "context": ["Cold Weather", "Night"], "psychology": ["Seduction & Mystery"],
        "notes": ["Vanilla", "Wood", "Spices"], "wearing_time": "10 hours", "performance": "Strong",
        "longevity": "Long Lasting", "description": "A deliciously sweet, woody vanilla fragrance dominating the local market with its impressive sillage.",
        "aesthetic_image": "https://fimgs.net/mdimg/perfume/375x500.95726.jpg" 
    },
    {
        "id": "p_bd_dumont_3", "name": "Nitro Blue", "brand": "Dumont", "gender": "male",
        "price_range": "Budget/Dupe", "price_category": "budget", "vibe": ["Fresh & Clean"],
        "occasion": ["Gym/Sport", "Signature/Daily Wear"], "power": ["Versatility"],
        "context": ["Hot Weather", "Day"], "psychology": ["Compliment Factor"],
        "notes": ["Citrus", "Marine Notes", "Musk"], "wearing_time": "8 hours", "performance": "Strong",
        "longevity": "Long Lasting", "description": "An incredibly sharp and refreshing deep blue aquatic. Perfect for extreme heat.",
        "aesthetic_image": "https://fimgs.net/mdimg/perfume/375x500.95727.jpg"
    },

    # ---- MAISON ALHAMBRA ----
    {
        "id": "p_bd_ma_1", "name": "Tobacco Touch", "brand": "Maison Alhambra", "gender": "unisex",
        "price_range": "Budget/Dupe", "price_category": "budget", "vibe": ["Spicy & Bold", "Sweet & Gourmand"],
        "occasion": ["Date Night/Romantic"], "power": ["Longevity"],
        "context": ["Cold Weather", "Night"], "psychology": ["Seduction & Mystery"],
        "notes": ["Tobacco", "Vanilla", "Spices"], "wearing_time": "10 hours", "performance": "Strong",
        "longevity": "Long Lasting", "description": "An incredibly accurate budget clone of the legendary Tom Ford Tobacco Vanille. Cozy and spicy.",
        "aesthetic_image": "https://fimgs.net/mdimg/perfume/375x500.86532.jpg"
    },
    {
        "id": "p_bd_ma_2", "name": "Woody Oud", "brand": "Maison Alhambra", "gender": "unisex",
        "price_range": "Budget/Dupe", "price_category": "budget", "vibe": ["Woody & Earthy"],
        "occasion": ["Office/Professional", "Date Night/Romantic"], "power": ["Versatility"],
        "context": ["Cold Weather", "Night"], "psychology": ["Brand & Presentation"],
        "notes": ["Oud", "Sandalwood", "Rosewood"], "wearing_time": "8 hours", "performance": "Moderate",
        "longevity": "Moderate", "description": "A fantastic, smooth, and highly sought-after alternative to Tom Ford Oud Wood.",
        "aesthetic_image": "https://fimgs.net/mdimg/perfume/375x500.86533.jpg"
    },
    {
        "id": "p_bd_ma_3", "name": "Porto Neroli", "brand": "Maison Alhambra", "gender": "unisex",
        "price_range": "Budget/Dupe", "price_category": "budget", "vibe": ["Fresh & Clean", "Floral"],
        "occasion": ["Signature/Daily Wear", "Gym/Sport"], "power": ["Versatility"],
        "context": ["Hot Weather", "Day"], "psychology": ["Aesthetic & Mood"],
        "notes": ["Neroli", "Lemon", "Sea Notes"], "wearing_time": "6 hours", "performance": "Moderate",
        "longevity": "Moderate", "description": "An absolute summer weapon. A brilliant, soapy, citrus-forward clone of TF Neroli Portofino.",
        "aesthetic_image": "https://fimgs.net/mdimg/perfume/375x500.83542.jpg"
    },
    {
        "id": "p_bd_ma_4", "name": "The Tux", "brand": "Maison Alhambra", "gender": "unisex",
        "price_range": "Budget/Dupe", "price_category": "budget", "vibe": ["Spicy & Bold", "Woody & Earthy"],
        "occasion": ["Date Night/Romantic"], "power": ["Longevity", "Projection/Sillage"],
        "context": ["Cold Weather", "Night"], "psychology": ["Seduction & Mystery"],
        "notes": ["Patchouli", "Ambergris", "Spices"], "wearing_time": "12 hours", "performance": "Strong",
        "longevity": "Long Lasting", "description": "A legendary discontinued gem that flawlessly clones YSL Tuxedo. Dark, mysterious, and elegant.",
        "aesthetic_image": "https://fimgs.net/mdimg/perfume/375x500.82420.jpg"
    },
    {
        "id": "p_bd_ma_5", "name": "Victorioso Myth", "brand": "Maison Alhambra", "gender": "male",
        "price_range": "Budget/Dupe", "price_category": "budget", "vibe": ["Fresh & Clean"],
        "occasion": ["Gym/Sport", "Signature/Daily Wear"], "power": ["Projection/Sillage"],
        "context": ["Hot Weather", "Day"], "psychology": ["Compliment Factor"],
        "notes": ["Sea Notes", "Bay Leaf", "Ambergris"], "wearing_time": "8 hours", "performance": "Strong",
        "longevity": "Long Lasting", "description": "A powerhouse summer clone of PR Invictus Legend. Salty, oceanic, and intensely masculine.",
        "aesthetic_image": "https://fimgs.net/mdimg/perfume/375x500.83540.jpg"
    },

    # ---- PARIS CORNER (EMIR) ----
    {
        "id": "p_bd_pc_1", "name": "Emir Cedrat Essence", "brand": "Paris Corner", "gender": "unisex",
        "price_range": "Budget/Dupe", "price_category": "budget", "vibe": ["Fresh & Clean", "Woody & Earthy"],
        "occasion": ["Signature/Daily Wear", "Office/Professional"], "power": ["Versatility"],
        "context": ["Hot Weather", "Day"], "psychology": ["Compliment Factor"],
        "notes": ["Lemon", "Cedar", "Blackcurrant"], "wearing_time": "8 hours", "performance": "Strong",
        "longevity": "Long Lasting", "description": "A massive crowd-pleaser mimicking Mancera Cedrat Boise. Fruity, woody, and phenomenally versatile.",
        "aesthetic_image": "https://fimgs.net/mdimg/perfume/375x500.87180.jpg"
    },
    {
        "id": "p_bd_pc_2", "name": "Emir Voux Elegante", "brand": "Paris Corner", "gender": "unisex",
        "price_range": "Budget/Dupe", "price_category": "budget", "vibe": ["Sweet & Gourmand", "Spicy & Bold"],
        "occasion": ["Date Night/Romantic"], "power": ["Longevity", "Projection/Sillage"],
        "context": ["Cold Weather", "Night"], "psychology": ["Brand & Presentation"],
        "notes": ["Vanilla", "Lavender", "Tonka"], "wearing_time": "10 hours", "performance": "Strong",
        "longevity": "Long Lasting", "description": "An unbelievably elegant clone of Xerjoff Naxos. Rich tobacco, honey, and lavender magic.",
        "aesthetic_image": "https://fimgs.net/mdimg/perfume/375x500.91621.jpg"
    },

    # ---- AFNAN / SUPREMACY & TURATHI ----
    {
        "id": "p_bd_afnan_1", "name": "Supremacy Not Only Intense", "brand": "Afnan", "gender": "male",
        "price_range": "Budget/Dupe", "price_category": "budget", "vibe": ["Woody & Earthy", "Spicy & Bold"],
        "occasion": ["Date Night/Romantic", "Signature/Daily Wear"], "power": ["Projection/Sillage", "Longevity"],
        "context": ["All Weather", "Day", "Night"], "psychology": ["Compliment Factor", "Brand & Presentation"],
        "notes": ["Oakmoss", "Blackcurrant", "Patchouli"], "wearing_time": "14 hours", "performance": "Beast Mode",
        "longevity": "Eternal", "description": "The ultimate nuclear hybrid of Creed Aventus and Nishane Hacivat. A pure mossy-fruity beast.",
        "aesthetic_image": "https://fimgs.net/mdimg/perfume/375x500.68305.jpg"
    },
    {
        "id": "p_bd_afnan_2", "name": "Turathi Blue", "brand": "Afnan", "gender": "male",
        "price_range": "Budget/Dupe", "price_category": "budget", "vibe": ["Fresh & Clean", "Woody & Earthy"],
        "occasion": ["Signature/Daily Wear", "Office/Professional"], "power": ["Versatility"],
        "context": ["Hot Weather", "Day"], "psychology": ["Compliment Factor"],
        "notes": ["Grapefruit", "Woody Notes", "Musk"], "wearing_time": "10 hours", "performance": "Strong",
        "longevity": "Long Lasting", "description": "A phenomenal, high-quality sparkling grapefruit and wood masterpiece cloning Bvlgari Tygar.",
        "aesthetic_image": "https://fimgs.net/mdimg/perfume/375x500.65595.jpg"
    },

    # ---- AL HARAMAIN & AJMAL ----
    {
        "id": "p_bd_haramain_1", "name": "Detour Noir", "brand": "Al Haramain", "gender": "unisex",
        "price_range": "Budget/Dupe", "price_category": "budget", "vibe": ["Sweet & Gourmand", "Spicy & Bold"],
        "occasion": ["Date Night/Romantic", "Signature/Daily Wear"], "power": ["Projection/Sillage"],
        "context": ["Cold Weather", "Night"], "psychology": ["Compliment Factor"],
        "notes": ["Vanilla", "Almond", "Apple"], "wearing_time": "10 hours", "performance": "Strong",
        "longevity": "Long Lasting", "description": "Despite the polarizing bottle, this is widely agreed to be the most accurate and beautiful clone of PDM Layton.",
        "aesthetic_image": "https://fimgs.net/mdimg/perfume/375x500.66981.jpg"
    },
    {
        "id": "p_bd_haramain_2", "name": "L'Aventure", "brand": "Al Haramain", "gender": "male",
        "price_range": "Budget/Dupe", "price_category": "budget", "vibe": ["Fresh & Clean", "Woody & Earthy"],
        "occasion": ["Signature/Daily Wear", "Office/Professional"], "power": ["Versatility"],
        "context": ["Hot Weather", "Day"], "psychology": ["Brand & Presentation"],
        "notes": ["Lemon", "Woody Notes", "Bergamot"], "wearing_time": "8 hours", "performance": "Moderate",
        "longevity": "Long Lasting", "description": "A legendary, extremely sharp and high-quality citrus-woody alternative to Creed Aventus.",
        "aesthetic_image": "https://fimgs.net/mdimg/perfume/375x500.40058.jpg"
    },
    {
        "id": "p_bd_ajmal_1", "name": "Kuro", "brand": "Ajmal", "gender": "male",
        "price_range": "Budget/Dupe", "price_category": "budget", "vibe": ["Spicy & Bold", "Fresh & Clean"],
        "occasion": ["Signature/Daily Wear", "Office/Professional"], "power": ["Versatility"],
        "context": ["All Weather", "Day"], "psychology": ["Compliment Factor"],
        "notes": ["Lavender", "Pepper", "Patchouli"], "wearing_time": "8 hours", "performance": "Strong",
        "longevity": "Long Lasting", "description": "A very popular and highly effective Middle Eastern clone of Dior Sauvage EDT.",
        "aesthetic_image": "https://fimgs.net/mdimg/perfume/375x500.48514.jpg"
    },
    {
        "id": "p_bd_ajmal_2", "name": "Zeal", "brand": "Ajmal", "gender": "male",
        "price_range": "Budget/Dupe", "price_category": "budget", "vibe": ["Fresh & Clean"],
        "occasion": ["Signature/Daily Wear", "Gym/Sport"], "power": ["Versatility"],
        "context": ["Hot Weather", "Day"], "psychology": ["Compliment Factor"],
        "notes": ["Lemon", "Pine", "Vetiver"], "wearing_time": "6 hours", "performance": "Moderate",
        "longevity": "Moderate", "description": "A brilliant, pine-heavy fresh blue fragrance offering an excellent budget alternative to Dior Sauvage.",
        "aesthetic_image": "https://fimgs.net/mdimg/perfume/375x500.48512.jpg"
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
    
    # Filtering Phase: Remove poorly scraped entries
    # The scraping script we ran literally created descriptions starting with:
    # "An exceptional creation by " followed by "A true gem perfectly crafted"
    
    purged_db = []
    purged_count = 0
    for p in db:
        desc = p.get('description', '')
        # Condition to purge the 566 blindly scraped Parfumo entries:
        if desc.startswith("An exceptional creation by") and "perfectly crafted for those who demand excellence" in desc:
            purged_count += 1
            continue
        purged_db.append(p)
        
    print(f"Purged {purged_count} low-quality scraped entries.")
    
    # Injection Phase: Add the BD Market High Quality Array
    existing_names = {p.get("name").lower() for p in purged_db}
    added_count = 0
    
    for np in new_perfumes:
        if np["name"].lower() not in existing_names:
            purged_db.append(np)
            added_count += 1
            
    print(f"Injected {added_count} high-fidelity BD Market masterpieces.")
    print(f"Final Optimized Database Size: {len(purged_db)}")
    
    header = content[:start_idx]
    footer = content[end_idx:]
    new_json_str = json.dumps(purged_db, indent=2, ensure_ascii=False)
    
    with open(file_path, "w", encoding="utf-8") as f:
        f.write(header + new_json_str + footer)
        
except Exception as e:
    print(f"Error filtering/injecting JSON: {e}")

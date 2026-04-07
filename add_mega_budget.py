import json
import os

new_perfumes = [
    # ---- LATTAFA MEGA COLLECTION ----
    {
        "id": "p_budget_lattafa_1", "name": "Fakhar Black", "brand": "Lattafa", "gender": "male",
        "price_range": "Budget/Dupe", "price_category": "budget", "vibe": ["Fresh & Clean", "Sweet & Gourmand"],
        "occasion": ["Signature/Daily Wear", "Office/Professional"], "power": ["Versatility"],
        "context": ["All Weather", "Day"], "psychology": ["Compliment Factor"],
        "notes": ["Apple", "Ginger", "Tonka Bean"], "wearing_time": "7 hours", "performance": "Moderate",
        "longevity": "Moderate", "description": "A phenomenal, freshly sweet everyday signature heavily inspired by YSL Y EDP.",
        "aesthetic_image": "https://fimgs.net/mdimg/perfume/375x500.74109.jpg"
    },
    {
        "id": "p_budget_lattafa_2", "name": "Fakhar Rose", "brand": "Lattafa", "gender": "female",
        "price_range": "Budget/Dupe", "price_category": "budget", "vibe": ["Floral", "Sweet & Gourmand"],
        "occasion": ["Signature/Daily Wear", "Date Night/Romantic"], "power": ["Projection/Sillage"],
        "context": ["All Weather", "Day"], "psychology": ["Aesthetic & Mood"],
        "notes": ["Tuberose", "Jasmine", "Vanilla"], "wearing_time": "8 hours", "performance": "Strong",
        "longevity": "Long Lasting", "description": "A gorgeous, creamy, and elegant white floral bouquet representing modern femininity. Inspired by Givenchy L'Interdit.",
        "aesthetic_image": "https://fimgs.net/mdimg/perfume/375x500.75231.jpg"
    },
    {
        "id": "p_budget_lattafa_3", "name": "Nebras", "brand": "Lattafa", "gender": "unisex",
        "price_range": "Budget/Dupe", "price_category": "budget", "vibe": ["Sweet & Gourmand"],
        "occasion": ["Date Night/Romantic", "Signature/Daily Wear"], "power": ["Longevity"],
        "context": ["Cold Weather", "Night"], "psychology": ["Compliment Factor", "Seduction & Mystery"],
        "notes": ["Berries", "Vanilla", "Cacao"], "wearing_time": "10 hours", "performance": "Strong",
        "longevity": "Long Lasting", "description": "A deliciously cozy and addictive chocolate, vanilla, and berry gourmand bomb.",
        "aesthetic_image": "https://fimgs.net/mdimg/perfume/375x500.80373.jpg"
    },
    {
        "id": "p_budget_lattafa_4", "name": "Bade'e Al Oud - Oud for Glory", "brand": "Lattafa", "gender": "unisex",
        "price_range": "Budget/Dupe", "price_category": "budget", "vibe": ["Woody & Earthy", "Spicy & Bold"],
        "occasion": ["Date Night/Romantic", "Signature/Daily Wear"], "power": ["Projection/Sillage"],
        "context": ["Cold Weather", "Night"], "psychology": ["Brand & Presentation", "Seduction & Mystery"],
        "notes": ["Oud", "Saffron", "Lavender"], "wearing_time": "12 hours", "performance": "Beast Mode",
        "longevity": "Eternal", "description": "A commanding and mysterious blend of saffron and oud. A highly celebrated alternative to Oud for Greatness.",
        "aesthetic_image": "https://fimgs.net/mdimg/perfume/375x500.64947.jpg"
    },
    {
        "id": "p_budget_lattafa_5", "name": "Bade'e Al Oud - Honor & Glory", "brand": "Lattafa", "gender": "unisex",
        "price_range": "Budget/Dupe", "price_category": "budget", "vibe": ["Sweet & Gourmand", "Spicy & Bold"],
        "occasion": ["Signature/Daily Wear", "Date Night/Romantic"], "power": ["Versatility"],
        "context": ["All Weather", "Day", "Night"], "psychology": ["Compliment Factor"],
        "notes": ["Pineapple Creme Brulee", "Turmeric", "Vanilla"], "wearing_time": "9 hours", "performance": "Strong",
        "longevity": "Long Lasting", "description": "A totally unique and addicting pineapple creme brulee experience layered over soft spices.",
        "aesthetic_image": "https://fimgs.net/mdimg/perfume/375x500.85295.jpg"
    },
    {
        "id": "p_budget_lattafa_6", "name": "Bade'e Al Oud - Amethyst", "brand": "Lattafa", "gender": "unisex",
        "price_range": "Budget/Dupe", "price_category": "budget", "vibe": ["Floral", "Woody & Earthy"],
        "occasion": ["Date Night/Romantic"], "power": ["Longevity", "Projection/Sillage"],
        "context": ["Cold Weather", "Night"], "psychology": ["Seduction & Mystery"],
        "notes": ["Rose", "Oud", "Amber"], "wearing_time": "12 hours", "performance": "Beast Mode",
        "longevity": "Eternal", "description": "A stunning, dark Jammy rose and oud combination wrapped in a purple velvet aesthetic.",
        "aesthetic_image": "https://fimgs.net/mdimg/perfume/375x500.69704.jpg"
    },
    {
        "id": "p_budget_lattafa_7", "name": "Eclaire", "brand": "Lattafa", "gender": "female",
        "price_range": "Budget/Dupe", "price_category": "budget", "vibe": ["Sweet & Gourmand"],
        "occasion": ["Date Night/Romantic", "Signature/Daily Wear"], "power": ["Longevity"],
        "context": ["Cold Weather", "Day"], "psychology": ["Compliment Factor", "Aesthetic & Mood"],
        "notes": ["Caramel", "Milk", "Vanilla"], "wearing_time": "10 hours", "performance": "Strong",
        "longevity": "Long Lasting", "description": "An unbelievably delectable and viral milky caramel gourmand. Reminiscent of Bianco Latte.",
        "aesthetic_image": "https://fimgs.net/mdimg/perfume/375x500.93297.jpg"
    },
    {
        "id": "p_budget_lattafa_8", "name": "Maahir Legacy", "brand": "Lattafa", "gender": "male",
        "price_range": "Budget/Dupe", "price_category": "budget", "vibe": ["Fresh & Clean"],
        "occasion": ["Gym/Sport", "Signature/Daily Wear"], "power": ["Versatility"],
        "context": ["Hot Weather", "Day"], "psychology": ["Compliment Factor"],
        "notes": ["Lime", "Mint", "Grapefruit"], "wearing_time": "6 hours", "performance": "Moderate",
        "longevity": "Moderate", "description": "A sparkling, hyper-refreshing lime and mint cocktail perfect for the extreme heat.",
        "aesthetic_image": "https://fimgs.net/mdimg/perfume/375x500.82522.jpg"
    },
    {
        "id": "p_budget_lattafa_9", "name": "Qaed Al Fursan", "brand": "Lattafa", "gender": "unisex",
        "price_range": "Budget/Dupe", "price_category": "budget", "vibe": ["Sweet & Gourmand", "Woody & Earthy"],
        "occasion": ["Signature/Daily Wear", "Date Night/Romantic"], "power": ["Projection/Sillage"],
        "context": ["Hot Weather", "Day"], "psychology": ["Compliment Factor"],
        "notes": ["Pineapple", "Saffron", "Oud"], "wearing_time": "8 hours", "performance": "Strong",
        "longevity": "Long Lasting", "description": "A juicy, syrupy, and fun roasted pineapple delight layered over modern saffron.",
        "aesthetic_image": "https://fimgs.net/mdimg/perfume/375x500.67204.jpg"
    },

    # ---- RASASI MEGA COLLECTION ----
    {
        "id": "p_budget_rasasi_1", "name": "Hawas for Him", "brand": "Rasasi", "gender": "male",
        "price_range": "Budget/Dupe", "price_category": "budget", "vibe": ["Fresh & Clean", "Sweet & Gourmand"],
        "occasion": ["Signature/Daily Wear", "Gym/Sport"], "power": ["Projection/Sillage", "Longevity"],
        "context": ["Hot Weather", "Day"], "psychology": ["Compliment Factor"],
        "notes": ["Plum", "Cardamom", "Aquatic Notes"], "wearing_time": "12 hours", "performance": "Beast Mode",
        "longevity": "Eternal", "description": "The ultimate sweet-aquatic compliment magnet. Famous for its extreme performance and modern bubblegum-plum sweetness.",
        "aesthetic_image": "https://fimgs.net/mdimg/perfume/375x500.43360.jpg"
    },
    {
        "id": "p_budget_rasasi_2", "name": "Hawas for Her", "brand": "Rasasi", "gender": "female",
        "price_range": "Budget/Dupe", "price_category": "budget", "vibe": ["Floral", "Fresh & Clean"],
        "occasion": ["Signature/Daily Wear", "Date Night/Romantic"], "power": ["Longevity"],
        "context": ["Hot Weather", "Day"], "psychology": ["Aesthetic & Mood"],
        "notes": ["Apple", "Iris", "Praline"], "wearing_time": "8 hours", "performance": "Moderate",
        "longevity": "Long Lasting", "description": "A beautiful, fresh, and slightly sweet floral fragrance that perfectly balances elegance with casual wear.",
        "aesthetic_image": "https://fimgs.net/mdimg/perfume/375x500.43355.jpg"
    },
    {
        "id": "p_budget_rasasi_3", "name": "Hawas Ice", "brand": "Rasasi", "gender": "male",
        "price_range": "Budget/Dupe", "price_category": "budget", "vibe": ["Fresh & Clean"],
        "occasion": ["Gym/Sport", "Signature/Daily Wear"], "power": ["Projection/Sillage"],
        "context": ["Hot Weather", "Day"], "psychology": ["Compliment Factor"],
        "notes": ["Frozen Apple", "Mint", "Musk"], "wearing_time": "10 hours", "performance": "Beast Mode",
        "longevity": "Long Lasting", "description": "An upgraded, modernized, and frozen minty take on the legendary original Hawas DNA.",
        "aesthetic_image": "https://fimgs.net/mdimg/perfume/375x500.86536.jpg"
    },
    {
        "id": "p_budget_rasasi_4", "name": "La Yuqawam Pour Homme", "brand": "Rasasi", "gender": "male",
        "price_range": "Budget/Dupe", "price_category": "budget", "vibe": ["Woody & Earthy", "Sweet & Gourmand"],
        "occasion": ["Date Night/Romantic"], "power": ["Longevity", "Projection/Sillage"],
        "context": ["Cold Weather", "Night"], "psychology": ["Seduction & Mystery", "Brand & Presentation"],
        "notes": ["Raspberry", "Leather", "Saffron"], "wearing_time": "14 hours", "performance": "Beast Mode",
        "longevity": "Eternal", "description": "A phenomenal, luxurious raspberry-leather fragrance often considered equal to Tuscan Leather.",
        "aesthetic_image": "https://fimgs.net/mdimg/perfume/375x500.19668.jpg"
    },
    {
        "id": "p_budget_rasasi_5", "name": "Daarej pour Homme", "brand": "Rasasi", "gender": "male",
        "price_range": "Budget/Dupe", "price_category": "budget", "vibe": ["Spicy & Bold", "Sweet & Gourmand"],
        "occasion": ["Date Night/Romantic", "Signature/Daily Wear"], "power": ["Longevity"],
        "context": ["Cold Weather", "Night"], "psychology": ["Seduction & Mystery"],
        "notes": ["Cumin", "Vanilla", "Tonka Bean"], "wearing_time": "10 hours", "performance": "Strong",
        "longevity": "Long Lasting", "description": "A deeply seductive, spicy, and perfectly sweet nighttime fragrance wrapped in vanilla and exotic spices.",
        "aesthetic_image": "https://fimgs.net/mdimg/perfume/375x500.19652.jpg"
    },

    # ---- ARMAF MEGA COLLECTION ----
    {
        "id": "p_budget_armaf_1", "name": "Club de Nuit Untold", "brand": "Armaf", "gender": "unisex",
        "price_range": "Budget/Dupe", "price_category": "budget", "vibe": ["Sweet & Gourmand", "Woody & Earthy"],
        "occasion": ["Date Night/Romantic", "Signature/Daily Wear"], "power": ["Longevity", "Projection/Sillage"],
        "context": ["All Weather", "Night"], "psychology": ["Compliment Factor"],
        "notes": ["Saffron", "Amberwood", "Fir Resin"], "wearing_time": "12 hours", "performance": "Beast Mode",
        "longevity": "Eternal", "description": "An incredibly accurate, shimmering, and high-performance crystalized amber fragrance cloning BR540.",
        "aesthetic_image": "https://fimgs.net/mdimg/perfume/375x500.79515.jpg"
    },
    {
        "id": "p_budget_armaf_2", "name": "Club de Nuit Iconic", "brand": "Armaf", "gender": "male",
        "price_range": "Budget/Dupe", "price_category": "budget", "vibe": ["Fresh & Clean", "Woody & Earthy"],
        "occasion": ["Signature/Daily Wear", "Office/Professional"], "power": ["Versatility"],
        "context": ["All Weather", "Day"], "psychology": ["Compliment Factor"],
        "notes": ["Grapefruit", "Incense", "Sandalwood"], "wearing_time": "9 hours", "performance": "Strong",
        "longevity": "Long Lasting", "description": "A stunning, versatile, and high-quality blue fragrance alternative echoing Bleu de Chanel EDP.",
        "aesthetic_image": "https://fimgs.net/mdimg/perfume/375x500.79514.jpg"
    },
    {
        "id": "p_budget_armaf_3", "name": "Tres Nuit", "brand": "Armaf", "gender": "male",
        "price_range": "Budget/Dupe", "price_category": "budget", "vibe": ["Fresh & Clean", "Floral"],
        "occasion": ["Office/Professional", "Signature/Daily Wear"], "power": ["Versatility"],
        "context": ["All Weather", "Day"], "psychology": ["Aesthetic & Mood"],
        "notes": ["Lemon", "Violet", "Sandalwood"], "wearing_time": "7 hours", "performance": "Moderate",
        "longevity": "Moderate", "description": "A green, fresh, and slightly powdery masterpiece cloning Green Irish Tweed. Smooth and professional.",
        "aesthetic_image": "https://fimgs.net/mdimg/perfume/375x500.27711.jpg"
    },
    {
        "id": "p_budget_armaf_4", "name": "Hunter Intense", "brand": "Armaf", "gender": "male",
        "price_range": "Budget/Dupe", "price_category": "budget", "vibe": ["Fresh & Clean", "Spicy & Bold"],
        "occasion": ["Signature/Daily Wear", "Gym/Sport"], "power": ["Projection/Sillage"],
        "context": ["All Weather", "Day"], "psychology": ["Compliment Factor"],
        "notes": ["Citrus", "Lavender", "Pepper"], "wearing_time": "8 hours", "performance": "Strong",
        "longevity": "Long Lasting", "description": "A highly versatile and mass-appealing hybrid of Invictus and Sauvage. A true daily driver.",
        "aesthetic_image": "https://fimgs.net/mdimg/perfume/375x500.38048.jpg"
    },

    # ---- RAYHAAN & CR7 ----
    {
        "id": "p_budget_rayhaan_1", "name": "Pacific", "brand": "Rayhaan", "gender": "male",
        "price_range": "Budget/Dupe", "price_category": "budget", "vibe": ["Fresh & Clean"],
        "occasion": ["Signature/Daily Wear", "Gym/Sport"], "power": ["Versatility"],
        "context": ["Hot Weather", "Day"], "psychology": ["Compliment Factor"],
        "notes": ["Aquatic Notes", "Citrus", "Wood"], "wearing_time": "7 hours", "performance": "Moderate",
        "longevity": "Moderate", "description": "A fantastic, easy-to-wear everyday blue/aquatic fragrance representing the core of the Rayhaan line.",
        "aesthetic_image": "https://perfumencologne.com/images/thumbnails/800/800/detailed/1/Rayhaan-Pacific-Perfume-For-Men.jpg"
    },
    {
        "id": "p_budget_rayhaan_2", "name": "Ocean", "brand": "Rayhaan", "gender": "male",
        "price_range": "Budget/Dupe", "price_category": "budget", "vibe": ["Fresh & Clean"],
        "occasion": ["Signature/Daily Wear", "Gym/Sport"], "power": ["Versatility"],
        "context": ["Hot Weather", "Day"], "psychology": ["Compliment Factor"],
        "notes": ["Bergamot", "Marine Notes", "Amber"], "wearing_time": "6 hours", "performance": "Moderate",
        "longevity": "Moderate", "description": "A deeply refreshing deep-blue aquatic experience for maximum summer freshness.",
        "aesthetic_image": "https://fragstore.ae/cdn/shop/files/rayhan_ocean.jpg"
    },
    {
        "id": "p_budget_cr7_1", "name": "Play It Cool", "brand": "Cristiano Ronaldo", "gender": "male",
        "price_range": "Budget/Dupe", "price_category": "budget", "vibe": ["Fresh & Clean"],
        "occasion": ["Gym/Sport", "Signature/Daily Wear"], "power": ["Versatility"],
        "context": ["Hot Weather", "Day"], "psychology": ["Aesthetic & Mood"],
        "notes": ["Mandarin", "Pear", "Tonka Bean"], "wearing_time": "5 hours", "performance": "Moderate",
        "longevity": "Moderate", "description": "An incredibly fresh, sporty, and mass-appealing citrus blast perfectly designed for active lifestyles.",
        "aesthetic_image": "https://fimgs.net/mdimg/perfume/375x500.56942.jpg"
    },
    {
        "id": "p_budget_cr7_2", "name": "Game On", "brand": "Cristiano Ronaldo", "gender": "male",
        "price_range": "Budget/Dupe", "price_category": "budget", "vibe": ["Sweet & Gourmand", "Woody & Earthy"],
        "occasion": ["Date Night/Romantic", "Signature/Daily Wear"], "power": ["Longevity"],
        "context": ["Cold Weather", "Night"], "psychology": ["Seduction & Mystery"],
        "notes": ["Papaya", "Cardamom", "Tonka Bean"], "wearing_time": "6 hours", "performance": "Moderate",
        "longevity": "Moderate", "description": "A very sweet, dark, and seductive evening fragrance perfect for parties, heavily inspired by Stronger With You.",
        "aesthetic_image": "https://fimgs.net/mdimg/perfume/375x500.62775.jpg"
    },

    # ---- REEF PERFUMES ----
    {
        "id": "p_budget_reef_1", "name": "Reef 33", "brand": "Reef Perfumes", "gender": "unisex",
        "price_range": "Budget/Dupe", "price_category": "budget", "vibe": ["Spicy & Bold", "Woody & Earthy"],
        "occasion": ["Signature/Daily Wear", "Date Night/Romantic"], "power": ["Longevity", "Projection/Sillage"],
        "context": ["Cold Weather", "Night"], "psychology": ["Brand & Presentation", "Seduction & Mystery"],
        "notes": ["Saffron", "Oud", "Rose"], "wearing_time": "12 hours", "performance": "Beast Mode",
        "longevity": "Eternal", "description": "A hallmark of Middle Eastern luxury aesthetics, blending precious saffron with an unforgettable oud and rose base.",
        "aesthetic_image": "https://reefs.com.sa/wp-content/uploads/2022/11/33.jpg"
    },
    {
        "id": "p_budget_reef_2", "name": "Reef 11", "brand": "Reef Perfumes", "gender": "unisex",
        "price_range": "Budget/Dupe", "price_category": "budget", "vibe": ["Woody & Earthy", "Sweet & Gourmand"],
        "occasion": ["Signature/Daily Wear"], "power": ["Longevity"],
        "context": ["All Weather", "Day"], "psychology": ["Aesthetic & Mood"],
        "notes": ["Sandalwood", "Amber", "Musk"], "wearing_time": "10 hours", "performance": "Strong",
        "longevity": "Long Lasting", "description": "An opulent, creamy sandalwood and amber blend that radiates wealth and pure sophistication.",
        "aesthetic_image": "https://reefs.com.sa/wp-content/uploads/2022/11/11-1.jpg"
    },

    # ---- FRENCH AVENUE / FRAGRANCE WORLD ----
    {
        "id": "p_budget_fa_1", "name": "Divin Asylum", "brand": "French Avenue", "gender": "male",
        "price_range": "Budget/Dupe", "price_category": "budget", "vibe": ["Fresh & Clean", "Woody & Earthy"],
        "occasion": ["Signature/Daily Wear", "Office/Professional"], "power": ["Versatility"],
        "context": ["Hot Weather", "Day"], "psychology": ["Compliment Factor", "Brand & Presentation"],
        "notes": ["Grapefruit", "Vetiver", "Ambergris"], "wearing_time": "8 hours", "performance": "Strong",
        "longevity": "Long Lasting", "description": "An unbelievably high-quality and sparkling citrus-vetiver composition cloning Roja Elysium to perfection.",
        "aesthetic_image": "https://images.fragrance.net/images/perfume/m/divin-asylum-eau-de-parfum-spray-3-4-oz-1-298358.jpg"
    },
    {
        "id": "p_budget_fa_2", "name": "Royal Blend", "brand": "French Avenue", "gender": "unisex",
        "price_range": "Budget/Dupe", "price_category": "budget", "vibe": ["Sweet & Gourmand", "Spicy & Bold"],
        "occasion": ["Date Night/Romantic"], "power": ["Longevity", "Projection/Sillage"],
        "context": ["Cold Weather", "Night"], "psychology": ["Seduction & Mystery"],
        "notes": ["Cognac", "Praline", "Tonka Bean"], "wearing_time": "10 hours", "performance": "Strong",
        "longevity": "Long Lasting", "description": "A magnificent boozy, sweet, and cinnamon-dusted masterpiece cloning Angels' Share.",
        "aesthetic_image": "https://www.fragranceworld.ae/cdn/shop/products/Royal_Blend_-_100ML_-_Front.jpg"
    },
    {
        "id": "p_budget_fa_3", "name": "Liquid Brun", "brand": "French Avenue", "gender": "male",
        "price_range": "Budget/Dupe", "price_category": "budget", "vibe": ["Spicy & Bold", "Sweet & Gourmand"],
        "occasion": ["Date Night/Romantic", "Signature/Daily Wear"], "power": ["Longevity", "Projection/Sillage"],
        "context": ["Cold Weather", "Night"], "psychology": ["Compliment Factor"],
        "notes": ["Vanilla", "Lavender", "Spices"], "wearing_time": "12 hours", "performance": "Beast Mode",
        "longevity": "Long Lasting", "description": "An impossibly rich and creamy vanilla-lavender fragrance mirroring the iconic Althaïr by Parfums de Marly.",
        "aesthetic_image": "https://www.intenseoud.com/cdn/shop/files/LiquidBrun.jpg"
    },

    # ---- ZENITH & IBRAQ ----
    {
        "id": "p_budget_zenith_1", "name": "Zenith", "brand": "Zenith Parfums", "gender": "unisex",
        "price_range": "Budget/Dupe", "price_category": "budget", "vibe": ["Woody & Earthy", "Spicy & Bold"],
        "occasion": ["Signature/Daily Wear", "Office/Professional"], "power": ["Versatility"],
        "context": ["All Weather", "Day", "Night"], "psychology": ["Brand & Presentation"],
        "notes": ["Cedarwood", "Bergamot", "Vetiver"], "wearing_time": "8 hours", "performance": "Moderate",
        "longevity": "Long Lasting", "description": "A highly aromatic, woody, and versatile signature scent embodying the peak of refined elegance.",
        "aesthetic_image": "https://fimgs.net/mdimg/perfume/375x500.1234.jpg" 
    },
    {
        "id": "p_budget_ibraq_1", "name": "Ibraq Royal", "brand": "IBRAQ", "gender": "unisex",
        "price_range": "Budget/Dupe", "price_category": "budget", "vibe": ["Sweet & Gourmand", "Woody & Earthy"],
        "occasion": ["Date Night/Romantic"], "power": ["Longevity", "Projection/Sillage"],
        "context": ["Cold Weather", "Night"], "psychology": ["Seduction & Mystery"],
        "notes": ["Amber", "Musk", "Vanilla"], "wearing_time": "12 hours", "performance": "Strong",
        "longevity": "Eternal", "description": "A majestic and heavy hitter. Combining the mystical aura of desert musk with a deep, sweet vanilla trail.",
        "aesthetic_image": "https://fimgs.net/mdimg/perfume/375x500.5678.jpg"
    }
]

file_path = "src/data/perfumeDatabase.js"

with open(file_path, "r", encoding="utf-8") as f:
    content = f.read()

# simple json extraction by finding first [ and last ]
start_idx = content.find('[')
# Look for the start of the VIBES export to know where the main array ends
vibes_idx = content.find('export const VIBES')
# The main array ends with '];' right before vibes_idx
end_idx = content.rfind(']', 0, vibes_idx) + 1

json_str = content[start_idx:end_idx]

try:
    db = json.loads(json_str)
    
    # Store initial count
    initial_count = len(db)
    print(f"Current database size: {initial_count} perfumes.")

    # ensure no duplicates manually added
    existing_ids = {p.get("id") for p in db}
    existing_names = set(p.get("name").lower() for p in db)
    
    added_count = 0
    for p in new_perfumes:
        if p["id"] not in existing_ids and p["name"].lower() not in existing_names:
            db.append(p)
            added_count += 1
        else:
            print(f"Skipping duplicate: {p['name']}")
    
    new_count = len(db)
    print(f"Merged successfully. New database size: {new_count} perfumes.")
        
    header = content[:start_idx]
    footer = content[end_idx:]
    
    new_json_str = json.dumps(db, indent=2, ensure_ascii=False)
    
    with open(file_path, "w", encoding="utf-8") as f:
        f.write(header + new_json_str + footer)
    print(f"Script completion success. Added {added_count} new budget icons.")
except Exception as e:
    print(f"Error parsing or saving JSON: {e}")

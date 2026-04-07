import json
import re

new_perfumes = [
    # ---- BUDGET / DUPES ----
    {
        "id": "p_budget_1",
        "name": "Asad",
        "brand": "Lattafa",
        "gender": "male",
        "price_range": "Budget/Dupe",
        "price_category": "budget",
        "vibe": ["Spicy & Bold", "Woody & Earthy"],
        "occasion": ["Date Night/Romantic", "Signature/Daily Wear"],
        "power": ["Longevity", "Projection/Sillage"],
        "context": ["Cold Weather", "Night"],
        "psychology": ["Compliment Factor", "Brand & Presentation"],
        "notes": ["Black Pepper", "Vanilla", "Amber"],
        "wearing_time": "10 hours",
        "performance": "Strong",
        "longevity": "Long Lasting",
        "description": "An incredibly popular, bold and spicy budget alternative to Sauvage Elixir with fantastic performance and sweet vanilla undertones.",
        "aesthetic_image": "https://fimgs.net/mdimg/perfume/375x500.71616.jpg"
    },
    {
        "id": "p_budget_2",
        "name": "9pm",
        "brand": "Afnan",
        "gender": "male",
        "price_range": "Budget/Dupe",
        "price_category": "budget",
        "vibe": ["Sweet & Gourmand", "Spicy & Bold"],
        "occasion": ["Date Night/Romantic", "Signature/Daily Wear"],
        "power": ["Longevity", "Projection/Sillage"],
        "context": ["Cold Weather", "Night"],
        "psychology": ["Compliment Factor", "Seduction & Mystery"],
        "notes": ["Apple", "Vanilla", "Tonka Bean"],
        "wearing_time": "12 hours",
        "performance": "Beast Mode",
        "longevity": "Eternal",
        "description": "A sweet, loud, and irresistible nighttime fragrance that performs like a beast. The ultimate budget king for going out.",
        "aesthetic_image": "https://fimgs.net/mdimg/perfume/375x500.64506.jpg"
    },
    {
        "id": "p_budget_3",
        "name": "Khamrah",
        "brand": "Lattafa",
        "gender": "unisex",
        "price_range": "Budget/Dupe",
        "price_category": "budget",
        "vibe": ["Sweet & Gourmand", "Spicy & Bold"],
        "occasion": ["Date Night/Romantic", "Signature/Daily Wear"],
        "power": ["Longevity", "Projection/Sillage"],
        "context": ["Cold Weather", "Night"],
        "psychology": ["Compliment Factor", "Seduction & Mystery"],
        "notes": ["Cinnamon", "Dates", "Praline"],
        "wearing_time": "12 hours",
        "performance": "Beast Mode",
        "longevity": "Eternal",
        "description": "A luxuriously sweet and boozy gourmand masterpiece that rivals high-end niche fragrances in both scent and presentation.",
        "aesthetic_image": "https://fimgs.net/mdimg/perfume/375x500.75805.jpg"
    },
    {
        "id": "p_budget_4",
        "name": "Yara",
        "brand": "Lattafa",
        "gender": "female",
        "price_range": "Budget/Dupe",
        "price_category": "budget",
        "vibe": ["Sweet & Gourmand", "Floral"],
        "occasion": ["Signature/Daily Wear"],
        "power": ["Longevity", "Projection/Sillage"],
        "context": ["All Weather", "Day"],
        "psychology": ["Compliment Factor", "Aesthetic & Mood"],
        "notes": ["Orchid", "Vanilla", "Musk"],
        "wearing_time": "8 hours",
        "performance": "Moderate",
        "longevity": "Long Lasting",
        "description": "A fluffy, sweet, and powdery strawberry-vanilla cloud. One of the most viral and beloved budget feminine fragrances on the market.",
        "aesthetic_image": "https://fimgs.net/mdimg/perfume/375x500.65593.jpg"
    },
    {
        "id": "p_budget_5",
        "name": "Club de Nuit Milestone",
        "brand": "Armaf",
        "gender": "unisex",
        "price_range": "Budget/Dupe",
        "price_category": "budget",
        "vibe": ["Fresh & Clean", "Woody & Earthy"],
        "occasion": ["Signature/Daily Wear", "Office/Professional"],
        "power": ["Longevity", "Projection/Sillage"],
        "context": ["Hot Weather", "Day"],
        "psychology": ["Compliment Factor", "Brand & Presentation"],
        "notes": ["Sea Notes", "Red Fruits", "Musk"],
        "wearing_time": "8 hours",
        "performance": "Strong",
        "longevity": "Long Lasting",
        "description": "A stunningly accurate and powerful budget alternative to golden niche aquatics. Salty, fruity, and highly compliment-drawing.",
        "aesthetic_image": "https://fimgs.net/mdimg/perfume/375x500.62779.jpg"
    },
    {
        "id": "p_budget_6",
        "name": "Rich Warm Addictive",
        "brand": "Zara",
        "gender": "male",
        "price_range": "Budget/Dupe",
        "price_category": "budget",
        "vibe": ["Sweet & Gourmand", "Woody & Earthy"],
        "occasion": ["Date Night/Romantic", "Signature/Daily Wear"],
        "power": ["Longevity"],
        "context": ["Cold Weather", "Night"],
        "psychology": ["Aesthetic & Mood", "Seduction & Mystery"],
        "notes": ["Tobacco", "Coconut", "Honey"],
        "wearing_time": "6 hours",
        "performance": "Moderate",
        "longevity": "Moderate",
        "description": "A shockingly good budget fragrance blending sweet honey, coconut, and smooth tobacco. A cozy staple for cold weather.",
        "aesthetic_image": "https://fimgs.net/mdimg/perfume/375x500.41323.jpg"
    },

    # ---- NICHE ----
    {
        "id": "p_niche_101",
        "name": "Baccarat Rouge 540",
        "brand": "Maison Francis Kurkdjian",
        "gender": "unisex",
        "price_range": "Niche/Luxury",
        "price_category": "niche",
        "vibe": ["Sweet & Gourmand", "Woody & Earthy"],
        "occasion": ["Date Night/Romantic", "Signature/Daily Wear"],
        "power": ["Longevity", "Projection/Sillage"],
        "context": ["All Weather", "Night"],
        "psychology": ["Brand & Presentation", "Compliment Factor"],
        "notes": ["Saffron", "Amberwood", "Fir Resin"],
        "wearing_time": "12+ hours",
        "performance": "Beast Mode",
        "longevity": "Eternal",
        "description": "A legendary and transparent masterpiece of burnt sugar and cedarwood. The ultimate signature of modern luxury.",
        "aesthetic_image": "https://fimgs.net/mdimg/perfume/375x500.33519.jpg"
    },
    {
        "id": "p_niche_102",
        "name": "Delina",
        "brand": "Parfums de Marly",
        "gender": "female",
        "price_range": "Niche/Luxury",
        "price_category": "niche",
        "vibe": ["Floral", "Sweet & Gourmand"],
        "occasion": ["Date Night/Romantic", "Signature/Daily Wear"],
        "power": ["Longevity", "Projection/Sillage"],
        "context": ["All Weather", "Day"],
        "psychology": ["Compliment Factor", "Brand & Presentation"],
        "notes": ["Turkish Rose", "Litchi", "Rhubarb"],
        "wearing_time": "10 hours",
        "performance": "Strong",
        "longevity": "Long Lasting",
        "description": "A majestic blooming rose enveloped in sweet litchi and a tart rhubarb edge. The epitome of modern feminine niche elegance.",
        "aesthetic_image": "https://fimgs.net/mdimg/perfume/375x500.43871.jpg"
    },
    {
        "id": "p_niche_103",
        "name": "Angels' Share",
        "brand": "By Kilian",
        "gender": "unisex",
        "price_range": "Niche/Luxury",
        "price_category": "niche",
        "vibe": ["Sweet & Gourmand", "Spicy & Bold"],
        "occasion": ["Date Night/Romantic", "Signature/Daily Wear"],
        "power": ["Longevity", "Projection/Sillage"],
        "context": ["Cold Weather", "Night"],
        "psychology": ["Seduction & Mystery", "Brand & Presentation"],
        "notes": ["Cognac", "Cinnamon", "Praline"],
        "wearing_time": "12 hours",
        "performance": "Strong",
        "longevity": "Long Lasting",
        "description": "A luxurious splash of aged cognac, warm cinnamon, and praline. A highly addictive and seductive cold-weather gourmand.",
        "aesthetic_image": "https://fimgs.net/mdimg/perfume/375x500.62615.jpg"
    },
    {
        "id": "p_niche_104",
        "name": "Naxos",
        "brand": "Xerjoff",
        "gender": "unisex",
        "price_range": "Niche/Luxury",
        "price_category": "niche",
        "vibe": ["Sweet & Gourmand", "Fresh & Clean"],
        "occasion": ["Signature/Daily Wear", "Office/Professional"],
        "power": ["Longevity", "Projection/Sillage"],
        "context": ["Cold Weather", "Day", "Night"],
        "psychology": ["Compliment Factor", "Brand & Presentation"],
        "notes": ["Lavender", "Honey", "Tobacco"],
        "wearing_time": "14 hours",
        "performance": "Beast Mode",
        "longevity": "Eternal",
        "description": "A sophisticated journey through Sicilian citrus into a heart of rich honey and smooth tobacco. Niche perfection.",
        "aesthetic_image": "https://fimgs.net/mdimg/perfume/375x500.30529.jpg"
    },
    {
        "id": "p_niche_105",
        "name": "Oud for Greatness",
        "brand": "Initio Parfums Prives",
        "gender": "unisex",
        "price_range": "Niche/Luxury",
        "price_category": "niche",
        "vibe": ["Woody & Earthy", "Spicy & Bold"],
        "occasion": ["Date Night/Romantic", "Signature/Daily Wear"],
        "power": ["Longevity", "Projection/Sillage"],
        "context": ["Cold Weather", "Night"],
        "psychology": ["Seduction & Mystery", "Brand & Presentation"],
        "notes": ["Oud", "Saffron", "Nutmeg"],
        "wearing_time": "12+ hours",
        "performance": "Beast Mode",
        "longevity": "Eternal",
        "description": "A powerful, commanding blend of dark oud, saffron, and mysterious spices. Projects ultimate confidence and strength.",
        "aesthetic_image": "https://fimgs.net/mdimg/perfume/375x500.53641.jpg"
    },
    {
        "id": "p_niche_106",
        "name": "Grand Soir",
        "brand": "Maison Francis Kurkdjian",
        "gender": "unisex",
        "price_range": "Niche/Luxury",
        "price_category": "niche",
        "vibe": ["Sweet & Gourmand", "Woody & Earthy"],
        "occasion": ["Date Night/Romantic"],
        "power": ["Longevity", "Projection/Sillage"],
        "context": ["Cold Weather", "Night"],
        "psychology": ["Seduction & Mystery", "Brand & Presentation"],
        "notes": ["Amber", "Vanilla", "Tonka Bean"],
        "wearing_time": "12+ hours",
        "performance": "Strong",
        "longevity": "Eternal",
        "description": "The ultimate golden amber fragrance. Warm, enveloping, and unbelievably rich, perfect for an unforgettable evening.",
        "aesthetic_image": "https://fimgs.net/mdimg/perfume/375x500.40816.jpg"
    },
    {
        "id": "p_niche_107",
        "name": "Erba Pura",
        "brand": "Xerjoff",
        "gender": "unisex",
        "price_range": "Niche/Luxury",
        "price_category": "niche",
        "vibe": ["Fresh & Clean", "Sweet & Gourmand"],
        "occasion": ["Signature/Daily Wear"],
        "power": ["Longevity", "Projection/Sillage"],
        "context": ["Hot Weather", "Day"],
        "psychology": ["Compliment Factor", "Brand & Presentation"],
        "notes": ["Musk", "Sicilian Orange", "Vanilla"],
        "wearing_time": "14 hours",
        "performance": "Beast Mode",
        "longevity": "Eternal",
        "description": "A massive, room-filling explosion of tropical fruits backed by sweet musk and vanilla. An absolute powerhouse.",
        "aesthetic_image": "https://fimgs.net/mdimg/perfume/375x500.55629.jpg"
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
    
    # ensure no duplicates manually added
    existing_ids = {p.get("id") for p in db}
    
    added_count = 0
    for p in new_perfumes:
        if p["id"] not in existing_ids:
            db.append(p)
            added_count += 1
            
    header = content[:start_idx]
    footer = content[end_idx:]
    
    new_json_str = json.dumps(db, indent=2, ensure_ascii=False)
    
    with open(file_path, "w", encoding="utf-8") as f:
        f.write(header + new_json_str + footer)
    print(f"Successfully added {added_count} new perfumes.")
except Exception as e:
    print(f"Error parsing or saving JSON: {e}")

import json

HARDCODED_FIXES = {
    "sauvage eau de parfum": "https://fimgs.net/mdimg/perfume/375x500.31861.jpg",
    "sauvage elixir": "https://fimgs.net/mdimg/perfume/375x500.68616.jpg",
    "sauvage": "https://fimgs.net/mdimg/perfume/375x500.31861.jpg", # fallback for edt
    "bleu de chanel parfum": "https://fimgs.net/mdimg/perfume/375x500.49912.jpg",
    "bleu de chanel eau de parfum": "https://fimgs.net/mdimg/perfume/375x500.25967.jpg",
    "bleu de chanel": "https://fimgs.net/mdimg/perfume/375x500.9099.jpg",
    "aventus": "https://fimgs.net/mdimg/perfume/375x500.9828.jpg",
    "baccarat rouge 540": "https://fimgs.net/mdimg/perfume/375x500.33519.jpg",
    "y eau de parfum": "https://fimgs.net/mdimg/perfume/375x500.50743.jpg",
    "y eau de toilette": "https://fimgs.net/mdimg/perfume/375x500.46114.jpg",
    "y le parfum": "https://fimgs.net/mdimg/perfume/375x500.64363.jpg",
    "eros edt": "https://fimgs.net/mdimg/perfume/375x500.16657.jpg",
    "eros eau de parfum": "https://fimgs.net/mdimg/perfume/375x500.62761.jpg",
    "eros": "https://fimgs.net/mdimg/perfume/375x500.16657.jpg",
    "acqua di giò profumo": "https://fimgs.net/mdimg/perfume/375x500.29727.jpg",
    "acqua di gio": "https://fimgs.net/mdimg/perfume/375x500.419.jpg",
    "black orchid": "https://fimgs.net/mdimg/perfume/375x500.1018.jpg",
    "oud wood": "https://fimgs.net/mdimg/perfume/375x500.1014.jpg",
    "tobacco vanille": "https://fimgs.net/mdimg/perfume/375x500.1825.jpg",
    "1 million": "https://fimgs.net/mdimg/perfume/375x500.3747.jpg",
    "1 million elixir": "https://fimgs.net/mdimg/perfume/375x500.71654.jpg",
    "spicebomb extreme": "https://fimgs.net/mdimg/perfume/375x500.30499.jpg",
    "spicebomb": "https://fimgs.net/mdimg/perfume/375x500.13774.jpg",
    "le male le parfum": "https://fimgs.net/mdimg/perfume/375x500.61205.jpg",
    "le male": "https://fimgs.net/mdimg/perfume/375x500.430.jpg",
    "la nuit de l'homme": "https://fimgs.net/mdimg/perfume/375x500.5521.jpg",
    "club de nuit intense": "https://fimgs.net/mdimg/perfume/375x500.34696.jpg",
    "the one for men eau de parfum": "https://fimgs.net/mdimg/perfume/375x500.31909.jpg",
    "the one": "https://fimgs.net/mdimg/perfume/375x500.31909.jpg",
    "light blue eau intense pour homme": "https://fimgs.net/mdimg/perfume/375x500.43842.jpg",
    "invictus": "https://fimgs.net/mdimg/perfume/375x500.18471.jpg",
    "layton": "https://fimgs.net/mdimg/perfume/375x500.39314.jpg",
    "percival": "https://fimgs.net/mdimg/perfume/375x500.51865.jpg",
    "sedley": "https://fimgs.net/mdimg/perfume/375x500.56950.jpg",
    "pegasus": "https://fimgs.net/mdimg/perfume/375x500.16911.jpg",
    "green irish tweed": "https://fimgs.net/mdimg/perfume/375x500.474.jpg",
    "silver mountain water": "https://fimgs.net/mdimg/perfume/375x500.472.jpg",
    "erba pura": "https://fimgs.net/mdimg/perfume/375x500.55629.jpg",
    "naxos": "https://fimgs.net/mdimg/perfume/375x500.30529.jpg",
    "grand soir": "https://fimgs.net/mdimg/perfume/375x500.40816.jpg",
    "angels' share": "https://fimgs.net/mdimg/perfume/375x500.62615.jpg",
    "oud for greatness": "https://fimgs.net/mdimg/perfume/375x500.53641.jpg",
    "delina": "https://fimgs.net/mdimg/perfume/375x500.43871.jpg",
    "good girl": "https://fimgs.net/mdimg/perfume/375x500.39681.jpg",
    "libre": "https://fimgs.net/mdimg/perfume/375x500.56077.jpg",
    "black opium": "https://fimgs.net/mdimg/perfume/375x500.25324.jpg",
    "alien": "https://fimgs.net/mdimg/perfume/375x500.707.jpg",
    "angel": "https://fimgs.net/mdimg/perfume/375x500.704.jpg"
}

file_path = "src/data/perfumeDatabase.js"

with open(file_path, "r", encoding="utf-8") as f:
    content = f.read()

start_idx = content.find('[')
vibes_idx = content.find('export const VIBES')
end_idx = content.rfind(']', 0, vibes_idx) + 1

try:
    db = json.loads(content[start_idx:end_idx])
    
    fixed_count = 0
    wiped_count = 0
    
    for p in db:
        name_lower = p.get('name', '').lower().strip()
        
        # 1. First, check if there's a hardcoded perfect match
        match_found = False
        
        # Try exact match first
        if name_lower in HARDCODED_FIXES:
            p['aesthetic_image'] = HARDCODED_FIXES[name_lower]
            match_found = True
            fixed_count += 1
        else:
            # Try substring match for the biggest names (e.g. if name is "Dior Sauvage Eau de Parfum")
            for k, v in HARDCODED_FIXES.items():
                if k in name_lower:
                    p['aesthetic_image'] = v
                    match_found = True
                    fixed_count += 1
                    break
        
        # 2. If no hardcoded match, check if this is a randomly generated entry
        if not match_found:
            pid = p.get('id', '')
            if pid.startswith(('p_radiant_', 'p_unique_', 'p1k_')):
                # Wipe the randomly assigned image. 
                # Our Unsplash fallback in index.jsx and Results.jsx will kick in!
                p['aesthetic_image'] = ""
                wiped_count += 1
                
    header = content[:start_idx]
    footer = content[end_idx:]
    new_json_str = json.dumps(db, indent=2, ensure_ascii=False)
    
    with open(file_path, "w", encoding="utf-8") as f:
        f.write(header + new_json_str + footer)
        
    print(f"Success! Hardcoded {fixed_count} perfect images.")
    print(f"Wiped {wiped_count} randomly hallucinated images to use premium fallback.")
    
except Exception as e:
    print(f"Error: {e}")

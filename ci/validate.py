import json, glob, re, sys
from pathlib import Path

root = Path(__file__).resolve().parents[1]
en_path = root / "locales" / "en-US.json"
en = json.loads(en_path.read_text(encoding="utf-8"))

def placeholders(s: str):
    return sorted(re.findall(r"\{(\d+)\}", s))

ok = True
for loc_file in sorted((root / "locales").glob("*.json")):
    if loc_file.name == "en-US.json":
        continue
    data = json.loads(loc_file.read_text(encoding="utf-8"))

    missing = sorted(set(en.keys()) - set(data.keys()))
    extra   = sorted(set(data.keys()) - set(en.keys()))

    if missing:
        print(f"[{loc_file.name}] Missing keys: {len(missing)}")
        for k in missing[:20]:
            print("  -", k)
        ok = False
    if extra:
        print(f"[{loc_file.name}] Extra keys: {len(extra)}")
        for k in extra[:10]:
            print("  -", k)

    for k, en_val in en.items():
        if k in data:
            ph_en = placeholders(en_val)
            ph_tr = placeholders(data[k])
            if ph_en != ph_tr:
                print(f"[{loc_file.name}] Placeholder mismatch for '{k}': en={ph_en} tr={ph_tr}")
                ok = False

sys.exit(0 if ok else 1)

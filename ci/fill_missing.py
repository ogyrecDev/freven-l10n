#!/usr/bin/env python3
import argparse, json, os, sys
from collections import OrderedDict
import re

def load(path):
    # preserve order of keys
    with open(path, "r", encoding="utf-8") as f:
        return json.load(f, object_pairs_hook=OrderedDict)

def save(path, obj):
    with open(path, "w", encoding="utf-8") as f:
        json.dump(obj, f, ensure_ascii=False, indent=2)
        f.write("\n")

def placeholder_set(s: str):
    return tuple(sorted(set(re.findall(r"\{(\d+)\}", s))))

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--base", required=True, help="path to locales/en-US.json")
    ap.add_argument("--locale", required=True, help="path to locales/xx-YY.json or 'ALL'")
    ap.add_argument("--write", action="store_true", help="write changes to disk")
    args = ap.parse_args()

    base = load(args.base)
    locales_dir = os.path.dirname(args.base)

    paths = []
    if args.locale.upper() == "ALL":
        for name in os.listdir(locales_dir):
            if name.endswith(".json") and name != os.path.basename(args.base):
                paths.append(os.path.join(locales_dir, name))
    else:
        paths.append(args.locale)

    changed_any = False
    for p in paths:
        try:
            data = load(p)
        except FileNotFoundError:
            print(f"[fill] create {p}")
            data = OrderedDict()

        merged = OrderedDict()
        missing_count = 0

        # align order with en-US
        for k, en_val in base.items():
            if k in data:
                merged[k] = data[k]
            else:
                merged[k] = en_val
                missing_count += 1

        # keep extra keys from locale at the end
        for k in data.keys():
            if k not in base:
                merged[k] = data[k]

        bad = []
        for k, v in merged.items():
            if k in base and isinstance(v, str) and isinstance(base[k], str):
                if placeholder_set(v) != placeholder_set(base[k]):
                    bad.append(k)
        if bad:
            print(f"[warn] {os.path.basename(p)}: placeholder mismatch in {len(bad)} keys (e.g. {bad[:3]})")

        if missing_count == 0 and list(merged.keys()) == list(data.keys()):
            print(f"[fill] {os.path.basename(p)}: up to date")
            continue

        print(f"[fill] {os.path.basename(p)}: +{missing_count} keys; re-ordered to match en-US")
        changed_any = True
        if args.write:
            save(p, merged)

    if not changed_any:
        print("[fill] nothing to do")

if __name__ == "__main__":
    sys.exit(main())

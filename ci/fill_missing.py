#!/usr/bin/env python3
import argparse, json, os, sys
from collections import OrderedDict

def load(path):
    with open(path, "r", encoding="utf-8") as f:
        return json.load(f)

def save(path, obj):
    ordered = OrderedDict(sorted(obj.items(), key=lambda kv: kv[0]))
    with open(path, "w", encoding="utf-8") as f:
        json.dump(ordered, f, ensure_ascii=False, indent=2)
        f.write("\n")

def placeholder_set(s):
    import re
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
            data = {}
        missing = [k for k in base.keys() if k not in data]
        if not missing:
            print(f"[fill] {os.path.basename(p)}: up to date")
            continue

        for k in missing:
            data[k] = base[k]

        bad = []
        for k, v in data.items():
            if k in base:
                if placeholder_set(v) != placeholder_set(base[k]):
                    bad.append(k)
        if bad:
            print(f"[warn] {os.path.basename(p)}: placeholder mismatch in {len(bad)} keys (e.g. {bad[:3]})")

        print(f"[fill] {os.path.basename(p)}: +{len(missing)} keys")
        changed_any = True
        if args.write:
            save(p, data)

    if not changed_any:
        print("[fill] nothing to do")

if __name__ == "__main__":
    sys.exit(main())

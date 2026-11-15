#!/usr/bin/env python3
"""Builds index.json from designs/<id>/ (design.ahwp + thumb.jpg + meta.json).
Run from the repo root before every commit:  python tools/make_index.py"""
import hashlib, json, os, sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
MAX_MB = 20   # shortcut: jsDelivr won't serve bigger files from a repo; put those in GitHub Releases instead

def sha256(path):
    h = hashlib.sha256()
    with open(path, "rb") as f:
        for chunk in iter(lambda: f.read(1 << 20), b""): h.update(chunk)
    return h.hexdigest()

designs, errors = [], []
ddir = os.path.join(ROOT, "designs")
for did in sorted(os.listdir(ddir)):
    d = os.path.join(ddir, did)
    if not os.path.isdir(d) or did == "example": continue
    ahwp, thumb, meta = (os.path.join(d, n) for n in ("design.ahwp", "thumb.jpg", "meta.json"))
    missing = [os.path.basename(p) for p in (ahwp, thumb, meta) if not os.path.isfile(p)]
    if missing: errors.append(f"{did}: missing {', '.join(missing)}"); continue
    size = os.path.getsize(ahwp)
    if size > MAX_MB * 1024 * 1024: errors.append(f"{did}: design.ahwp is over {MAX_MB} MB"); continue
    m = json.load(open(meta, encoding="utf-8"))
    designs.append({
        "id": did,
        "name": m["name"], "nameAr": m.get("nameAr", m["name"]),
        "author": m.get("author", ""),
        "file": f"designs/{did}/design.ahwp", "thumb": f"designs/{did}/thumb.jpg",
        "size": size, "sha256": sha256(ahwp),
    })

json.dump({"version": 1, "designs": designs}, open(os.path.join(ROOT, "index.json"), "w", encoding="utf-8"), ensure_ascii=False, indent=2)
print(f"index.json: {len(designs)} designs")
for e in errors: print("skipped ->", e)
sys.exit(1 if errors else 0)

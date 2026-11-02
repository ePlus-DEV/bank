#!/usr/bin/env python3
"""Build a static BankHub site from YAML. © ePlus.DEV."""
import json
import pathlib
import re
import shutil
import sys
import yaml

ROOT = pathlib.Path(__file__).resolve().parents[1]
OUT = ROOT / "_site"
CATEGORIES = {"bank", "wallet", "donate"}
def fail(message):
    raise ValueError(message)

def main():
    data = yaml.safe_load((ROOT / "data/accounts.yml").read_text(encoding="utf-8"))
    if not isinstance(data, dict) or not isinstance(data.get("accounts"), list):
        fail("accounts.yml must contain an accounts list")
    ids = set()
    accounts = []
    for i, a in enumerate(data["accounts"], 1):
        if not isinstance(a, dict):
            fail(f"Account {i} must be an object")
        for field in ("id", "category", "bank", "name", "number"):
            if not isinstance(a.get(field), str) or not a[field].strip():
                fail(f"Account {i}: {field} must be a non-empty string")
        if a["category"] not in CATEGORIES:
            fail(f"Account {i}: invalid category")
        if a["id"] in ids:
            fail(f"Duplicate id: {a['id']}")
        ids.add(a["id"])
        if not isinstance(a.get("enabled", False), bool):
            fail(f"Account {i}: enabled must be boolean")
        if a.get("enabled") and a["category"] == "bank" and not str(a.get("bankId", "")).strip():
            fail(f"Account {i}: enabled bank requires bankId")
        if a.get("enabled") and not re.fullmatch(r"[0-9]{4,30}", a["number"]):
            fail(f"Account {i}: enabled account number must contain 4–30 digits")
        accounts.append({
            "id": a["id"], "category": a["category"], "bank": a["bank"],
            "bankId": str(a.get("bankId", "")), "name": a["name"],
            "number": a["number"], "note": str(a.get("note", "")),
            "featured": a.get("featured", False) is True,
            "enabled": a.get("enabled", False),
        })
    template = (ROOT / "index.html").read_text(encoding="utf-8")
    pattern = r"const accounts=\[.*?\];"
    encoded = json.dumps(accounts, ensure_ascii=False).replace("<", "\\u003c").replace(">", "\\u003e").replace("&", "\\u0026")
    updated, count = re.subn(pattern, lambda _: "const accounts=" + encoded + ";", template, count=1, flags=re.S)
    if count != 1:
        fail("Could not locate accounts array in index.html")
    OUT.mkdir(exist_ok=True)
    (OUT / "index.html").write_text(updated, encoding="utf-8")
    for name in ("CNAME", "favicon.ico", "robots.txt"):
        source = ROOT / name
        if source.exists():
            shutil.copy2(source, OUT / name)
    (OUT / ".nojekyll").touch()
    print(f"Built {OUT} with {len(accounts)} accounts ({sum(a['enabled'] for a in accounts)} enabled)")

if __name__ == "__main__":
    try:
        main()
    except (ValueError, yaml.YAMLError) as error:
        print(f"Build failed: {error}", file=sys.stderr)
        sys.exit(1)

#!/usr/bin/env python3
"""
Valide data/prices.json avant de merger une pull request.
Vérifie que chaque entrée a bien : item (str), prix (nombre positif), date (ISO 8601 valide).
Rejette aussi les doublons exacts (même item + même date).
"""

import json
import sys
from datetime import datetime

PATH = "data/prices.json"


def fail(msg):
    print(f"::error::{msg}")
    sys.exit(1)


def main():
    try:
        with open(PATH, encoding="utf-8") as f:
            entries = json.load(f)
    except json.JSONDecodeError as e:
        fail(f"JSON invalide dans {PATH} : {e}")
        return

    if not isinstance(entries, list):
        fail(f"{PATH} doit contenir une liste d'entrées.")

    seen = set()
    for i, entry in enumerate(entries):
        if not isinstance(entry, dict):
            fail(f"Entrée #{i} n'est pas un objet valide.")

        for field in ("item", "prix", "date"):
            if field not in entry:
                fail(f"Entrée #{i} : champ '{field}' manquant.")

        if not isinstance(entry["item"], str) or not entry["item"].strip():
            fail(f"Entrée #{i} : 'item' doit être une chaîne non vide.")

        if not isinstance(entry["prix"], (int, float)) or entry["prix"] <= 0:
            fail(f"Entrée #{i} : 'prix' doit être un nombre positif.")

        try:
            datetime.fromisoformat(entry["date"].replace("Z", "+00:00"))
        except (ValueError, AttributeError):
            fail(f"Entrée #{i} : 'date' doit être au format ISO 8601 (ex: 2026-07-15T09:00:00Z).")

        key = (entry["item"].strip().lower(), entry["date"])
        if key in seen:
            fail(f"Entrée #{i} : doublon détecté pour '{entry['item']}' à {entry['date']}.")
        seen.add(key)

    print(f"OK : {len(entries)} entrées valides.")


if __name__ == "__main__":
    main()

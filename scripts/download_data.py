"""
Download datasets
Run: python3 scripts/download_data.py --all

PrimeVul   (function-level, pairs, VD-S)             -> s1 baseline
ReposVul   (function-level + diff + callers/callees) -> inter-procedural context
DiverseVul (large volume) (bonus)                    -> robustness / training
"""

import argparse, os
from datasets import load_dataset

DATA = os.path.join(os.path.dirname(__file__), "..", "data")


def primevul():
    os.makedirs(DATA, exist_ok=True)
    try:
        ds = load_dataset("colin/PrimeVul")
        for split in ds:
            ds[split].to_json(os.path.join(DATA, f"primevul_{split}.jsonl"))
        print("PrimeVul OK ->", DATA)
    except Exception as e:
        print("PrimeVul auto-download failed:", e)


def reposvul():
    print("ReposVul: downloaded from "
          "https://drive.google.com/file/d/1sQynG6Fe2h2zmZ7MFGtAHGIhL3PAZuXF/view?usp=drive_link")


def diversevul():
    os.makedirs(DATA, exist_ok=True)
    try:
        ds = load_dataset("bstee615/diversevul")
        for split in ds:
            ds[split].to_json(os.path.join(DATA, f"diversevul_{split}.jsonl"))
        print("DiverseVul OK ->", DATA)
    except Exception as e:
        print("DiverseVul auto-download failed:", e)


if __name__ == "__main__":
    p = argparse.ArgumentParser()
    p.add_argument("--all", action="store_true")
    p.add_argument("--primevul", action="store_true")
    p.add_argument("--reposvul", action="store_true")
    a = p.parse_args()
    if a.all or a.primevul: primevul()
    if a.all or a.reposvul: reposvul()
    if a.all: diversevul()
    if not any(vars(a).values()): p.print_help()

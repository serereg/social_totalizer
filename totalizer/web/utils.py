import csv
import json
from pathlib import Path
from typing import List, Dict


def form_csv(file: Path, columns: List[str], rows: List[Dict]):
    with open(file, "w", newline="") as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=columns)
        writer.writeheader()
        for row in rows:
            writer.writerow({k: json.dumps(v) for k, v in row.items() if k in columns})

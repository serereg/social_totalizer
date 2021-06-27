import csv
import json
from pathlib import Path
from typing import List, Dict


def form_csv(file: Path, columns: List[str], rows: List[Dict]):
    """Forming csv file from given columns and
        list of rows as dictionaries.

    Args:
        file: file to be created.
        columns: columns for resulting table for csv file.
        rows: list with dictionaries. For example:
            [{"col1": time1, "col2": value1},
            {"col1" time2, "col2": value2}, ...]
    """
    with open(file, "w", newline="") as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=columns)
        writer.writeheader()
        for row in rows:
            writer.writerow({k: json.dumps(v) for k, v in row.items() if k in columns})

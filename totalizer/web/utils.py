import csv
import json
from typing import List, Dict


def form_csv(file, columns: List[str], rows: List[Dict]):
    """Forming csv file-like object from given columns and
        list of rows as dictionaries.

    Args:
        file: file-like object.
        columns: columns for resulting table for csv file.
        rows: list with dictionaries. For example:
            [{"col1": time1, "col2": value1},
            {"col1" time2, "col2": value2}, ...]
    """
    writer = csv.DictWriter(file, fieldnames=columns)
    writer.writeheader()
    for row in rows:
        writer.writerow({k: json.dumps(v) for k, v in row.items() if k in columns})

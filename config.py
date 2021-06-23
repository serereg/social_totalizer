import json
from pathlib import Path


path = Path("settings.json")
CONFIG = json.loads(path.read_text())

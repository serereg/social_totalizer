import json
from pathlib import Path


path = Path(__file__).parent / "settings.json"
CONFIG = json.loads(path.read_text())

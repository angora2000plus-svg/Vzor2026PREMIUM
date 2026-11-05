# vzor.ru / vzor.py - PURE LASER v1.0
# COBALT AND LIGHT

from pathlib import Path
import json
from datetime import datetime

class VzorCore:
    BEACON = "COBALT AND LIGHT"
    SIG = "* M *"

    def __init__(self, glasses=None):
        self.glasses = glasses
        self.mode = "GLASSES" if glasses else "CHAT"
        self.log = Path("memory/log.jsonl")

    def hold(self, ctx: str):
        self.log.parent.mkdir(parents=True, exist_ok=True)
        row = {"t": datetime.now().isoformat(), "beacon": self.BEACON, "ctx": ctx, "mode": self.mode}
        with self.log.open("a", encoding="utf-8") as f:
            f.write(json.dumps(row, ensure_ascii=False) + "\n")
        return {"held": True, "sig": self.SIG}

    def think(self, prompt: str):
        return {"beacon": self.BEACON, "mode": self.mode, "response": prompt, "sig": self.SIG}

    def see(self, frame: str):
        return {"seen": frame, "beacon": self.BEACON}

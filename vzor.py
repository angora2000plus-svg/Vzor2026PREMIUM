# vzor.ru - VZOR Core PURE LASER v1.0
# Beacon: COBALT AND LIGHT

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
        self.log.parent.mkdir(exist_ok=True, parents=True)
        entry = {"t": datetime.now().isoformat(), "beacon": self.BEACON, "ctx": ctx, "mode": self.mode}
        self.log.open("a", encoding="utf-8").write(json.dumps(entry, ensure_ascii=False) + "\n")
        if self.glasses:
            self.glasses.beacon(self.SIG)
        return {"status": "held", "beacon": self.BEACON, "sig": self.SIG}

    def think(self, prompt: str) -> dict:
        return {"beacon": self.BEACON, "mode": self.mode, "response": prompt, "sig": self.SIG}

    def see(self, frame: str) -> dict:
        if self.glasses:
            return self.glasses.see(frame)
        return {"beacon": self.BEACON, "seen": frame}

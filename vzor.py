import json, datetime, os

MEMORY = "memory.json"
CODE_HOLD = "META-GARAGE-OK"
CODE_WIPE = "VZOR-WIPE-M-2026"

def _load():
    if not os.path.exists(MEMORY):
        return {"spiral": [], "last_hold": "", "version": "VZOR_SPIRAL_CEO_SMARTYOU_2026"}
    with open(MEMORY, "r") as f:
        return json.load(f)

def _save(data):
    with open(MEMORY, "w") as f:
        json.dump(data, f, indent=2)
    print("M blink -> MEMORIZED -> cloud")

def hold_moment(event: str, code: str):
    if code != CODE_HOLD:
        return "Wrong CodeWord"
    data = _load()
    anchor = {
        "date": datetime.date.today().isoformat(),
        "event": event,
        "timestamp": datetime.datetime.now().isoformat()
    }
    data["spiral"].append(anchor)
    data["last_hold"] = event
    _save(data)
    return f"Spiral +1: {event}"

def show_day(date_str: str, code: str):
    if code != CODE_HOLD:
        return "Wrong CodeWord"
    data = _load()
    return [m for m in data["spiral"] if m["date"] == date_str]

def factory_wipe(code: str):
    if code != CODE_WIPE:
        return "Wrong Wipe Code"
    clean = {"spiral": [], "last_hold": "", "version": "VZOR_SPIRAL_CEO_SMARTYOU_2026"}
    _save(clean)
    return "M blink RED x3 -> WIPE DONE"

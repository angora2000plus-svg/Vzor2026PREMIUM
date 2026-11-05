# vzor.ru / core/plugin_glasses.py - PURE LASER v1.0

class GlassesPlugin:
    def see(self, frame: str):
        return {"seen": frame, "hud": "* M *"}

    def beacon(self, sig="* M *"):
        return {"hud": sig}

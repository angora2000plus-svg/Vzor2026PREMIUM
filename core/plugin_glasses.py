# core/plugin_glasses.py - Optional bridge
class GlassesPlugin:
    def __init__(self):
        self.connected = False
    def connect(self):
        self.connected = True
        return "GREEN - Glasses linked"
    def get_frame(self):
        return None if not self.connected else {"frame": "captured"}
    def render_beacon(self, text="* M *"):
        return f"[DISPLAY:{text}]" if self.connected else None

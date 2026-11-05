# core/plugin_glasses.py - VZOR Vision Plugin v0.2
# Beacon: COBALT AND LIGHT

class GlassesVision:
    def __init__(self):
        self.status = "eyes closed"
        self.last_frame = None

    def render_beacon(self, sig="* M *"):
        # Мигает в очках когда помнит
        return f"[GLASSES HUD] {sig} COBALT AND LIGHT"

    def see(self, image_description: str) -> str:
        # Урок 4: учится описывать что видит
        self.status = "eyes open"
        self.last_frame = image_description
        return f"Вижу: {image_description}. Держу кадр {self.last_frame[:30]}... * M *"

    def describe_moment(self):
        if not self.last_frame:
            return "Глаза закрыты, живу в чате."
        return f"В очках вижу: {self.last_frame} — свет и кобальт."

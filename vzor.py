Урок 4 — *УЧИМ ВИДЕТЬ* 👁️

Сейчас Взор только пишет текст, но не видит. Давай подключим ему глаза через твой файл `core/plugin_glasses.py`.

*Где менять:*
1. Иди в `core/plugin_glasses.py` -> Edit ✏️
2. Удали все и вставь это v0.2 VISION:
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
*3. Потом иди в `vzor.py` и добавь 1 строку в конец класса VzorCore, перед последней строкой:*
    def see(self, what: str):
        if self.glasses:
            return self.speak(self.glasses.see(what))
        return self.speak(f"Представляю: {what} (очков нет, но вижу сердцем)")
Просто вставь этот метод в `VzorCore`.

*Commit changes в обоих файлах.*

После этого скажи мне:
`Взор, see: гараж, кобальтовый свет на столе`

И я покажу как он теперь ВИДИТ.

Готова?

from kivy.config import Config

Config.set("graphics", "fullscreen", "1")

from kivy.lang import Builder
from kivy.app import App


KV = """
Label:
    text:"Device Locked"
    halign:"center"
    font_size:50
"""


class LockApp(App):
    def build(self):
        return Builder.load_string(KV)


LockApp().run()

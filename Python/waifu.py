from kivy.lang import Builder 
from kivymd.app import MDApp
import requests

KV = """
MDBoxLayout:    
    orientation:"vertical"
    AsyncImage:
        id:image
        fit_mode:"cover"
    MDFlatButton:
        size_hint:1,0.1
        md_bg_color:app.theme_cls.primary_light
        text:"Reload"
        on_press:app.set_source()
"""

class Main(MDApp):

    def build(self):
        return Builder.load_string(KV)
    
    def set_source(self):
        self.root.ids.image.source = requests.get(
                "https://api.waifu.pics/sfw/waifu"
        ).json()["url"]

Main().run()

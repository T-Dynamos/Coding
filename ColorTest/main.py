from kivy.lang import Builder
from kivymd.app import MDApp
from kivymd.uix.boxlayout import MDBoxLayout
from kivy.utils import get_hex_from_color
from kivymd.uix.label import MDLabel
import colorsys
import os 

# File imports
from colorthief import ColorThief
from palettes.core_palette import CorePalette
from utils.theme_utils import themeFromSourceColor

IMAGE_FILE = "/home/tdynamos/Downloads/test.png" # file


class Main(MDApp):

    def build(self):
        # Changable
        self.theme_cls.theme_style = "Light"
        return Builder.load_file("main.kv")

    def rgb_to_argb(self,r, g, b, a=255) -> int:
        return (a << 24) | (r << 16) | (g << 8) | b
    
    def argb_to_rgb(self,argb):
        return ((argb >> 16 ) & 0xff) / 255 , ((argb >> 8) & 0xff) / 255 , (argb & 0xff) / 255, 1 

    def on_start(self): 
        file_size = os.path.getsize(IMAGE_FILE) 
        color_thief = ColorThief(IMAGE_FILE)

        # Generate four most dominant
        _temp = color_thief.get_palette(color_count=4,quality=int(file_size/1000))
        dominat_colors = [
            [1 , k[0] / 255, k[1] / 255, k[2] / 255]
            for k in _temp]
    
        DOMINANT_NO = 3
    
        # Most dominant color
        argb = self.rgb_to_argb(_temp[DOMINANT_NO][0],_temp[DOMINANT_NO][1],_temp[DOMINANT_NO][2])
        color = themeFromSourceColor(argb)

        for k in color["schemes"][self.theme_cls.theme_style.lower()].props.keys():
            label = MDLabel(text=k, halign="center",size_hint=(1,None), height = 60 )
            widget = MDBoxLayout(size_hint=(1,None), height = 60)
            widget.md_bg_color = self.argb_to_rgb(color["schemes"][self.theme_cls.theme_style.lower()].props[k])
            self.root.ids.test.add_widget(label)
            self.root.ids.test.add_widget(widget)

        self.root.ids.bg_.md_bg_color = self.argb_to_rgb(argb)

    def generate_color_tones(self, rgb_color):
        rgb_color = [k * 255 for k in rgb_color]
        h, l, s = colorsys.rgb_to_hls(*[x / 255 for x in rgb_color])
        l = 0
        tones = []
        prev = 1
        for i in NUM_TONES:
            lightness = prev
            r, g, b = colorsys.hls_to_rgb(h, lightness, s)
            r, g, b = r, g, b
            tones.append([r, g, b])
            prev = prev - 1 / len(NUM_TONES)
        return tones
      
Main().run()

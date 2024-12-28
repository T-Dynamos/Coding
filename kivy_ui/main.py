from kivy.lang import Builder
from kivymd.app import MDApp
from kivy_garden.frostedglass import FrostedGlass
from kivy.clock import Clock
from kivy.animation import Animation
import _thread

KV = """
<CSlider@MDBoxLayout>:
    update:print()
    orientation:"vertical"
    text:""
    value:0
    max:69
    MDLabel:
        text:root.text
        padding:[dp(10),0]
        theme_text_color:"Custom"
        text_color:1,1,1,1
    MDSlider:
        size_hint:1,1
        value:root.value
        max:root.max
        hint:False

MDRelativeLayout:
    md_bg_color:app.theme_cls.opposite_bg_dark
    Image:
        id:img
        source:"/home/tdynamos/SnowFlakes/inbuilt_themes/Default/background.jpg"
        size_hint:1,0.5
        pos_hint:{"top":1}
        allow_stretch:True
        keep_ratio:False

    FrostedGlass:
        id:glass
        background:img
        size_hint:0.6,0.2
        pos_hint:{"center_x":0.5,"center_y":0.75}
        blur_size:0
        outline_color:1,1,1,1
        border_radius:[dp(20)] * 4
        overlay_color:[0,0,0,0.2]
        noise_opacity:0.1

    MDBoxLayout:    
        id:box
        size_hint:1,0.6
        pos_hint:{"bottom":1}
        orientation:"vertical"
        radius:[dp(20),dp(20),0,0]
        md_bg_color:app.theme_cls.opposite_bg_dark
        CSlider:
            text:"Noise"
            value:glass.noise_opacity
            max:1
        CSlider:
            text:"Blur"
            value:glass.blur_size
            max:100
        CSlider:
            text:"Saturation"
            value:glass.saturation
            max:10
        CSlider:
            value:glass.luminosity
            text:"Luminosity"
            max:10
        
"""


class Frost(MDApp):
    def build(self):
        return Builder.load_string(KV)

    def set(self, typed, value, widget):
        if typed == "noise":
            self.root.ids.glass.noise_opacity = value
        elif typed == "blur":
            self.root.ids.glass.blur_size = value
        elif typed == "luminosity":
            self.root.ids.glass.luminosity = value
        elif typed == "saturation":
            self.root.ids.glass.saturation = value
        widget.parent.text = widget.parent.text.split(" : ")[0] + " : " + str(value)

    def on_start(self):
        #  Clock.schedule_once(self.main_thread)
        self.root.ids.box.children[-1].children[0].bind(
            value=lambda x, y: self.set("noise", y, x)
        )
        self.root.ids.box.children[-2].children[0].bind(
            value=lambda x, y: self.set("blur", y, x)
        )
        self.root.ids.box.children[-3].children[0].bind(
            value=lambda x, y: self.set("saturation", y, x)
        )
        self.root.ids.box.children[-4].children[0].bind(
            value=lambda x, y: self.set("luminosity", y, x)
        )


Frost().run()

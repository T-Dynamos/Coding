from kivy.lang import Builder
from kivymd.app import MDApp
from kivy.core.window import Window
from kivy.clock import Clock
import string
import sys

arg = list(sys.argv)

del arg[-1]
del arg[-1]

if len(arg) < 2:
    arg.append("400")
    arg.append("100")

Window.size = [int(arg[1]),int(arg[2])]

VIEW = f"""
#:import sys sys

MDRelativeLayout:
    md_bg_color:app.theme_cls.bg_dark
    MDLabel:
        id:key_label
        text:"Key"
        halign:"center"
        font_name:'{str(sys.argv[sys.argv.index("font")+1])}'
        font_size:"50sp"
"""

class MainView(MDApp):

    def build(self):
        self.theme_cls.theme_style = "Dark"
        Window.borderless = True
        Window.bind(on_keyboard=self.on_keyboard)
        return Builder.load_string(VIEW)

    def on_keyboard(self,*largs):
        if largs[-2] is not None and largs[-2] in list(string.ascii_lowercase+string.ascii_uppercase+"""123456789     {[:;'"<,.>?/|\=+-_)(*&^%$#@!)~`]}"""):
            self.root.ids.key_label.text = largs[-2] 
        else:
            print(largs)
            self.root.ids.key_label.text = str(largs[-1][-1] if largs[-1][-1] != "capslock" else largs[-1][0]).capitalize() if len(largs[-1]) != 0 and len(largs[-1]) >= 1 else "Capslock"

MainView().run()

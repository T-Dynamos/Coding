import os
from datetime import datetime
from random import SystemRandom

random = SystemRandom()

from kivy.animation import Animation
from kivy.app import App
from kivy.clock import Clock
from kivy.core.window import Window
from kivy.graphics.context_instructions import Color
from kivy.graphics.vertex_instructions import RoundedRectangle
from kivy.lang import Builder
from kivy.metrics import dp
from kivy.properties import ColorProperty, ListProperty
from kivy.uix.widget import Widget
from kivy.utils import get_color_from_hex

NUM_POINTS = 20

class Chaos(Widget):
    points = ListProperty()
    point_color = ColorProperty(get_color_from_hex("#4E6379"))
    pt_size = dp(20)
    anim_time = 1
    anim_t = "in_out_circ"

    def start_anim(self, *args):
        h2 = int(Window.height / 2)
        new_points = list(self.points)

        for i, pt in enumerate(self._pts):
            new_pos = [self.points[i][0], h2 + dp(random.randint(-h2 + 50, h2 - 50))]
            anim = Animation(
                pos=[new_pos[0] - self.pt_size / 2, new_pos[1] - self.pt_size / 2],
                d=1,
                t=self.anim_t,
            )
            anim.cancel_all(pt)
            anim.start(pt)
            new_points[i] = new_pos

        Animation(points=new_points, d=1, t=self.anim_t).start(self)

    _pts = []

    def pt_update(self, *args):
        self.canvas.clear()
        self._pts.clear()
        with self.canvas:
            for pt in self.points:
                Color(rgba=self.point_color)
                rect = RoundedRectangle(
                    pos=[pt[0] - self.pt_size / 2, pt[1] - self.pt_size / 2],
                    size=[self.pt_size] * 2,
                    radius=[self.pt_size / 2] * 4,
                )
                self._pts.append(rect)


KV = """
AnchorLayout:
    Chaos:
        id:chaos
        canvas.before:
            Line:
                width:dp(2)
                points:self.points
    Label:
        id:time
        text_size:self.size
        font_size:"150sp"
        halign:"center"
        valign:"center"
        font_name:"/home/tdynamos/Moon/fonts/bold.ttf"
        canvas.before:
            Color:
                rgba:[0,0,0,.7]
            Rectangle:
                size:self.size
                pos:self.pos
"""


class TimeApp(App):
    def build(self):
        Window.size = self.get_resolution()
        Window.bind(size=self.update_points)
        return Builder.load_string(KV)

    def get_resolution(self):
        return [
            int(_)
            for _ in os.popen("xrandr")
            .read()
            .split("current")[-1]
            .split(",")[0]
            .strip()
            .split("x")
        ]

    def on_start(self):
        self.update_points()
        Clock.schedule_interval(self.update_time, 0.95)

    def update_points(self, *args):
        pts = []
        spacing = (Window.width) / NUM_POINTS
        h2 = int(Window.height / 2)
        for point in range(NUM_POINTS + 1):
            pts.append(
                [
                    spacing * point,
                    h2 + dp(random.randint(-h2 + 50, h2 - 50)),
                ]
            )

        self.root.ids.chaos.points = pts
        self.root.ids.chaos.pt_update()
        Clock.schedule_interval(
            self.root.ids.chaos.start_anim, self.root.ids.chaos.anim_time
        )

    def update_time(self, *args):
        self.root.ids.time.text = datetime.now().strftime("%I:%M:%S %p")


TimeApp().run()

from kivy.app import App
from kivy.lang import Builder
from kivy.clock import Clock
import math

from kivy.uix.floatlayout import FloatLayout
from kivy.properties import ListProperty


class LineAnimation(FloatLayout):
    points = ListProperty([])


KV = """ 
RelativeLayout:
    # LineAnimation:
    #     id:p1
    #     canvas:
    #         Color:
    #             rgba: [0,1,1,1]
    #         Line:
    #             points: self.points
    # LineAnimation:
    #     id:p2
    #     canvas:
    #         Color:
    #             rgba: [1,0,1,1]
    #         Line:
    #             points: self.points
    BoxLayout:
        id:particle_1
        size_hint:None, None
        size:[dp(30)] * 2
        x:(self.parent.width - self.width ) * 0.5 
        y:(self.parent.height - self.height ) * 0.5 
        canvas:
            Color:
                rgba:[0,1,1,1]
            RoundedRectangle:
                size:self.size
                pos:self.pos
                radius:[self.height/2] * 4
    BoxLayout:
        id:particle_2
        size_hint:None, None
        size:[dp(30)] * 2
        x:(self.parent.width - self.width ) * 0.5 
        y:(self.parent.height - self.height ) * 0.5 
        canvas:
            Color:
                rgba:[1,0,1,1]
            RoundedRectangle:
                size:self.size
                pos:self.pos
                radius:[self.height/2] * 4
"""


class WaveAnimation(App):
    particle = None

    # ui constants
    time = 0
    c = 0

    def build(self):
        layout = Builder.load_string(KV)
        self.particle_1 = layout.ids.particle_1
        self.particle_2 = layout.ids.particle_2
        return layout

    def on_start(self):
        self.c = (self.particle_1.parent.height - self.particle_1.height) * 0.5
        Clock.schedule_interval(self.update, 0)

    def wave(self, amplitude, frequency, k, x, t):
        return amplitude * math.sin(2 * math.pi * frequency * t + k * x)

    # TODO: implement for n waves?
    def wave_net(self, a1, f1, k1, x1, a2, f2, k2, x2, t):
        # are these conditions required?
        # assert k1 == k2
        # assert f2 == f1
        phase_diff = 2 * math.pi * (f1 * t - f2 * t) + k1 * x1 - k2 * x2
        net_amplitude = a1**2 + a2**2 + 2 * a1 * a2 * math.cos(phase_diff)
        theta = math.atan(
            (a2 * math.sin(phase_diff)) / (a1 + a2 * math.cos(phase_diff))
        )
        return net_amplitude * math.sin(
            2 * math.pi * f1 * t + (k1 * x1) + theta
        ), net_amplitude
    
    def update(self, dt):
        self.time += dt
        sol1, n1 = self.wave_net(
            *[4, 1, 1, 10],  # wave 1
            *[4, 1, 1, 80],  # wave 2
            self.time,
        )

        # WOW!!!
        # Alakh Sir words works!!
        # when frequency isn't same phase is time dependent!!!!!!
        sol2, n2 = self.wave_net(
            *[4, 0.1, 1, 10],  # wave 1
            *[3, 1, 1, 20],  # wave 2
            self.time,
        )
        self.particle_2.y = self.c + sol2
        self.particle_1.y = self.c + sol1


WaveAnimation().run()

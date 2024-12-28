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
    canvas:
        Color:
            rgba:1,1,1,0.5
        Line:
            points:[ [self.width/2,0], [self.width/2, self.height] ]
        Color:
            rgba:1,1,1,0.5
        Line:
            points:[[0,self.height/2], [self.width, self.height/2] ]
    Label:
        size_hint:None, None
        size:[dp(50), dp(50)]
        halign:"center"
        id:fps
        text:"0"
    BoxLayout
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
    BoxLayout:
        id:particle_3
        size_hint:None, None
        size:[dp(30)] * 2
        x:(self.parent.width - self.width ) * 0.5 
        y:(self.parent.height - self.height ) * 0.5 
        canvas:
            Color:
                rgba:[1,1,0,1]
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
        return Builder.load_string(KV)

    def on_start(self):
        self.c = (self.root.ids.particle_1.parent.height - self.root.ids.particle_1.height) * 0.5
        Clock.schedule_interval(self.update, 0)
        Clock.schedule_interval(self._print_fps, 1)

    def wave(self, amplitude, frequency, k, x, t):
        return amplitude * math.sin(2 * math.pi * frequency * t + k * x)

    # TODO: implement for n waves?
    def wave_net(self, a1, f1, k1, x1, a2, f2, k2, x2, t):
        # are these conditions required?
        # assert k1 == k2
        # assert f2 == f1
        phase_diff = (2 * math.pi * (f1 * t - f2 * t)) + k1 * x1 - k2 * x2
        net_amplitude = math.sqrt(a1**2 + a2**2 + 2 * a1 * a2 * math.cos(phase_diff))

        # if net_amplitude == a1 + a2:
        #     print("constructive", net_amplitude)
        # elif net_amplitude == a1 - a2:
        #     print("destructive", net_amplitude)
        # else:
        #     print("Something else?", net_amplitude)

        if net_amplitude > 0:
            theta = math.atan(
                (a2 * math.sin(phase_diff)) / (a1 + a2 * math.cos(phase_diff))
            )
        else:
            # atan not defined at 90 degree
            theta = math.pi / 2
        
        return net_amplitude * math.sin(
            2 * math.pi * f1 * t + (k1 * x1) + theta
        ), net_amplitude
    
    def _print_fps(self, *largs):
        self.root.ids.fps.text = str(Clock.get_rfps())
    
    def update(self, dt):
        self.time += dt
        _lambda = 2
        _frequency = 1
        w1 = [50, _frequency, math.pi * 2 / _lambda, 11]
        w2 = [50, _frequency, math.pi * 2 / _lambda, 18]
        self.root.ids.particle_1.y = self.c + self.wave(*w1, self.time)
        self.root.ids.particle_2.y = self.c + self.wave(*w2, self.time)
        # when frequency isn't same phase is time dependent
        pos, net_amplitude = self.wave_net(
            *w1,  # wave 1
            *w2,  # wave 2
            self.time,
        )
        self.root.ids.particle_3.y = self.c + pos
        # net_amplitude changes with time
        # print(net_amplitude)


WaveAnimation().run()

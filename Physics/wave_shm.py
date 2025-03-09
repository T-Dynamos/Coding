from kivy.app import App
from kivy.lang import Builder
from kivy.clock import Clock
import math
import gc

from kivy.uix.floatlayout import FloatLayout
from kivy.properties import ListProperty
from kivy.metrics import dp
from kivy.core.window import Window

Window.size = [700, 500] 

class LineAnimation(FloatLayout):
    points = ListProperty([])


KV = """ 
RelativeLayout:

    LineAnimation:
        id:wave_1
        canvas:
            Color:
                rgba:[0,1,1,1]
            SmoothLine:
                points:self.points
    LineAnimation:
        id:wave_2
        canvas:
            Color:
                rgba:[1,0,1,1]
            SmoothLine:
                points:self.points
    LineAnimation:
        id:wave_net
        width:dp(2)
        canvas:
            Color:
                rgba:[1,1,0,0]
            SmoothLine:
                points:self.points
            SmoothLine:
                points:self.points
    LineAnimation:
        id:wave_net_2
        width:dp(2)
        canvas:
            Color:
                rgba:[1,0.5,0.5,1]
            SmoothLine:
                points:self.points
    Label:
        size_hint:None, None
        size:[self.texture_size[0] + dp(10), self.texture_size[1] + dp(10)]
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
                rgba:[1,1,0,0]
            RoundedRectangle:
                size:self.size
                pos:self.pos
                radius:[self.height/2] * 4
    BoxLayout:
        id:particle_4
        size_hint:None, None
        size:[dp(30)] * 2
        x:(self.parent.width - self.width ) * 0.5 
        y:(self.parent.height - self.height ) * 0.5 
        canvas:
            Color:
                rgba:[1,0.5,0.5,1]
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
        self.c = (
            self.root.ids.particle_1.parent.height - self.root.ids.particle_1.height
        ) * 0.5
        Clock.schedule_interval(self.update, 0)
        Clock.schedule_interval(self._print_fps, 1)
        super().on_start()
        # Clock.schedule_interval(lambda _: gc.collect(), 60)

    def wave(self, amplitude, freq, k, phase, x, t):
        return amplitude * math.sin(2 * math.pi * freq * t + k * x + phase)

    # TODO: implement for n waves?
    def wave_net(self, a1, f1, k1, x1, a2, f2, k2, x2, t):
        # only works for these conditioans
        # assert k1 == k2
        # assert f2 == f1
        phase_diff = (2 * math.pi * (f1 * t - f2 * t)) + k1 * x1 - k2 * x2
        net_amplitude = math.sqrt(a1**2 + a2**2 + 2 * a1 * a2 * math.cos(phase_diff))
        if net_amplitude > 0:
            theta = math.atan(
                (a2 * math.sin(phase_diff)) / (a1 + a2 * math.cos(phase_diff))
            )
        else:
            # atan not defined at 90 degree
            theta = math.pi / 2
        return net_amplitude * math.sin(2 * math.pi * f1 * t + (k1 * x1)  + (k2 * x2) + theta)

    def _print_fps(self, *largs):
        self.root.ids.fps.text = "FPS: " + str(Clock.get_rfps())


    def update(self, dt):
        # UI related internal stuff
        ############################
        time_slow = 2
        self.time += dt / time_slow
        _p_w = self.root.ids.particle_1.width / 2
        self.c = self.root.height / 2 - _p_w
        width = self.root.width
        epsilon = 0.4e3
        dx = width/epsilon
        ############################

        # define waves
        k1 = 5
        k2 = -5
        freq_1 = 1
        freq_2 = 1
        w1 = [100, freq_1, k1, math.pi/2,  0]
        w2 = [100, freq_2, k2, 0,  0]

        # set postion of particles
        self.root.ids.particle_1.y = -1000 + self.c + self.wave(*w1, self.time)
        self.root.ids.particle_2.y = -1000 + self.c + self.wave(*w2, self.time)
        self.root.ids.particle_4.y = -1000 + self.c +self.wave(*w1, self.time) +  self.wave(*w2, self.time)

        # Add waves
        wave_1_points = []
        wave_2_points = []
        wave_net_points = []
        wave_net_2_points = []
        # no waves visible in screen

        _width = 0
        while _width < width:
            # derived purely by error and trial
            w1[-1] = w2[-1] =  (0.5 * width - _width)/epsilon
            wave_1_points.append([_width, self.c + _p_w + self.wave(*w1, self.time)])
            wave_2_points.append([_width, self.c + _p_w + self.wave(*w2, self.time)])
            # wave_net_points.append([_width, self.c + _p_w + self.wave_net(*w1, *w2, y)])
            wave_net_2_points.append(
                [_width, self.c + _p_w + self.wave(*w1, self.time) + self.wave(*w2, self.time)])
            _width += dx

        # set to points
        self.root.ids.wave_1.points = wave_1_points
        self.root.ids.wave_2.points = wave_2_points
        self.root.ids.wave_net_2.points = wave_net_2_points


WaveAnimation().run()

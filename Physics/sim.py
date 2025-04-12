from kivy.app import App
from kivy.uix.widget import Widget
from kivy.uix.label import Label
from kivy.graphics import Ellipse, Color, Triangle
from kivy.clock import Clock
from math import sqrt
import math
from kivy.properties import ListProperty

from collections import deque

from kivy.core.window import Window

class Body(Widget):

    line_points  = deque(maxlen=5)

    def __init__(self, mass, pos, vel, color, **kwargs):
        super().__init__(**kwargs)
        self.mass = mass
        self.pos_x, self.pos_y = pos
        self.vel_x, self.vel_y = vel
        self.size = (10, 10)
        self.canvas.add(Color(*color))
        self.ellipse = Ellipse(pos=(self.pos_x, self.pos_y), size=self.size)
        self.canvas.add(self.ellipse)

    def update_position(self):
        self.pos_x += self.vel_x
        self.pos_y += self.vel_y
        self.ellipse.pos = (self.pos_x, self.pos_y)

    def apply_force(self, fx, fy):
        self.vel_x += fx / self.mass
        self.vel_y += fy / self.mass

class ThreeBodySimulation(Widget):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        zero_x = Window.width/2 
        zero_y = Window.height/2
        
        b1_pos =  [zero_x + 0, zero_y + 50]
        b2_pos =  [zero_x + 0, zero_y - 50]
        b3_pos =  [zero_x, zero_y]
        #
        # self.triangle = Triangle(points=[*[b1_pos + b2_pos + b3_pos]])
        # self.canvas.add(self.triangle)

        # Initialize 3 bodies 
        self.bodies = [
            Body(1, b1_pos, [+1, 0], (1, 0, 0)),   # red
            Body(1, b2_pos, [-1, 0], (0, 1, 0)),  # green
            Body(0.00001, b3_pos, [0, 0], (0, 0, 1)),  # blue
    ]
        for body in self.bodies:
            self.add_widget(body)

        Clock.schedule_interval(self.update, 0)

    def update(self, dt):
        G = 150
        # Gravitational constant tweak for stability

        forces = [[0, 0] for _ in self.bodies]

        # Calculate pairwise gravitational forces
        for i in range(len(self.bodies)):
            for j in range(i + 1, len(self.bodies)):
                dx = self.bodies[j].pos_x - self.bodies[i].pos_x
                dy = self.bodies[j].pos_y - self.bodies[i].pos_y
                dist_sq = dx ** 2 + dy ** 2 + 1e-5  # avoid division by zero
                dist = sqrt(dist_sq)
                force = G * self.bodies[i].mass * self.bodies[j].mass / dist_sq
                fx = force * dx / dist
                fy = force * dy / dist

                forces[i][0] += fx
                forces[i][1] += fy
                forces[j][0] -= fx
                forces[j][1] -= fy

        # Apply forces and update positions
        _pt = []
        for i, body in enumerate(self.bodies):
            fx, fy = forces[i]
            body.apply_force(fx, fy)
            body.update_position()
            _pt.append(body.pos_x)
            _pt.append(body.pos_y)

        # self.triangle.points = _pt

class ThreeBodyApp(App):
    
    def build(self):
        
        return ThreeBodySimulation()

if __name__ == '__main__':
    ThreeBodyApp().run()


import vispy
import numpy as np
from vispy.scene import visuals
import math

def f(x):
    return math.sin(x)

def function_to_points(
        function, 
        y_start,
        y_end, 
        resolution = 0.1, 
        max_points=float("inf")
):
    points = []
    current = y_start
    
    while current < y_end:
        try:
            x,z = function(current)
            points.append([current, x, z])
        except Exception as e:
            print(e)
            pass
        current += resolution
    
    if max_points != float("inf"):
        _f = []
        _c = 0
        __ = int(len(points)/max_points)
        while len(_f) < max_points:
            try:
                _f.append(points[_c])
            except:
                break
            _c += __
        points = _f
    print(len(points))
    return points 

def points_to_scatter(points, connect=None, line=True, **kwargs):
    scatter = visuals.Markers() if not line else visuals.Line( antialias=True)
    if line:
        kwargs["color"] = "yellow"
        # kwargs["connect"] = np.matrix(connect)
    scatter.set_data(
        np.matrix(points), **kwargs 
    )
    return scatter

canvas = vispy.scene.SceneCanvas(keys='interactive', show=True)
view = canvas.central_widget.add_view()

view.add(
points_to_scatter(
# functions to points
function_to_points(
    lambda x: ( x - x**2, 0),
    -math.pi*5,
    math.pi*5,
    0.01,
) 
))

view.camera = 'turntable'
view.border_color = "red"
vispy.app.run()

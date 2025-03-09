import numpy as np
import wave
import os
rate = 44100

import sys
num = float(sys.argv[1])

def play_in_loop(file):
    os.system(f"mpv {file} --loop")

def play_function(func):
    output_filename = f'{os.path.expanduser("~")}/.cache/test.wav'
    with wave.open(output_filename, 'wb') as wf:
        wf.setnchannels(1)
        wf.setsampwidth(2)
        wf.setframerate(rate)
        wf.writeframes(np.int16(func * 32767).tobytes())
    play_in_loop(output_filename)

def func():
    duration = 0.5
    t = np.linspace(0, duration, int(rate * duration), endpoint=False)
    return 1 * np.sin(2*np.pi  *  num *t) 

play_function(func())

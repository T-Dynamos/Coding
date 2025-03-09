import subprocess
import numpy as np
from concurrent.futures import ThreadPoolExecutor
from kivy.app import App
from kivy.graphics.texture import Texture
from kivy.lang import Builder
from kivy.clock import Clock
import time
from kivy.config import Config
import traceback

Config.set("graphics", "maxfps", 0)

class ThreadExecutor:
    _thread = None

    def __init__(self):
        self._thread = ThreadPoolExecutor(max_workers=5)

    def function_wrapper(self, function_, *args):
        try:
            function_(*args)
        except Exception as e:
            print(traceback.format_exc())

    def submit(self, function_, *args):
        self._thread.submit(self.function_wrapper, function_, *args)

class VideoRecordingApp(App):
    output_file = "output.mkv"
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.ffmpeg_process = None
        self.frame_rate = 30
        self.frame_count = 0
        self.thread = ThreadExecutor()

    def on_start(self):
        self.start_recording()
        super().on_start()

    def on_stop(self):
        self.recording = False
        if self.ffmpeg_process:
            self.ffmpeg_process.stdin.close()
            self.ffmpeg_process.wait()
    
    recording = False
    def start_recording(self):
        self.recording = True
        def __(*args):
            self._texture = np.frombuffer(self.root.export_as_image().texture.pixels, dtype=np.uint8)
        Clock.schedule_interval(__, 0)
        self.thread.submit(self._start_recording)

    _texture = None
    def _start_recording(self):
        self.ffmpeg_process = subprocess.Popen(
            [
                "ffmpeg",
                "-y",
                "-f", "rawvideo",  
                "-vcodec", "rawvideo",  
                "-pix_fmt", "rgba",  
                "-s", f"{int(self.root.width)}x{int(self.root.height)}",  
                "-r", str(self.frame_rate),
                "-i", "-",
                "-c:v", "libx264", 
                "-preset", "fast", 
                "-crf", "23",
                "-pix_fmt", "yuv420p",
                self.output_file,
            ],
            stdin=subprocess.PIPE,
        )
        while self.recording:
            while self._texture is None:
                pass
            self.thread.submit(self.write_frame, self._texture)
            self._texture = None
            time.sleep(1/(self.frame_rate + 5))

    def write_frame(self, texture):
        texture_data = texture
        texture_data = texture.reshape((self.root.height, self.root.width, 4))
        self.ffmpeg_process.stdin.write(texture_data.tobytes())

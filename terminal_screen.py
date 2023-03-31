import os 
import time

class TerminalScreen:

    def __init__(self,char="█",small_char="▄",char_lenght=10):
        self.char = char
        self.char_lenght = char_lenght
        self.small_char = small_char
        self.get_terminal_size()

    def get_terminal_size(self) -> list:
        self.terminal_size = list(os.get_terminal_size())
        return self.terminal_size

    def clear(self,clear_cmd="clear") -> os.system:
        return os.system(clear_cmd)

    def center_print(self, text : str) -> print:
        self.clear()
        vertical_lines = len(text.split("\n"))
        vertical_split = ["\n"*(int(self.terminal_size[-1]/2)-int(vertical_lines/2))]
        center_content = [line.center(self.terminal_size[0]) for line in text.split("\n")]
        final_content = vertical_split + center_content + vertical_split
        return print("".join(final_content),end="")

    def random_figure(self, size : int) -> list:
        print((self.char+" "*(size)+self.char)+" "*(size-1))[:-1]*int(self.terminal_size[-1]/2)

terminal_screen = TerminalScreen()

i = 0 

while True:
    i += 1
    #print(terminal_screen.random_figure(i))
    terminal_screen.center_print(terminal_screen.random_figure(i))
    time.sleep(0.1)

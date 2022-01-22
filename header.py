################################## HEADER SCRIPT 1.0 ###################################
import os 
import sys
from itertools import cycle
from shutil import get_terminal_size
from threading import Thread
from time import sleep
import time
exit_status = 1
store_true = ""
col = {"BL" : '\033[30m',"B" : '\033[94m',"C" : '\033[96m',"D" : '\033[36m',"G" : '\033[92m',"P" : '\033[95m',"R" : '\033[91m',"Y": '\033[93m',"W" : '\033[37m',"BLACK_BG" : '\033[40m',"RED_BG" : '\033[41m',"GREEN_BG" : '\033[42m',"YELLOW_BG" : '\033[43m',"BLUE_BG" : '\033[44m',"PURPLE_BG" : '\033[45m',"CYAN_BG" : '\033[46m',"WHITE_BG" : '\033[47m',"BOLD" : '\033[1m',"FAINT" : '\033[2m',"ITALIC" : '\033[3m',"UNDERLINE" : '\033[4m',"BLINK" : '\033[5m',"INVERSE" : '\033[7m',"HIDDEN": '\033[8m',"STRIKE" : '\033[9m',"END" : '\033[0m'}

class Loader:
    def __init__(self, desc="Loading...", end="Done!", timeout=0.1):

        self.desc = desc
        self.end = end
        self.timeout = timeout

        self._thread = Thread(target=self._animate)
        self.steps = ["⢿ ", "⣻ ", "⣽ ", "⣾ ", "⣷ ", "⣯ ", "⣟ ", "⡿ "]
        self.done = False

    def start(self):
        self._thread.start()
        return self

    def _animate(self):
        for c in cycle(self.steps):
            if self.done:
                break
            print(f"\r{col['W']+c} {self.desc} ", flush=True, end="")
            sleep(self.timeout)

    def enter(self):
        self.start()

    def stop(self):
        self.done = True
        cols = get_terminal_size((80, 20)).columns
        print("\r" + f"" * cols, end="", flush=True)
        print(f"\r{self.end}", flush=True)

    def exit(self, exc_type, exc_value, tb):
        self.stop()

def checkImport(module):
	try:
		exec(f"import {module}")
	except Exception:
		return False
	return True
def chekPacakage(pacakage):
	from shutil import which 
	if which(pacakage) is None:
		return False
	else:
		return True
def getArgs(test_args,type=""):
	args = sys.argv
	if type == str or type==None:
		if test_args in args:
			try:
				arg = (args[args.index(test_args)+1])
				return arg
			except IndexError:
				return "" 
		else:
			return None
	
	elif type == int:
		if test_args in args:
			try:
				arg = int(args[args.index(test_args)+1])
				return arg
			except ValueError:
				raise ValueError(f"'{test_args}' is not an integer ") from None	
			except IndexError:
				return "" 
		else:
			return None
	elif type == store_true:
		if test_args in args:
			return True 
		else:
			return False
def printBox(string,col1,col2):
	a = len(string)
	return (f'{col1}╔═{a*"═"}═╗\n║ {col2+string} {col1}║\n╚═{a*"═"}═╝')

def error(string,exit=True):
	if exit is None or exit is False:
		print(f"{col['R']}[{col['Y']}Error{col['R']}] {col['R']}{string}")
		return None
	else:
		print(f"{col['R']}[{col['Y']}Error{col['R']}] {col['R']}{string}")
		sys.exit(exit_status)

def success(string):
	print(f"{col['R']}[{col['G']}  ✓  {col['R']}] {col['G']}{string}")

def message(string):
	print(f"{col['R']}[{col['B']}  >  {col['R']}] {col['Y']}{string}")

def ask(string):
	string = input(f"{col['R']}[{col['Y']}  ?  {col['R']}] {col['C']}{string} : {col['G']}")
	return string

def successR(string):
	return f"{col['R']}[{col['G']}  ✓  {col['R']}] {col['G']}{string}"

def messageR(string):
	f"{col['R']}[{col['B']}  >  {col['R']}] {col['Y']}{string}"

def aPrint(string,time_test):
	for i in string :
		sys.stdout.write(i)
		sys.stdout.flush()
		time.sleep(time_test)
	print()
if __name__ == "main":
	sys.exit("You can't run script directly")
else:
	pass

##################################### CODED BY ANSH DADWAL ##################################
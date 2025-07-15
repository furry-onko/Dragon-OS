import os
import sys
import curses as c
from colorama import Fore, Back, Style, init

init(autoreset=True)

def execute() -> None:
    os.system("dir && pause")
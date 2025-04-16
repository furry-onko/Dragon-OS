import json
import sys
import os
import subprocess
from colorama import Fore, Style, Back, init
import curses as c
from time import sleep

init(autoreset=True)

def menu(stdscr):
    c.curs_set(0)
    stdscr.clear()
    stdscr.refresh()
    stdscr.keypad(True)

    menu: list = ["System", "Options", "Exit"]
    selected: int = 0

    while True:
        stdscr.clear()

        for i, item in enumerate(menu):
            x: int = i * 10
            
            if i == selected:
                stdscr.attron(c.A_REVERSE)
                stdscr.addstr(0, x, f"{item}")
                stdscr.attroff(c.A_REVERSE)
            
            else:
                stdscr.addstr(0, x, f"{item}")

        stdscr.refresh()

        key = stdscr.getch()

        if key == c.KEY_RIGHT:
            selected = (selected + 1) % len(menu)
        
        elif key == c.KEY_LEFT:
            selected = (selected - 1) % len(menu)
        
        elif key == c.KEY_ENTER or key in [10, 13]:
            break

def execute() -> None:
    c.wrapper(menu)
import json
import sys
import os
import subprocess
from colorama import Fore, Style, Back, init
from blessed import Terminal

init()

def menu():
    term: object = Terminal()
    menu_items: list = ["System", "Users", "Info", "Exit"]

    with term.fullscreen(), term.cbreak(), term.hidden_cursor():
        while True:
            print(term.clear)
            print(term.center(term.bold("Dragon-OS Configuration Menu")))

            for idx, item in enumerate(menu_items):
                if idx == current_row:
                    print(term.move_yx(term.height // 2 + idx, term.width // 2 - len(item) // 2) +
                          term.reverse(item))
                else:
                    print(term.move_yx(term.height // 2 + idx, term.width // 2 - len(item) // 2) +
                          item)

            key = term.inkey()
            if key.name == "KEY_UP" and current_row > 0:
                current_row -= 1
            elif key.name == "KEY_DOWN" and current_row < len(menu_items) - 1:
                current_row += 1
            elif key.name in ["KEY_ENTER", "KEY_RETURN"]:
                if menu_items[current_row] == "Exit":
                    break


def execute() -> None:
    menu()
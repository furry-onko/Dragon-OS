import json
import sys
import os
import subprocess
from colorama import Fore, Style, Back, init
import curses as c
from time import sleep

init(autoreset=True)

def draw_popup(stdscr, option) -> None:
    in_popup: bool = True

    lang: list = ["English", "Polski", "Español"]
    sysinfo: list = ["Creators", "Version", "Contact"]
    sysinfo_content: dict = {
        "Creators": ["Onko Aikuu (@furry_onko)", "ChatGPT", "GitHub Copilot"],
        "Version": ["Dragon OS v1.0"],
        "Contact": ["GitHub: @furry-onko", "Telegram, Instagram, etc: @furry_onko"]
    }
    bootseq: list = ["Enable FastBoot", "Disable FastBoot"]

    height, width = stdscr.getmaxyx()
    popup_width: int = 75
    popup_height: int = 10

    start_x: int = width // 2 - popup_width // 2
    start_y: int = height// 2 - popup_height// 2

    # stdscr.attron(c.A_DIM)

    for y in range(height):
        stdscr.hline(y, 0, ' ', width)
    # stdscr.attroff(A_DIM)

    selected: int = 0

    if option == "Language":
        popup_height = len(lang) + 4
        start_y = height // 2 - popup_height // 2
        popup = c.newwin(popup_height, popup_width, start_y, start_x)
        popup.box()

        popup.addstr(1, 2, option)

        for idy, item in enumerate(lang):
            y: int = 2 + idy
            popup.addstr(y, 2, f"[{'x' if idy == selected else ' '}] {item}")
        popup.refresh()

        while True:
            key = popup.getch()
            if key in [27, 10, 13]:
                stdscr.clear()
                stdscr.refresh()
                break

    elif option == "Users":
        with open('Files/config/users.json', 'r') as f:
            json_data: dict = json.load(f)
            users: dict | list = json_data["users"]
            usernames: list = [user['user_name'] for user in users]

        popup_height = len(usernames) + 4
        start_y = height // 2 - popup_height // 2
        popup = c.newwin(popup_height, popup_width, start_y, start_x)
        popup.box()

        popup.addstr(1, 2, option)

        for idy, item in enumerate(usernames):
            y: int = 2 + idy
            popup.addstr(y, 2, f"[{'x' if idy == selected else ' '}] {item}")
        popup.refresh()

        while True:
            key = popup.getch()
            if key in [27, 10, 13]:
                stdscr.clear()
                stdscr.refresh()
                break

    elif option == "System Information":
        ...
    
    elif option == "Packages":
        ...
    
    elif option == "Boot sequence":
        ...
    
    elif option == "Date / Time":
        ...
    
    elif option == "Network":
        ...
    
    elif option == "Save and exit":
        ...
    
    elif option == "Exit without saving":
        ...
    
    elif option == "Restore and exit":
        ...
    
    elif option == "Launch Dragon OS":
        ...


def draw_top_menu(stdscr, top, selected) -> None:
    for idx, item in enumerate(top):
        x = idx * 10
        if idx == selected:
            stdscr.attron(c.A_REVERSE)
            stdscr.addstr(0, x, item)
            stdscr.attroff(c.A_REVERSE)
        else:
            stdscr.addstr(0, x, item)

def draw_sub_menu(stdscr, sub, selected) -> None:
    for idy, item in enumerate(sub):
        y: int = 2 + idy
        stdscr.addstr(y, 2, f"[{'x' if idy == selected else ' '}] {item}")

def menu(stdscr):
    c.curs_set(0)
    stdscr.clear()
    stdscr.refresh()
    stdscr.keypad(True)

    top_menu: list = ["System", "Options", "Exit"]
    submenu_content: dict = {
        "System": ["Language", "Users", "System Information"],
        "Options": ["Packages", "Boot sequence", "Date / Time", "Network"],
        "Exit": ["Save and exit", "Exit without saving", "Restore and exit", "Launch Dragon OS"]
    }
    selected_top: int = 0
    selected_sub: int = 0
    in_submenu: bool = False
    in_popup: bool = False

    while True:
        stdscr.clear()

        draw_top_menu(stdscr, top_menu, selected_top)

        if in_submenu:
            submenu = submenu_content[top_menu[selected_top]]
            draw_sub_menu(stdscr, submenu, selected_sub)
        
        stdscr.refresh()
        key = stdscr.getch()

        if in_submenu:
            if key == c.KEY_UP:
                selected_sub = (selected_sub -1) % len(submenu)
            elif key == c.KEY_DOWN:
                selected_sub = (selected_sub +1) % len(submenu)
            elif key in [c.KEY_LEFT, c.KEY_RIGHT]:
                in_submenu = False
            elif key in [c.KEY_ENTER, 10, 13]:
                stdscr.clear()
                draw_popup(stdscr, submenu[selected_sub])
                stdscr.clear()
                stdscr.refresh()
                continue

        else:
            if key == c.KEY_LEFT:
                selected_top = (selected_top -1) % len(top_menu)
            elif key == c.KEY_RIGHT:
                selected_top = (selected_top +1) % len(top_menu)
            elif key in [c.KEY_DOWN, c.KEY_ENTER, 10, 13]:
                in_submenu = True
                selected_sub = 0

def execute() -> None:
    c.wrapper(menu)
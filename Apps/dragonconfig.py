import json
import sys
import os
import subprocess
import curses.textpad as ct
import curses as c
from colorama import Fore, Style, Back, init
from time import sleep

init(autoreset=True)

def draw_popup(stdscr, option) -> None:
    in_popup: bool = True
    c.start_color()
    c.init_pair(1, c.COLOR_MAGENTA, c.COLOR_BLACK)
    c.init_pair(2, c.COLOR_CYAN, c.COLOR_BLACK)
    c.init_pair(3, c.COLOR_GREEN, c.COLOR_BLACK)
    c.init_pair(4, c.COLOR_BLACK, c.COLOR_WHITE)

    are_you_sure: list = ["Yes", "No"]
    lang: list = ["English", "Polski", "Español"]
    sysinfo: list = ["Creators", "Version", "Contact"]
    sysinfo_content: dict = {
        "Creators": ["Onko Aikuu (@furry_onko)", "ChatGPT", "GitHub Copilot"],
        "Version": ["Dragon OS v1.0"],
        "Contact": ["GitHub: @furry-onko", "Telegram, Instagram, etc: @furry_onko"]
    }
    bootseq: list = ["Enable FastBoot", "Disable FastBoot"]

    user_options: list = ["Change username", "Change password", "Change account type", "Delete user", "Add a new user"]

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
        popup.keypad(True)

        while True:
            popup.clear()
            popup.box()
            popup.addstr(1, 2, option)

            for idy, item in enumerate(lang):
                y: int = 2 + idy
                popup.addstr(y, 2, f"[{'x' if idy == selected else ' '}] {item}")

            popup.refresh()

            key = popup.getch()
            if key == 27:
                stdscr.clear()
                stdscr.refresh()
                break
            
            elif key == c.KEY_DOWN:
                selected = (selected +1) % len(lang)
            
            elif key == c.KEY_UP:
                selected = (selected -1) % len(lang)

    elif option == "Users":
        with open('Files/config/users.json', 'r') as f:
            json_data: dict = json.load(f)
            users: dict | list = json_data["users"]
            usernames: list = [user['user_name'] for user in users]

        popup_height = len(usernames) + 4
        start_y = height // 2 - popup_height // 2
        popup = c.newwin(popup_height, popup_width, start_y, start_x)
        popup.keypad(True)

        while True:
            popup.clear()
            popup.box()
            popup.addstr(1, 2, option)
            
            with open("Files/config/core.json", 'r') as f:
                data: dict | list = json.load(f)
                current_user: str = data["CurrentUser"]

            for idy, item in enumerate(usernames):
                y: int = 2 + idy
                if item == current_user:
                    popup.addstr(y, 2, f"[{'x' if idy == selected else ' '}]")
                    popup.attron(c.color_pair(2))
                    popup.addstr(y, 6, f"{item} ← Current user")
                    popup.attroff(c.color_pair(2))
                else:
                    popup.addstr(y, 2, f"[{'x' if idy == selected else ' '}] {item}")
            
            popup.refresh()

            key = popup.getch()
            selected_user: str = usernames[selected]

            if key == 27:
                stdscr.clear()
                stdscr.refresh()
                break

            elif key == c.KEY_DOWN:
                selected = (selected +1) % len(usernames)

            elif key == c.KEY_UP:
                selected = (selected -1) % len(usernames)
            
            elif key in [c.KEY_ENTER, 10, 13]:
                popup.clear()
                popup.box()
                
                while True:
                    popup.addstr(1, 2, selected_user, c.color_pair(1))
                    for idy, option in enumerate(user_options):
                        y: int = 2 + idy
                        popup.addstr(y, 2, f"[{'x' if idy == selected else ' '}] {option}")
                    popup.refresh()

                    key = popup.getch()

                    if key == c.KEY_UP:
                        selected = (selected -1) % len(user_options)
                    elif key == c.KEY_DOWN:
                        selected = (selected +1) % len(user_options)
                    elif key in [c.KEY_ENTER, 10, 13]:
                        if selected == 0:
                            selected_option: int = 0
                            new_username: str = selected_user
                            edit_mode = False

                            while True:
                                popup.clear()
                                popup.box()
                                popup.addstr(1, 2, user_options[selected], c.color_pair(1))

                                textbox_win = popup.derwin(1, 30, 3, 2)

                                textbox_win.attron(c.A_NORMAL)
                                textbox_win.refresh()
                                popup.refresh()
                                textbox_win.bkgd(' ', c.color_pair(4))

                                popup.addstr(5, 2, "[Save]", c.A_REVERSE if selected_option == 1 else c.A_NORMAL)
                                popup.addstr(6, 2, "[Exit]", c.A_REVERSE if selected_option == 2 else c.A_NORMAL)
                                popup.refresh()

                                key = popup.getch()

                                if selected_option == 0:
                                    if key in [c.KEY_ENTER, 10, 13]:
                                        textbox_win.bkgd(' ', c.color_pair(4))
                                        textbox_win.refresh()
                                        textbox = ct.Textbox(textbox_win)
                                        c.curs_set(1)
                                        new_username: str = textbox.edit().strip()
                                        textbox_win.addstr(0, 0, new_username)
                                        c.curs_set(0)

                                        textbox_win.clear()
                                        textbox_win.bkgd(' ', c.color_pair(4))
                                        textbox_win.addstr(0, 0, new_username, c.color_pair(4))
                                        textbox_win.refresh

                                        selected_option = 1
                                    elif key == c.KEY_UP:
                                        selected_option = (selected_option -1) %3
                                    elif key == c.KEY_DOWN:
                                        selected_option = (selected_option +1) %3
                                    
                                    textbox_win.bkgd(' ', c.color_pair(4))
                                    textbox_win.refresh()
                                else:
                                    if key == c.KEY_UP:
                                        selected_option = (selected_option -1) %3
                                    elif key == c.KEY_DOWN:
                                        selected_option = (selected_option +1) %3
                                    elif key in [c.KEY_ENTER, 10, 13]:
                                        if selected_option == 1:
                                            with open("Files/config/users.json", 'r') as f:
                                                data: dict | list = json.load(f)
                                                
                                            for user in data['users']:
                                                if user['user_name'] == selected_user:
                                                    user['user_name'] = new_username
                                                    break

                                            with open("Files/config/users.json", 'w') as f:
                                                json.dump(data, f, indent=4)
                                                
                                            break
                                        else: break
                                            
                                            

    elif option == "System Information":
        popup_height = len(sysinfo) + 4
        start_y = height // 2 - popup_height // 2
        popup = c.newwin(popup_height, popup_width, start_y, start_x)
        popup.keypad(True)

        while True:
            popup.clear()
            popup.box()
            popup.addstr(1, 2, option, c.color_pair(1))

            for idy, item in enumerate(sysinfo):
                y: int = 2 + idy
                popup.addstr(y, 2, f"[{'x' if idy == selected else ' '}] {item}")

            popup.refresh()

            key = popup.getch()
            
            if key in [c.KEY_ENTER, 10, 13]:
                while True:
                    popup.clear()
                    popup.box()
                    popup.attron(c.color_pair(1))
                    popup.addstr(1, 2, sysinfo[selected])
                    popup.attroff(c.color_pair(1))
                    for text_id, text in enumerate(sysinfo_content[sysinfo[selected]]):
                        y: int = 2 + text_id
                        popup.addstr(y, 2, text)
                    popup.refresh()
                    key = popup.getch()
                    if key == 27: break

            elif key == 27:
                stdscr.clear()
                stdscr.refresh()
                break
            
            elif key == c.KEY_UP:
                selected = (selected -1) % len(sysinfo)
            
            elif key == c.KEY_DOWN:
                selected = (selected +1) % len(sysinfo)
    
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

        down_stripe_content: str = "⇄ Navigate on top menu        ⇅ Navigate on submenu        [Enter] Open        [Esc] Quit menu"
        down_stripe_content = down_stripe_content.ljust(c.COLS)

        try:
            stdscr.attron(c.A_REVERSE)
            stdscr.addstr(c.LINES -2, 0, down_stripe_content)
            stdscr.attroff(c.A_REVERSE)
        except: pass
        
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
# By @furry_onko

# Import packages
import json
import sys
import os
import subprocess
import curses.textpad as ct
import curses as c
from colorama import Fore, Style, Back, init
import time
from datetime import datetime as dt
from System import system as drg
import requests as req

# Init colorama
init(autoreset=True)

# Function adding options (list/tuple), title, text and control
def options(popup, title: str, options: list | tuple, control: str = None, text: list | tuple = None) -> str | None:
    # Selected option in this window
    selected_option: int = 0

    # Control + refresh loop
    while True:
        # Clear window
        popup.clear()
        # Make box around this popup
        popup.box()
        # Add title
        popup.addstr(1, 2, title, c.color_pair(1))
        
        # Check if there is a text
        if text:
            # Add text printing loop
            for i, line in enumerate(text):
                txt_y: int = 2 +i
                # Print option
                popup.addstr(txt_y, 2, line)

        # Add option d
        for idy, item in enumerate(options):
            # Y axis value changing depending on text
            y: int = (len(text) + idy + 2 if text else 2 + idy)
            # Add options having [x] when selected
            popup.addstr(y, 2, f"[{'x' if idy == selected_option else ' '}] {item}")

        # Get pressed key value
        key = popup.getch()

        # Option changinng by pressing keys
        if key == c.KEY_UP:
            selected_option = (selected_option - 1) % len(options)
        elif key == c.KEY_DOWN:
            selected_option = (selected_option + 1) % len(options)
        elif key in [c.KEY_ENTER, 10, 13]:
            popup.clear()   # Clear popup
            popup.box()     # Add a border
            popup.refresh() # Print changes
            # Returns selected option and its value
            return options[selected_option]
            break # Exit loop
        elif key == 27: # esc
            popup.clear()   # Clear popup
            popup.box()     # Add a border
            popup.refresh() # Print changes
            return # Returning nothing
            break  # Exit loop

        # Shift + Q action
        elif key == 81 and control == "q-crash":
            raise ValueError("crash-forced dragonconfig")


def info(popup, title: str, select_options: list | tuple = None, text_options: list | tuple = None) -> str | None:
    selected_option: int = 0
    y: int = 0

    while True:
        popup.clear()
        popup.box()
        popup.addstr(1, 2, title, c.color_pair(1))

        #add text
        for idy, item in enumerate(text_options):
            y = 2 + idy
            popup.addstr(y, 2, item)

        for idy, item in enumerate(select_options):
            y = 2 + idy + len(text_options)
            popup.addstr(y, 2, f"[{'x' if idy == selected_option else ' '}] {item}")

        key = popup.getch()

        if key == c.KEY_UP:
            selected_option = (selected_option - 1) % len(select_options)
        elif key == c.KEY_DOWN:
            selected_option = (selected_option + 1) % len(select_options)
        elif key in [c.KEY_ENTER, 10, 13]:
            popup.clear()
            popup.box()
            popup.refresh()
            return select_options[selected_option]
            break
        elif key == 27:
            popup.clear()
            popup.box()
            popup.refresh()
            return
            break

# Popup with options and input field that could be a password prompt
def edit_popup_field(popup, title: str, current_value: str, mask: bool = False, mask_char: str = '•') -> str | None:
    selected_option = 0
    new_value = current_value

    while True:
        popup.clear()
        popup.box()
        popup.addstr(1, 2, title, c.color_pair(1))

        # Add text popup
        textbox_win = popup.derwin(1, 30, 3, 2)
        textbox_win.clear()

        # Change color of textbox when it's selected
        if selected_option == 0:
            textbox_win.bkgd(' ', c.color_pair(4))
        else:
            textbox_win.bkgd(' ', c.color_pair(0))

        # Display value in textbox if it's in a password mode
        display_value = mask_char * len(new_value) if mask else new_value
        textbox_win.addstr(0, 0, display_value)

        # Change style to normal
        textbox_win.attron(c.A_NORMAL)

        # Refresh both textbox and popup
        textbox_win.refresh()
        popup.refresh()

        # Add Save and Exit options
        popup.addstr(5, 2, "[Save]", c.A_REVERSE if selected_option == 1 else c.A_NORMAL)
        popup.addstr(6, 2, "[Exit]", c.A_REVERSE if selected_option == 2 else c.A_NORMAL)
        popup.refresh()

        # Get key
        key = popup.getch()

        if selected_option == 0: # Textbox
            # On enter in textbox
            if key in [c.KEY_ENTER, 10, 13]:
                # Change to selected
                textbox_win.bkgd(' ', c.color_pair(4))
                textbox_win.refresh()
                # Make a textbox interaction
                textbox = ct.Textbox(textbox_win)
                c.curs_set(1) # Make a cursor visible
                # Get a stripped value from textbox interacion
                entered = textbox.edit().strip()
                c.curs_set(0) # Hide a cursor

                # After go to the next option and re-assign a value
                new_value = entered
                selected_option = 1
            elif key == c.KEY_UP:
                selected_option = (selected_option - 1) % 3
            elif key == c.KEY_DOWN:
                selected_option = (selected_option + 1) % 3
        else: # Not in a textbox
            if key == c.KEY_UP:
                selected_option = (selected_option - 1) % 3
            elif key == c.KEY_DOWN:
                selected_option = (selected_option + 1) % 3
            elif key in [c.KEY_ENTER, 10, 13]:
                # On Save option
                if selected_option == 1:
                    # Refresh everything and return
                    textbox_win.clear()
                    textbox_win.refresh()
                    popup.clear()
                    popup.box()
                    popup.refresh()
                    return new_value
                # On Exit option
                else:
                    # Refresh everything and return nothing
                    textbox_win.clear()
                    textbox_win.refresh()
                    popup.clear()
                    popup.box()
                    popup.refresh()
                    return None

# Main popup funcion
def draw_popup(stdscr, option) -> None:
    # Bool if you are in popup 
    in_popup: bool = True

    # Start color mode and add color pairs (fg - bg)
    c.start_color()
    c.init_pair(1, c.COLOR_MAGENTA, c.COLOR_BLACK)
    c.init_pair(2, c.COLOR_CYAN, c.COLOR_BLACK)
    c.init_pair(3, c.COLOR_GREEN, c.COLOR_BLACK)
    c.init_pair(4, c.COLOR_BLACK, c.COLOR_WHITE)

    # Add all options
    are_you_sure: list = ["Yes", "No"]
    lang: list = ["English", "Polski", "Español"]
    sysinfo: list = ["Creators", "Version", "Contact"]
    sysinfo_content: dict = {
        "Creators": ["Onko Aikuu (@furry_onko)", "ChatGPT", "GitHub Copilot"],
        "Version": ["Dragon OS v1.0"],
        "Contact": ["GitHub: @furry-onko", "Telegram, Instagram, etc: @furry_onko"]
    }
    bootseq: list = ["Enable FastBoot", "Disable FastBoot", "About FastBoot"]
    abt_fastboot: list = ["FastBoot lets you skip installing all packages.", "Packages will be updated once in a month"]

    user_options: list = ["Change username", "Change password", "Change account type", "Remove user", "Add a new user", "Choose user"]

    # Get window width and height
    height, width = stdscr.getmaxyx()

    # Assign popup size
    popup_width: int = 75
    popup_height: int = 10

    # Add popup placing (to make it appear in the middle)
    start_x: int = width // 2 - popup_width // 2
    start_y: int = height// 2 - popup_height// 2

    # Screen thingy i forgot what it does ;_;
    for y in range(height):
        stdscr.hline(y, 0, ' ', width)

    # Selected submenu values
    selected: int = 0
    sub_selected: int = 0
    selected_option: int = 0

    # Popup for language changing
    if option == "Language":
        # Popup height changing according to amount of options
        popup_height = len(lang) + 4

        # Popup start coordinates (to place it in the middle)
        start_y = height // 2 - popup_height // 2

        # Make a popup
        popup = c.newwin(popup_height, popup_width, start_y, start_x)
        
        # Make popup detect arrow keys
        popup.keypad(True)

        # Add options 
        selected_language: str = options(popup, option, lang)

        # Get currently used language
        with open("Files/config/register.json", 'r') as f:
            system_lang: str = json.load(f)['*'][0]['SYSTEM'][1]['SystemLang']
        
        # If popup returned any language
        if selected_language:
            system_lang = selected_language

            # Add info popups according to selected language
            if selected_language == "English":
                options(popup, "Notice", ["OK"], text=("Language works only on the system UI,", "not dragonconfig."))
            
            elif selected_language == "Polski":
                options(popup, "Uwaga", ["OK"], text=("Wybrany język działa tylko w warstwie zewnętrznej systemu,", "nie w dragonconfig."))

            elif selected_language == "Español":
                options(popup, "Notar", ["OK"], text=("El idioma solo funciona en la interfaz de usuario del sistema,", "no en dragonconfig."))

    # Popup for user management options
    elif option == "Users":
        # Load users' data
        with open('Files/config/users.json', 'r') as f:
            json_data: dict = json.load(f)
            users: dict | list = json_data["users"]
            usernames: list = [user['user_name'] for user in users]

        # Popup placement
        popup_height = len(usernames) + 4
        start_y = height // 2 - popup_height // 2
        popup = c.newwin(popup_height, popup_width, start_y, start_x)
        popup.keypad(True)

        # Refresh loop
        while True:
            # Popup refresh + add title
            popup.clear()
            popup.box()
            popup.addstr(1, 2, option)
            
            # Load current user data
            with open("Files/config/core.json", 'r') as f:
                current_user: str = json.load(f)["CurrentUser"]

            # Print every username to edit
            for idy, item in enumerate(usernames):
                y: int = 2 + idy

                # Add information about selected user
                if item == current_user:
                    popup.addstr(y, 2, f"[{'x' if idy == selected else ' '}]")
                    popup.addstr(y, 6, f"{item} ← Current user", c.color_pair(2))
                else:
                    popup.addstr(y, 2, f"[{'x' if idy == selected else ' '}] {item}")
            
            popup.refresh()

            # Keys control
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

                """ potential repetition
                with open('Files/config/users.json', 'r') as f:
                    json_data: dict = json.load(f)
                    users: dict | list = json_data["users"]
                    usernames: list = [user['user_name'] for user in users]
                """

                while True:
                    # Add user control popup
                    popup.addstr(1, 2, selected_user, c.color_pair(1))

                    # Disable options that could destroy root
                    if selected_user == "root":
                        for idy, option in enumerate(user_options[4:]):
                            y: int = 2 + idy
                            popup.addstr(y, 2, f"[{'x' if idy == sub_selected else ' '}] {option}")
                        popup.refresh()

                    # Options for every user
                    else:
                        for idy, option in enumerate(user_options):
                            y: int = 2 + idy
                            popup.addstr(y, 2, f"[{'x' if idy == sub_selected else ' '}] {option}")
                        popup.refresh()

                    key = popup.getch()
                    
                    # Controls for selected root and every other account
                    if key == c.KEY_UP:
                        if selected_user == "root":
                            sub_selected = (sub_selected -1) % 2
                        else:
                            sub_selected = (sub_selected -1) % len(user_options)
                    elif key == c.KEY_DOWN:
                        if selected_user == "root":
                            sub_selected = (sub_selected +1) % 2
                        else:
                            sub_selected = (sub_selected +1) % len(user_options)
                    elif key in [c.KEY_ENTER, 10, 13]:
                        if selected_user == "root":
                            sub_selected += 3

                        # Option for changing user name
                        if sub_selected == 0:
                            # Get username
                            new_username = edit_popup_field(popup, "Change Username", selected_user)
                            
                            if new_username:
                                # Load users
                                with open("Files/config/users.json", 'r') as f:
                                    data: dict | list = json.load(f)
                                
                                # Change selected user's name
                                for user in data['users']:
                                    if user['user_name'] == selected_user:
                                        user['user_name'] = new_username
                                        break

                                # Set value
                                with open("Files/config/users.json", 'w') as f:
                                    json.dump(data, f, indent=4)
                            # Exit if empty username
                            else: break

                        # Option for changing user password
                        elif sub_selected == 1:
                            # Load data
                            with open("Files/config/users.json", 'r') as f:
                                data: dict | list = json.load(f)

                            # Get user's password
                            for user in data['users']:
                                if user['user_name'] == selected_user:
                                    display_password: str = user['user_passw'] or ""
                                    break

                            # Add popup for changing password
                            new_password = edit_popup_field(popup, "Change Password", display_password, mask=True)
                            
                            # Set password    
                            for user in data['users']:
                                if user['user_name'] == selected_user:
                                    user['user_passw'] = new_password
                                    break

                            # Save a new password to file
                            with open("Files/config/users.json", 'w') as f:
                                json.dump(data, f, indent=4)

                        # Option for changing account type
                        elif sub_selected == 2:
                            # Get account type from popup
                            account_type: str = options(popup, option, ["Admin", "User"])
                            with open("Files/config/users.json", 'r') as f:
                                data: dict | list = json.load(f)
                            
                            # Change user's account type
                            for user in data['users']:
                                if user['user_name'] == selected_user:
                                    try:
                                        user['account_type'] = account_type.lower()
                                        break
                                    except: break

                            # Save to file
                            with open("Files/config/users.json", 'w') as f:
                                json.dump(data, f, indent=4)

                        # Option for removing user
                        elif sub_selected == 3:
                            # Get confirmation from popup
                            delete_check = options(popup, "Remove user", ["No", "Yes"])
                            
                            # If returned "Yes"
                            if delete_check == "Yes":
                                # Load users
                                with open("Files/config/users.json", 'r') as f:
                                    data: dict | list = json.load(f)
                                
                                # Delete user
                                for index, user in enumerate(data['users']):
                                    if user['user_name'] == selected_user:
                                        del data['users'][index]
                                
                                # Save to file
                                with open("Files/config/users.json", 'w') as f:
                                    json.dump(data, f, indent=4)
                        
                        elif sub_selected == 4:
                            ...

                    # Exit popup on esc
                    elif key == 27:
                        popup.clear()
                        popup.box()
                        popup.refresh()
                        break

    # System information interaction
    elif option == "System Information":

        # Place popup in the middle
        popup_height = len(sysinfo) + 4
        start_y = height // 2 - popup_height // 2
        popup = c.newwin(popup_height, popup_width, start_y, start_x)
        popup.keypad(True)

        # Popup loop
        while True:
            # Make popup + add title
            popup.clear()
            popup.box()
            popup.addstr(1, 2, option, c.color_pair(1))

            # Add information category
            for idy, item in enumerate(sysinfo):
                y: int = 2 + idy
                popup.addstr(y, 2, f"[{'x' if idy == selected else ' '}] {item}")

            popup.refresh()

            key = popup.getch()
            
            # After selecting an option
            if key in [c.KEY_ENTER, 10, 13]:
                # Information text
                while True:
                    # Make popup + add title
                    popup.clear()
                    popup.box()
                    popup.addstr(1, 2, sysinfo[selected], c.color_pair(1))
                    
                    # Add text
                    for text_id, text in enumerate(sysinfo_content[sysinfo[selected]]):
                        y: int = 2 + text_id
                        popup.addstr(y, 2, text)
                    
                    # Exit on esc
                    popup.refresh()
                    key = popup.getch()
                    if key == 27: break

            # Exit to menu on esc
            elif key == 27:
                stdscr.clear()
                stdscr.refresh()
                break
            
            elif key == c.KEY_UP:
                selected = (selected -1) % len(sysinfo)
            
            elif key == c.KEY_DOWN:
                selected = (selected +1) % len(sysinfo)

    # System packages control
    elif option == "Packages":
        # Make a window
        popup = c.newwin(popup_height, popup_width, start_y, start_x)
        popup.keypad(True)

        # Get system packages options
        result = options(popup, option, ["Package List", "Add Package", "Remove Package"])
        
        # Package list
        if result == "Package List":
            while True:
                # Load all packages' data
                with open("Files/config/register.json", 'r') as f:
                    packages: dict | list = json.load(f)["*"][0]["SYSTEM"][0]["Packages"]

                # Add a window containing packages
                packages_popup = c.newwin(popup_height, popup_width, start_y, start_x)
                packages_popup.keypad(True)

                package_names: list = []

                # Add package name and enabled / disabled value
                for package in packages:
                    package_names.append(
                        package['package_name']
                    )
                    if package['enabled']:
                        is_enabled = 'Enabled'
                    else:
                        is_enabled = 'Disabled'

                # Get a package name from a popup
                selected_package = options(packages_popup, result, [*package_names, 'Back'])

                # If selected package is not back
                if selected_package != 'Back':
                    # Iterate through packages
                    for package in packages:
                        # Get info about a package
                        if package['package_name'] == selected_package:
                            # Make a box displaying every information about 
                            package_info_box = c.newwin(popup_height, popup_width, start_y, start_x)
                            package_info = info(packages_popup, selected_package, ['Attributes'], [
                                is_enabled,
                                f"Name: {package['package_name']}",
                                f"Description: {package['package_desc']}",
                                f"Version: {package['version']}",
                                f"Creator: {package['creator']}",
                            ])

                            # Option for package attributes' informations
                            if package_info == "Attributes":
                                attr_names: list = []

                                for attr in package['attributes']:
                                    if attr == "SYS": attr_names.append("System critical")
                                    elif attr == "ND": attr_names.append("Cannot delete")
                                    elif attr == "DOM": attr_names.append("Immutable")
                                    elif attr == "PKG": attr_names.append("Package")
                                    else: attr_names.append("Unknown attribute")

                                package_attr_box = c.newwin(popup_height, popup_width, start_y, start_x)
                                package_attributes = info(package_attr_box, f"{selected_package} - Attributes", ['Back'], [*attr_names])
                else: break

        elif result == "Add Package":
            package_name: str = edit_popup_field(popup, "Package name", result)
            if package_name:
                package_list_raw: str = req.get("https://raw.githubusercontent.com/furry-onko/furry-onko/refs/heads/main/dragon/package-list.json", headers={"User-Agent": "Mozilla/5.0"})
                package_list: dict = package_list_raw.json()["Packages"]
                package_names: list = []

                for index, package in enumerate(package_list):
                    package_names.append(
                        package[0]
                    )
                
                if package_name in package_names:
                    # ckeck if package is in installed
                    for package_name_check in package['package_name']:
                        if package_name == package_name_check:
                            err_popup = c.newwin(popup_height, popup_width, start_y, start_x)
                            options(err_popup, f"Package \"{package_name}\" is already installed.", ["OK"])
                    
                    pkg_found = c.newwin(popup_height, popup_width, start_y, start_x)
                    options(pkg_found, f"Package {package_name} found", ["OK"])
                
                else:
                    err_popup = c.newwin(popup_height, popup_width, start_y, start_x)
                    options(err_popup, f"Package \"{package_name}\" not found", ["OK"])
                

    elif option == "Boot sequence":
        ...
    
    elif option == "Date / Time":
        in_date: bool = True
        sel_date_opt: int = 0
        sel_time_opt: int = 0
        sel_exit_opt: int = 0

        popup = c.newwin(popup_height, popup_width, start_y, start_x)
        popup.keypad(True)
    
        now = dt.now()
        current_hour: int = now.hour
        current_min: int = now.minute
        current_day: int = now.day
        current_month: int = now.month
        current_year: int = now.year

        while True:
            popup.addstr(1, 2, option, c.color_pair(1))
            popup.box()
            popup.refresh()

            time: list = [current_hour, current_min]
            date: list = [current_day, current_month, current_year]
            datetime_exit: list = ["Save", "Exit"]
            datetime_list: list = [date, time]

            for idy, y_item in enumerate(datetime_list):
                y: int = 2 + idy

                for idx, x_item in enumerate(y_item):
                    x: int = (idx +1) * 2
                    popup.addstr(y, x, str(x_item))

            key = popup.getch()
            if key == 27: break
    
    elif option == "Network":
        ...
    
    elif option == "Save and exit":
        ...
    
    elif option == "Exit without saving":
        popup = c.newwin(popup_height, popup_width, start_y, start_x)
        popup.keypad(True)
        ews = options(popup, f"{option} - Are you sure?", ["Yes", "No"], control="q-crash")
        if ews == "Yes": raise ValueError("exit")
        else:
            stdscr.clear()
            stdscr.refresh()

    elif option == "Restore and exit":
        ...
    
    elif option == "Launch Dragon OS":
        with open("Files/config/core.json", 'r') as f:
            data: dict | list = json.load(f)
        
        system_installation: bool = data['SystemInstallation']
        if system_installation: raise ValueError("system execute")
        else: raise ValueError("system install")

def draw_top_menu(stdscr, top, selected) -> None:
    # Enumerate through options on top menu
    for idx, item in enumerate(top):
        x = idx * 10
        # Highlight if selected
        if idx == selected:
            stdscr.attron(c.A_REVERSE)
            stdscr.addstr(0, x, item)
            stdscr.attroff(c.A_REVERSE)
        else:
            stdscr.addstr(0, x, item)

def draw_sub_menu(stdscr, sub, selected) -> None:
    # Add options from top menu
    for idy, item in enumerate(sub):
        y: int = 2 + idy
        stdscr.addstr(y, 2, f"[{'x' if idy == selected else ' '}] {item}")

# Init main window function
def menu(stdscr):
    # Disable cursor
    c.curs_set(0)

    # Refresh bottom menu
    stdscr.clear()
    stdscr.refresh()

    # Enable arrow keys
    stdscr.keypad(True)

    # Top menu options
    top_menu: list = ["System", "Options", "Exit"]
    
    # Submenu options
    submenu_content: dict = {
        "System": ["Language", "Users", "System Information"],
        "Options": ["Packages", "Boot sequence", "Date / Time", "Network"],
        "Exit": ["Save and exit", "Exit without saving", "Restore and exit", "Launch Dragon OS"]
    }

    # Selected options list 
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

        # Add bottom stripe
        down_stripe_content: str = "⇄ Navigate on top menu        ⇅ Navigate on submenu        [Enter] Open        [Esc] Quit menu"
        down_stripe_content = down_stripe_content.ljust(c.COLS)

        try:
            stdscr.attron(c.A_REVERSE)
            stdscr.addstr(c.LINES -2, 0, down_stripe_content)
            stdscr.attroff(c.A_REVERSE)
        except: pass
        
        stdscr.refresh()
        key = stdscr.getch()

        # Submenu controls
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

        # Top menu con
        else:
            if key == c.KEY_LEFT:
                selected_top = (selected_top -1) % len(top_menu)
            elif key == c.KEY_RIGHT:
                selected_top = (selected_top +1) % len(top_menu)
            elif key in [c.KEY_DOWN, c.KEY_ENTER, 10, 13]:
                in_submenu = True
                selected_sub = 0

# Init menu
def execute() -> None:
    c.wrapper(menu)
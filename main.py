# By Onko Aikuu :3
import os
import sys
import subprocess

def printLogo() -> None:    
    print("⢗⣝⢮⡳⣝⢮⡳⣝⢮⡳⣝⢮⡳⣝⢮⢯⡺⣝⢮⢯⡺⣝⣞⢽⣪⢟⡮⡯⣞⢽⢵⣫⢯⢞⡽⣝⣞⢽⢝⣞⡽⣝⢽⡺⣽⡹⣝⡽⣝⣵".center(os.get_terminal_size().columns))
    print("⢕⢗⡳⣝⢮⢳⣹⡪⡳⣝⢮⡳⣝⢮⢯⡺⣝⢮⣫⡳⡽⣕⣗⢯⢞⡵⡯⣞⡵⡯⣳⣳⡫⡯⣞⣗⢽⣝⢽⣺⡺⡽⡵⣻⣺⡺⣵⡻⣺⣺".center(os.get_terminal_size().columns))
    print("⡺⣝⢞⢮⡳⣝⢮⡺⣝⢮⡳⣝⢮⢯⡺⣝⢮⣳⡳⡽⣝⣞⢮⢯⣫⢾⢝⡮⡯⣞⣗⢗⡽⣝⣞⢮⣗⢗⡯⣞⣞⡽⣝⣞⣞⣞⡵⣯⣳⣳".center(os.get_terminal_size().columns))
    print("⡞⡮⣫⢞⢞⢮⡳⣝⢮⡳⣝⡮⡯⣳⢽⡺⣵⡳⡮⣙⠺⢪⢯⣳⡹⢽⢝⡾⣝⣞⡮⡯⡯⣞⡮⣗⣗⢯⢯⣞⣞⢾⢵⣳⣳⡳⣽⣺⣺⣪".center(os.get_terminal_size().columns))
    print("⢮⡫⡮⣫⣫⡳⣝⢮⣳⢽⣕⢯⢯⣞⣗⠽⡮⡯⡯⡯⡯⣦⣈⡘⠺⠳⣍⠚⢗⢷⢽⢽⣝⣮⣻⡺⡮⡯⣗⣗⣗⣯⣻⣺⣪⢯⣞⣞⣞⣮".center(os.get_terminal_size().columns))
    print("⢕⢯⡫⣞⢮⢞⡚⠓⠓⠓⢹⡽⠁⢳⡳⡯⡶⣬⣉⠋⠫⠗⣯⡷⣷⣔⡤⡀⡀⠙⠹⢵⣳⣳⣳⢽⢽⢽⣺⣺⣺⣺⣺⣺⣺⢽⣺⣺⣺⣺".center(os.get_terminal_size().columns))
    print("⡹⣕⢯⢞⡽⣕⢯⣫⢏⣯⣳⣫⢯⢗⡯⡯⣻⣺⣞⣿⣶⣦⣄⡈⡉⠙⠻⠿⣾⣵⣰⡀⠄⠁⠋⠫⢯⣻⣺⣺⢞⣞⣞⣞⢾⣝⣞⣞⣞⢾".center(os.get_terminal_size().columns))
    print("⡪⣗⢯⡳⣝⡮⡯⣺⢝⡮⣺⢼⢝⣵⣋⣋⣉⣉⣉⣉⣁⣉⣟⣿⣷⣧⣣⣢⣠⣀⢉⠙⠛⠻⢶⣦⡄⣀⠈⢞⣯⣗⣗⡯⣗⣗⣗⡷⡽⡽".center(os.get_terminal_size().columns))
    print("⢽⣪⢗⡯⣳⢝⣞⡵⡯⣺⡳⣽⣽⣾⣻⣯⡿⠏⠻⢟⣿⣭⣉⡉⡈⡉⡙⡛⡙⠛⠛⠛⠛⠒⠊⠺⡷⣖⡿⠛⠚⠚⠚⠙⠚⠚⢑⡿⡽⣽".center(os.get_terminal_size().columns))
    print("⣳⠳⠫⣞⡗⠯⠞⣞⡽⠾⢿⢻⣷⡟⠉⢀⢀⢄⣮⣾⢿⢽⣻⣟⡷⠿⠿⠿⠿⠿⠻⠟⢷⢗⣧⡷⣮⣯⢴⣤⣦⣴⣤⡔⢀⡴⡽⣞⡯⡷".center(os.get_terminal_size().columns))
    print("⣳⣲⣲⡳⣳⡲⣲⢽⢵⣲⣽⢿⡷⠁⢔⢑⣬⣾⢗⡿⣿⣝⣝⡛⣻⣷⢷⡷⣷⣻⡾⠋⠁⠀⡀⠉⠛⠺⢟⣷⣻⣞⣷⣳⢯⡯⣯⢷⣻⢽".center(os.get_terminal_size().columns))
    print("⢮⣺⢼⡺⣕⢯⣳⡫⣗⡷⣿⡛⠁⢌⢢⣾⢿⣺⡳⠁⠀⠉⢳⣿⣻⢽⢽⡽⠋⡁⣄⣆⣶⣼⢾⡾⣮⣖⣔⢄⠅⠛⢚⡽⣯⢯⡷⣻⣞⣯".center(os.get_terminal_size().columns))
    print("⣳⡳⣝⢮⢯⡳⣳⢽⢵⣿⣻⡇⠌⣢⣾⡿⣝⢟⠻⠷⣦⣤⣿⣳⢽⢽⣕⣶⣻⣻⢽⡽⣳⡽⡽⣞⣗⣯⢯⢇⣱⢾⡽⡯⣯⠏⣯⣗⣗⡷".center(os.get_terminal_size().columns))
    print("⣗⢽⡺⣝⡵⣫⢾⢕⣿⢾⣻⠎⣸⣯⣿⣻⢪⠮⠊⠀⠀⢸⡾⣺⢽⣳⣳⣳⢗⡯⣟⣞⡷⡯⣟⣗⣟⣞⣷⣻⢽⣻⣺⢯⢯⠇⣗⣷⡳⡯".center(os.get_terminal_size().columns))
    print("⢷⢝⡾⣕⢯⣳⡫⡯⣾⣿⣻⡼⣿⠹⣾⣗⣿⡶⠶⠶⠶⠾⡯⡯⣟⣞⣗⡯⣯⢯⢷⣳⢯⢿⢵⣻⢮⣗⣷⣫⡯⡷⣯⣻⡝⠀⣿⢮⢯⢯".center(os.get_terminal_size().columns))
    print("⢽⢵⣫⢾⢝⡮⣞⡽⣽⡾⣯⣟⠣⢀⢻⣽⣞⢖⡀⡀⠀⣀⣽⢯⣟⢾⢵⣻⢽⢽⣻⣺⢯⣻⡽⣞⣟⣞⣾⣺⢽⣽⣺⢾⠁⢠⣿⢽⢽⢽".center(os.get_terminal_size().columns))
    print("⣹⢵⣳⡫⣗⡽⡮⣻⣺⢿⣯⢿⣻⡆⡂⣻⣷⢫⣧⡶⠟⠋⠀⠈⣫⡿⡽⣽⢽⣻⣺⢾⢽⣳⢯⣗⣟⡾⣺⢾⢽⣺⢾⠋⡀⣾⢯⢯⢯⣻".center(os.get_terminal_size().columns))
    print("⢮⣳⡳⡽⣕⢯⢯⢞⣞⣿⣽⣟⣷⣻⡔⢄⢿⣿⣳⣝⢆⠀⢠⡾⠏⠀⠉⣯⠟⠾⣽⡽⡽⠾⣽⠚⠁⠈⢯⣯⣟⠃⡟⠠⣼⡿⡽⡽⣽⣺".center(os.get_terminal_size().columns))
    print("⢳⡳⡽⣝⣞⡽⡽⣝⣞⢞⣞⣯⣷⢿⡽⣖⢆⠻⣽⣾⣝⣾⣻⢕⡄⡀⣸⡟⠀⠀⢸⡇⠀⠀⢿⣇⢄⢢⣢⣷⡏⢀⢐⣾⣻⢽⢽⢽⣺⢾".center(os.get_terminal_size().columns))
    print("⣝⡽⣝⣞⣞⣞⡽⣺⢮⡻⡮⣻⣽⢿⡽⣯⢿⡌⡊⡻⢽⣟⣮⣗⡽⣲⡿⣪⢦⡂⢸⣗⡲⡰⣜⣿⡼⣿⢽⡾⢐⣰⡾⣟⢾⢽⢽⡽⣞⣟".center(os.get_terminal_size().columns))
    print("⡳⣽⣺⣺⣺⣺⣺⣳⣫⢯⠯⣳⣝⢿⣻⣽⢷⣻⡄⠢⡑⢌⢛⠿⣻⣿⣽⡾⣷⣽⢾⡷⣷⡿⠿⢚⢩⣰⡿⢡⣵⡿⡽⡽⡽⣽⢽⢾⣽⣺".center(os.get_terminal_size().columns))
    print("⢽⡺⡦⣦⣢⢦⣤⣤⢼⣻⢄⡼⣺⣝⢿⣻⣿⡽⣟⣿⢶⢶⢴⣁⠢⡐⡩⢉⠍⡚⣫⣫⣷⢾⡽⣷⢿⣝⣼⡿⣻⣺⢽⢯⣻⡽⡽⣯⢾⣺".center(os.get_terminal_size().columns))
    print("⢯⢯⢯⣞⢾⣝⣞⢾⢽⣺⢽⣝⢷⣝⢷⣝⡷⣟⣟⣿⣻⣿⣻⣯⡿⣷⢮⣶⣟⣿⣻⣽⡯⣿⣽⣟⣯⣟⣗⡯⣗⡯⣟⣽⣳⣻⡽⡯⣯⢷".center(os.get_terminal_size().columns))
    print("⢽⢽⢵⡳⡯⣞⢾⢽⢽⣺⢽⣺⣳⣝⣗⣗⡯⣟⡾⡮⣗⡯⣟⡷⣿⣻⣯⣷⢿⢾⢯⡷⣻⣽⣺⣳⣳⣗⡯⣯⢯⣟⡽⣞⣗⣯⢯⡿⣽⣻".center(os.get_terminal_size().columns))
    print("⡽⣝⣗⡯⡯⡯⡯⡯⣗⡯⣗⣗⣗⣗⣗⣗⡯⣗⡯⡯⣗⡿⡽⣽⣝⣗⡷⣽⢽⢽⣳⣻⣳⣗⣯⣞⣗⡷⡯⡿⡽⣞⣯⣟⡾⡽⡯⣟⣗⣟".center(os.get_terminal_size().columns))
    print()
    print("    ____                               ____  _____".center(os.get_terminal_size().columns))
    print("   / __ \_________ _____ _____  ____  / __ \/ ___/".center(os.get_terminal_size().columns))
    print("  / / / / ___/ __ `/ __ `/ __ \/ __ \/ / / /\__ \ ".center(os.get_terminal_size().columns))
    print(" / /_/ / /  / /_/ / /_/ / /_/ / / / / /_/ /___/ / ".center(os.get_terminal_size().columns))
    print("/_____/_/   \__,_/\__, /\____/_/ /_/\____//____/  ".center(os.get_terminal_size().columns))
    print("                 /____/                           ".center(os.get_terminal_size().columns))
    print("\n")

if os.name == "nt":
    os.system("cls")
    os.system("py -m pip install --upgrade pip")
    os.chdir(
        os.path.dirname(__file__)
    )

    os.system("title Dragon OS - Loading Libraries...")
    os.system("cls")
    printLogo()

else:
    os.system("clear")
    os.system("python3 -m pip install --upgrade pip --break-system-packages")
    os.chdir(
        os.path.dirname(__file__)
    )

    print("\033]0;Dragon OS - Loading Libraries...\007")
    os.system("clear")
    printLogo()


print(
    "Loading... "
    .center(
        os.get_terminal_size().columns
    )
)

dependencies: list = ["colorama", "keyboard", "requests", "bcrypt"]

if os.name == "nt": dependencies.append("windows-curses")

# sys.executable

for i, package in enumerate(dependencies):
    try:
        if os.name == "nt":
            os.system(f"title Dragon OS - Loading Libraries... {i +1}/{len(dependencies)}")
        else:
            print(f"\033]0;Dragon OS - Loading Libraries... {i +1}/{len(dependencies)}")

        print(f"[\033[34mINFO\033[0m]      Loading libraries {i +1}/{len(dependencies)} ({package})", end="\r")
        subprocess.call([sys.executable, "-m", "pip", "install", package, "--break-system-packages"], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
        print(" " * 50, end="\r")

    except:
        print(f"[\033[0;31mERROR\033[0m]      Error loading library: {package}")

print("[\033[34mINFO\033[0m]      Loading libraries - Done")

if os.name == "nt":
    os.system("title Dragon OS - Loading Libraries... - Done")
else:
    print("\033]0;Dragon OS - Loading Libraries... - Done")

print("[[\033[34mINFO\033[0m]      Importing libraries", end="\r")

if os.name == "nt":
    os.system("title Dragon OS - Importing Libraries...")
else:
    print("\033]0;Dragon OS - Importing Libraries...\007")

from Apps import dragoninstall as drg_inst
from Apps import datetime as dt
from Apps import dragonconfig as dc
from Apps import tests
from System import system as drg
from System import crash
from colorama import Fore, Style, Back, init
import keyboard
import requests
import bcrypt
import json

print(" " * 50, end="\r")
print("[\033[34mINFO\033[0m]      Importing libraries - Done")

if os.name == "nt":
    os.system("title Dragon OS - Importing Libraries... - Done")
else:
    print("\033]0;Dragon OS - Importing Libraries... - Done\007")

init(autoreset=True)

user: str = ""
with open("Files/config/core.json", "r") as f:
    user: str = json.load(f)["CurrentUser"]

def terminal() -> None:
    global user
    os.system("cls" if os.name == "nt" else "clear")

    def clear() -> None:
        os.system("cls" if os.name == "nt" else "clear")

    keyboard.add_hotkey("ctrl+l", clear)

    while True:
        print(f"${user}: ", end="")
        cmd: str = input().lower()

        if cmd == "dragoninstall":
            drg_inst.execute()
            break
        
        if cmd == "dragonconfig":
            try: dc.execute()
            except ValueError as x:
                full_exception: str = x
                x: tuple = str(full_exception).split(' ')

                if x[0] == "exit":
                    print("")

                elif x[0] == "crash-forced":
                    crash.crash(x)

                elif x[0] == "system":
                    if x[1] == "install":
                        drg_inst.execute()
                        break
                    else:
                        drg.execute()
                        break
                
                else: print(f"{Fore.YELLOW}Incorrect exception raised: {full_exception}\n")

        elif cmd == "exit":
            print("Exiting...")
            break
        
        elif cmd == "test":
            tests.test()
            
        elif cmd == "datetime":
            dt.execute()

        elif cmd == "dragon":
            drg.execute()
            break

        elif cmd == "user":
            print(f"Current user: {user}")
            newuser: str = input("Enter user name: ").strip()
            password: str = input("Enter password: ")
            # hashed: str = bcrypt.hashpw(password, bcrypt.salt())

            if newuser == user:
                print("You are already logged in as this user.")

            elif newuser in ["", " "]:
                print("")

            else:
                with open("Files/config/users.json", "r", encoding="utf-8") as f:
                    data: dict | list = json.load(f)
                    users: dict = data["users"]
                    
                    for _user in users:
                        if user == newuser:
                            print("User not changed")
                            break

                        if _user['user_name'] == newuser and _user['user_passw'] == password:
                            user = newuser
                            print(f"User changed to {user}")
                            os.system(f"title Dragon OS - ${user}")
                            with open("Files/config/core.json", "r+") as f:
                                data: dict | list = json.load(f)
                                data['CurrentUser'] = user
                                f.seek(0)
                                json.dump(data, f, indent=4)
                                f.truncate()
                                f.close()
                            break
                f.close()


        elif cmd == "ls":
            print("dragoninstall", end="  ")
            print("datetime", end="  ")
            print("dragon", end="  ")
            print("user", end="  ")
            print("dragonconfig")

if os.name == "nt":
    os.system(f"title Dragon OS - ${user}")
else:
    print(f"\033]0;Dragon OS - ${user}\007")

terminal()

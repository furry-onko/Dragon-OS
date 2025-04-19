# By Onko Aikuu :3
import os
import sys
os.system("cls" if os.name == "nt" else "clear")
os.system("py -m pip install subprocess")
import subprocess

os.chdir(os.getcwd())
os.system("title Dragon OS - Loading Libraries...")
os.system("cls" if os.name == "nt" else "clear")

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
print("┳┓┳┓┏┓┏┓┏┓┳┓".center(os.get_terminal_size().columns))
print("┃┃┣┫┣┫┃┓┃┃┃┃".center(os.get_terminal_size().columns))
print("┻┛┛┗┛┗┗┛┗┛┛┗".center(os.get_terminal_size().columns))

print("Loading... ".center(os.get_terminal_size().columns))

dependencies: list = ["colorama", "keyboard", "requests", "json", "os", "sys", "bcrypt", "time", "windows-curses"]

for i, package in enumerate(dependencies):
    try:
        os.system(f"title Dragon OS - Loading Libraries... {i +1}/{len(dependencies)}")
        print(f"[\033[34mINFO\033[0m]      Loading libraries {i +1}/{len(dependencies)} ({package})", end="\r")
        subprocess.call([sys.executable, "-m", "pip", "install", package], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
        print(" " * 50, end="\r")

    except:
        print(f"[\033[0;31mERROR\033[0m]      Error loading library: {package}")

os.system("title Dragon OS - Loading Libraries... - Done")

os.system("title Dragon OS - Importing Libraries...")
from Apps import dragoninstall as drg_inst
from Apps import datetime as dt
from Apps import dragonconfig as dc
from System import dragon as drg
from colorama import Fore, Style, Back, init
import keyboard
import requests
import bcrypt
import json
os.system("title Dragon OS - Importing Libraries... - Done")

init(autoreset=True)


user: str = ""
with open("Files/config/core.json", "r") as f:
    data: dict | list = json.load(f)
    user = data["CurrentUser"]
    f.close()

def download() -> None:
    try:
        download_core_link: str = "https://raw.githubusercontent.com/furry-onko/Dragon-OS/refs/heads/main/Files/config/core.json"
        download_users_link: str = "https://raw.githubusercontent.com/furry-onko/Dragon-OS/refs/heads/main/Files/config/users.json"
        download_dragoninstall_link: str = "https://raw.githubusercontent.com/furry-onko/Dragon-OS/refs/heads/main/Apps/dragoninstall.py" 

        download_core_response = requests.get(download_core_link)
        download_core_response.raise_for_status()

        download_users_response = requests.get(download_users_link)
        download_users_response.raise_for_status()

        download_dragoninstall_response = requests.get(download_dragoninstall_link)
        download_dragoninstall_response.raise_for_status()

        os.makedirs("Files/config", exist_ok=True)
        os.chdir("Files/config")
        if not os.path.exists("core.json") and not os.path.exists("users.json"):        
            with open("core.json", "wb") as f:
                f.write(download_core_response.content)
                f.close()
        
            with open("users.json", "wb") as f:
                f.write(download_users_response.content)
                f.close()
        
        
        os.chdir("../..")
        
        if not os.path.exists("Apps/dragoninstall.py"):
            os.makedirs("Apps", exist_ok=True)
            os.chdir("Apps")
            with open("dragoninstall.py", "wb") as f:
                f.write(download_dragoninstall_response.content)
                f.close()
    except Exception as x:
        print(f"ERROR DOWNLOADING FILES: {x}")
        print("PLEASE CHECK YOUR INTERNET CONNECTION")
        print("OR CHECK YOUR FIREWALL SETTINGS")
        # exit(-3)

def terminal() -> None:
    global user
    os.system("cls" if os.name == "nt" else "clear")

    def clear() -> None:
        os.system("cls" if os.name == "nt" else "clear")
        print(f"${user}: ", end="")

    keyboard.add_hotkey("ctrl+l", clear)

    while True:
        print(f"${user}: ", end="")
        cmd: str = input().lower()

        if cmd == "dragoninstall":
            drg_inst.execute()
            break
        
        if cmd == "dragonconfig":
            dc.execute()
            break

        elif cmd == "exit":
            print("Exiting...")
            break
            
        elif cmd == "datetime":
            dt.execute()
            break

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

os.system(f"title Dragon OS - ${user}")
download()
terminal()
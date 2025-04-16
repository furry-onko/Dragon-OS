import json
import sys
import os
import subprocess

os.chdir(os.getcwd())
os.system("title Dragon OS - Loading Libraries...")
os.system("cls" if os.name == "nt" else "clear")

print("""
⢗⣝⢮⡳⣝⢮⡳⣝⢮⡳⣝⢮⡳⣝⢮⢯⡺⣝⢮⢯⡺⣝⣞⢽⣪⢟⡮⡯⣞⢽⢵⣫⢯⢞⡽⣝⣞⢽⢝⣞⡽⣝⢽⡺⣽⡹⣝⡽⣝⣵
⢕⢗⡳⣝⢮⢳⣹⡪⡳⣝⢮⡳⣝⢮⢯⡺⣝⢮⣫⡳⡽⣕⣗⢯⢞⡵⡯⣞⡵⡯⣳⣳⡫⡯⣞⣗⢽⣝⢽⣺⡺⡽⡵⣻⣺⡺⣵⡻⣺⣺
⡺⣝⢞⢮⡳⣝⢮⡺⣝⢮⡳⣝⢮⢯⡺⣝⢮⣳⡳⡽⣝⣞⢮⢯⣫⢾⢝⡮⡯⣞⣗⢗⡽⣝⣞⢮⣗⢗⡯⣞⣞⡽⣝⣞⣞⣞⡵⣯⣳⣳
⡞⡮⣫⢞⢞⢮⡳⣝⢮⡳⣝⡮⡯⣳⢽⡺⣵⡳⡮⣙⠺⢪⢯⣳⡹⢽⢝⡾⣝⣞⡮⡯⡯⣞⡮⣗⣗⢯⢯⣞⣞⢾⢵⣳⣳⡳⣽⣺⣺⣪
⢮⡫⡮⣫⣫⡳⣝⢮⣳⢽⣕⢯⢯⣞⣗⠽⡮⡯⡯⡯⡯⣦⣈⡘⠺⠳⣍⠚⢗⢷⢽⢽⣝⣮⣻⡺⡮⡯⣗⣗⣗⣯⣻⣺⣪⢯⣞⣞⣞⣮
⢕⢯⡫⣞⢮⢞⡚⠓⠓⠓⢹⡽⠁⢳⡳⡯⡶⣬⣉⠋⠫⠗⣯⡷⣷⣔⡤⡀⡀⠙⠹⢵⣳⣳⣳⢽⢽⢽⣺⣺⣺⣺⣺⣺⣺⢽⣺⣺⣺⣺
⡹⣕⢯⢞⡽⣕⢯⣫⢏⣯⣳⣫⢯⢗⡯⡯⣻⣺⣞⣿⣶⣦⣄⡈⡉⠙⠻⠿⣾⣵⣰⡀⠄⠁⠋⠫⢯⣻⣺⣺⢞⣞⣞⣞⢾⣝⣞⣞⣞⢾
⡪⣗⢯⡳⣝⡮⡯⣺⢝⡮⣺⢼⢝⣵⣋⣋⣉⣉⣉⣉⣁⣉⣟⣿⣷⣧⣣⣢⣠⣀⢉⠙⠛⠻⢶⣦⡄⣀⠈⢞⣯⣗⣗⡯⣗⣗⣗⡷⡽⡽
⢽⣪⢗⡯⣳⢝⣞⡵⡯⣺⡳⣽⣽⣾⣻⣯⡿⠏⠻⢟⣿⣭⣉⡉⡈⡉⡙⡛⡙⠛⠛⠛⠛⠒⠊⠺⡷⣖⡿⠛⠚⠚⠚⠙⠚⠚⢑⡿⡽⣽
⣳⠳⠫⣞⡗⠯⠞⣞⡽⠾⢿⢻⣷⡟⠉⢀⢀⢄⣮⣾⢿⢽⣻⣟⡷⠿⠿⠿⠿⠿⠻⠟⢷⢗⣧⡷⣮⣯⢴⣤⣦⣴⣤⡔⢀⡴⡽⣞⡯⡷
⣳⣲⣲⡳⣳⡲⣲⢽⢵⣲⣽⢿⡷⠁⢔⢑⣬⣾⢗⡿⣿⣝⣝⡛⣻⣷⢷⡷⣷⣻⡾⠋⠁⠀⡀⠉⠛⠺⢟⣷⣻⣞⣷⣳⢯⡯⣯⢷⣻⢽
⢮⣺⢼⡺⣕⢯⣳⡫⣗⡷⣿⡛⠁⢌⢢⣾⢿⣺⡳⠁⠀⠉⢳⣿⣻⢽⢽⡽⠋⡁⣄⣆⣶⣼⢾⡾⣮⣖⣔⢄⠅⠛⢚⡽⣯⢯⡷⣻⣞⣯
⣳⡳⣝⢮⢯⡳⣳⢽⢵⣿⣻⡇⠌⣢⣾⡿⣝⢟⠻⠷⣦⣤⣿⣳⢽⢽⣕⣶⣻⣻⢽⡽⣳⡽⡽⣞⣗⣯⢯⢇⣱⢾⡽⡯⣯⠏⣯⣗⣗⡷
⣗⢽⡺⣝⡵⣫⢾⢕⣿⢾⣻⠎⣸⣯⣿⣻⢪⠮⠊⠀⠀⢸⡾⣺⢽⣳⣳⣳⢗⡯⣟⣞⡷⡯⣟⣗⣟⣞⣷⣻⢽⣻⣺⢯⢯⠇⣗⣷⡳⡯
⢷⢝⡾⣕⢯⣳⡫⡯⣾⣿⣻⡼⣿⠹⣾⣗⣿⡶⠶⠶⠶⠾⡯⡯⣟⣞⣗⡯⣯⢯⢷⣳⢯⢿⢵⣻⢮⣗⣷⣫⡯⡷⣯⣻⡝⠀⣿⢮⢯⢯
⢽⢵⣫⢾⢝⡮⣞⡽⣽⡾⣯⣟⠣⢀⢻⣽⣞⢖⡀⡀⠀⣀⣽⢯⣟⢾⢵⣻⢽⢽⣻⣺⢯⣻⡽⣞⣟⣞⣾⣺⢽⣽⣺⢾⠁⢠⣿⢽⢽⢽
⣹⢵⣳⡫⣗⡽⡮⣻⣺⢿⣯⢿⣻⡆⡂⣻⣷⢫⣧⡶⠟⠋⠀⠈⣫⡿⡽⣽⢽⣻⣺⢾⢽⣳⢯⣗⣟⡾⣺⢾⢽⣺⢾⠋⡀⣾⢯⢯⢯⣻
⢮⣳⡳⡽⣕⢯⢯⢞⣞⣿⣽⣟⣷⣻⡔⢄⢿⣿⣳⣝⢆⠀⢠⡾⠏⠀⠉⣯⠟⠾⣽⡽⡽⠾⣽⠚⠁⠈⢯⣯⣟⠃⡟⠠⣼⡿⡽⡽⣽⣺
⢳⡳⡽⣝⣞⡽⡽⣝⣞⢞⣞⣯⣷⢿⡽⣖⢆⠻⣽⣾⣝⣾⣻⢕⡄⡀⣸⡟⠀⠀⢸⡇⠀⠀⢿⣇⢄⢢⣢⣷⡏⢀⢐⣾⣻⢽⢽⢽⣺⢾
⣝⡽⣝⣞⣞⣞⡽⣺⢮⡻⡮⣻⣽⢿⡽⣯⢿⡌⡊⡻⢽⣟⣮⣗⡽⣲⡿⣪⢦⡂⢸⣗⡲⡰⣜⣿⡼⣿⢽⡾⢐⣰⡾⣟⢾⢽⢽⡽⣞⣟
⡳⣽⣺⣺⣺⣺⣺⣳⣫⢯⠯⣳⣝⢿⣻⣽⢷⣻⡄⠢⡑⢌⢛⠿⣻⣿⣽⡾⣷⣽⢾⡷⣷⡿⠿⢚⢩⣰⡿⢡⣵⡿⡽⡽⡽⣽⢽⢾⣽⣺
⢽⡺⡦⣦⣢⢦⣤⣤⢼⣻⢄⡼⣺⣝⢿⣻⣿⡽⣟⣿⢶⢶⢴⣁⠢⡐⡩⢉⠍⡚⣫⣫⣷⢾⡽⣷⢿⣝⣼⡿⣻⣺⢽⢯⣻⡽⡽⣯⢾⣺
⢯⢯⢯⣞⢾⣝⣞⢾⢽⣺⢽⣝⢷⣝⢷⣝⡷⣟⣟⣿⣻⣿⣻⣯⡿⣷⢮⣶⣟⣿⣻⣽⡯⣿⣽⣟⣯⣟⣗⡯⣗⡯⣟⣽⣳⣻⡽⡯⣯⢷
⢽⢽⢵⡳⡯⣞⢾⢽⢽⣺⢽⣺⣳⣝⣗⣗⡯⣟⡾⡮⣗⡯⣟⡷⣿⣻⣯⣷⢿⢾⢯⡷⣻⣽⣺⣳⣳⣗⡯⣯⢯⣟⡽⣞⣗⣯⢯⡿⣽⣻
⡽⣝⣗⡯⡯⡯⡯⡯⣗⡯⣗⣗⣗⣗⣗⣗⡯⣗⡯⡯⣗⡿⡽⣽⣝⣗⡷⣽⢽⢽⣳⣻⣳⣗⣯⣞⣗⡷⡯⡿⡽⣞⣯⣟⡾⡽⡯⣟⣗⣟
""")
print("""
┳┓┳┓┏┓┏┓┏┓┳┓
┃┃┣┫┣┫┃┓┃┃┃┃
┻┛┛┗┛┗┗┛┗┛┛┗
""")

print("Loading...")

os.system("title Dragon OS - Loading Libraries... (1/)")
subprocess.call([sys.executable, "-m", "pip", "install", "colorama"], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
os.system("title Dragon OS - Loading Libraries... (2/)")
subprocess.call([sys.executable, "-m", "pip", "install", "keyboard"], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
os.system("title Dragon OS - Loading Libraries... (3/)")
subprocess.call([sys.executable, "-m", "pip", "install", "requests"], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
os.system("title Dragon OS - Loading Libraries... (4/)")
subprocess.call([sys.executable, "-m", "pip", "install", "json"], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
os.system("title Dragon OS - Loading Libraries... (5/)")
subprocess.call([sys.executable, "-m", "pip", "install", "os"], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
os.system("title Dragon OS - Loading Libraries... (6/)")
subprocess.call([sys.executable, "-m", "pip", "install", "sys"], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
os.system("title Dragon OS - Loading Libraries... (7/)")
subprocess.call([sys.executable, "-m", "pip", "install", "bcrypt"], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
os.system("title Dragon OS - Loading Libraries... (8/)")
subprocess.call([sys.executable, "-m", "pip", "install", "asciimatics"], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
os.system("title Dragon OS - Loading Libraries... (9/)")
subprocess.call([sys.executable, "-m", "pip", "install", "time"], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)


os.system("title Dragon OS - Loading Libraries... - Done")

os.system("title Dragon OS - Importing Libraries...")
import blessed
from Apps import dragoninstall as drg_inst
from Apps import datetime as dt
from Apps import dragonconfig as dc
from System import dragon as drg
from colorama import Fore, Style, Back, init
import keyboard
import requests
import hashlib
import bcrypt
os.system("title Dragon OS - Importing Libraries... - Done")

init(autoreset=True)


user: str = "root"

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
    except:
        print("ERROR DOWNLOADING FILES")
        print("PLEASE CHECK YOUR INTERNET CONNECTION")
        print("OR CHECK YOUR FIREWALL SETTINGS")
        exit(-3)

def terminal() -> None:
    global user
    os.system("cls" if os.name == "nt" else "clear")

    def clear():
        os.system("cls" if os.name == "nt" else "clear")
        print(f"${user}: ", end="", flush=True)

    keyboard.add_hotkey("ctrl+l", clear)

    while True:
        print(f"${user}: ", end="", flush=True)
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
                            break

        elif cmd == "ls":
            print("dragoninstall", end="  ")
            print("datetime", end="  ")
            print("dragon", end="  ")
            print("user", end="  ")
            print("dragonconfig")

os.system(f"title Dragon OS - ${user}")
download()
terminal()
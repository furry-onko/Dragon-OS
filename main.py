import json
import sys
import os
import subprocess

os.system("cls" if os.name == "nt" else "clear")
print("Please Wait...")

subprocess.call([sys.executable, "-m", "pip", "install", "colorama"], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
subprocess.call([sys.executable, "-m", "pip", "install", "keyboard"], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
subprocess.call([sys.executable, "-m", "pip", "install", "requests"], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)

from Apps import dragoninstall as drg_inst
from Apps import datetime as dt
from System import dragon as drg
from colorama import Fore, Style, Back, init
import keyboard
import requests

init(autoreset=True)


user: str = "root"

def download() -> None:
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
    with open("core.json", "wb") as f:
        f.write(download_core_response.content)
        f.close()
    
    with open("users.json", "wb") as f:
        f.write(download_users_response.content)
        f.close()
    
    os.chdir("../..")
    
    os.makedirs("Apps", exist_ok=True)
    os.chdir("Apps")
    with open("dragoninstall.py", "wb") as f:
        f.write(download_dragoninstall_response.content)
        f.close()

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

        if cmd == "dragoninstall": drg_inst.execute()
        
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

            if newuser == user:
                print("You are already logged in as this user.")

            elif newuser in ["", " "]:
                print("")

            else:
                with open("Files/config/users.json", "r", encoding="utf-8") as f:
                    data = json.load(f)
                    if newuser.lower() in [user.lower() for user in data["users"]]:
                        user = newuser
                        print(f"User changed to {user}")
                    else:
                        print("USER NOT FOUND")

        elif cmd == "ls":
            print("dragoninstall", end="  ")
            print("datetime", end="  ")
            print("dragon", end="  ")
            print("user")

download()
terminal()
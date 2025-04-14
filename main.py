# Basic commands for using the json library:
# 1. Load JSON data from a string: json_data = json.loads(json_string)
# 2. Dump JSON data to a string: json_string = json.dumps(data_dict)
# 3. Load JSON data from a file: with open('file.json', 'r') as f: data = json.load(f)
# 4. Write JSON data to a file: with open('file.json', 'w') as f: json.dump(data_dict, f)
# 5. Pretty print JSON data: print(json.dumps(data_dict, indent=4))

from Apps import dragoninstall as drg_inst
from Apps import datetime as dt

from System import dragon as drg
import colorama as c
import json
import sys
import os
import keyboard
user: str = "root"

c.init(autoreset=True)

def terminal():
    global user
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
                try:
                    with open("Files/config/users.json", "r", encoding="utf-8") as f:
                        data = json.load(f)
                        if newuser.lower() in [user.lower() for user in data["users"]]:
                            user = newuser
                            print(f"User changed to {user}")
                        else:
                            print("USER NOT FOUND")

                except:
                    print("ERROR. CONFIG FILE NOT FOUND. PLEASE INSTALL YOUR SYSTEM")

        elif cmd == "ls":
            print("dragoninstall", end="  ")
            print("datetime", end="  ")
            print("dragon", end="  ")
            print("user", end="  ")

os.system("cls" if os.name == "nt" else "clear")
terminal()
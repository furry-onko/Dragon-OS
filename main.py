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
import file

user: str = "root"

c.init(autoreset=True)

def terminal():
    while True:
        cmd: str = input(f"{user}: ").lower()

        if cmd == "dragoninstall": drg_inst.execute()
        
        elif cmd == "exit":
            print("Exiting...")
            break
            
        elif cmd == "datetime":dt.execute()
        elif cmd == "dragon": drg.execute()

        elif cmd == "user":
            print(f"Current user: {user}")
            newuser: str = input("Enter new user: ")
            if newuser == user:
                print("You are already logged in as this user.")

        elif cmd == "ls":
            print("dragoninstall", end="  ")
            print("datetime", end="  ")
            print("dragon", end="  ")
            print("user", end="  ")
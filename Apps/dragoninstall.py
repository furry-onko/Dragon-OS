import os, sys
import json
import colorama
from colorama import Fore, Style, Back, init
from Apps import dragonconfig as dconf

init(autoreset=True)

def checkInstallation() -> bool:
    try:
        with open("Files/config/core.json", "r", encoding='utf-8') as f:
            json_data = json.load(f)
            system_installation: bool = json_data['SystemInstallation']
            f.close()
            return system_installation

    except FileNotFoundError:
        with open("Files/config/core.json", "w", encoding='utf-8') as f:
            json_data = {"SystemInstallation": False}
            json.dump(json_data, f)
            f.close()
            return False

def beginInstallation():
    def info(text: str | int, end="\n"):
        print(f"[{Fore.BLUE + Style.BRIGHT}INFO{Style.RESET_ALL}]       {text}", end=f"{end}")

    info("Creating folders.", end="")
    try:
        os.chdir("..")
        os.makedirs("Files")
        os.chdir("Files")
        os.makedirs("config")
        os.makedirs("ini")
        os.chdir("../..")
        print(" - Done")
    except Exception as e:
        print(f" - Error: {e}")

    info("Creating config files. ", end="")
    try:
        os.chdir('..')
        with open("Files/config/users.json", "w") as f:
            data = {"users": ["root"]}
            json.dump(data, f)
            f.close()
        print(" - Done")
    except Exception as e:
        print(f" - Error: {e}")
    

def execute():
    is_installed: bool = checkInstallation()
    if is_installed == True:
        print(Fore.GREEN + "System already installed.", end=" ")
        print("(", end="")
        print(Fore.BLACK + Style.BRIGHT + "Type 'dragon' to run the system.", end="")
        print(")")
    else:
        dconf.execute()
        beginInstallation()

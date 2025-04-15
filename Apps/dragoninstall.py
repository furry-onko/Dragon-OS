import os, sys
import json
import colorama
from colorama import Fore, Style, Back, init

init(autoreset=True)

def checkInstallation() -> bool:
    os.chdir('../..')
    try:
        with open("Files/config/core.json", "r", encoding='utf-8') as f:
            json_data = json.load(f)
            system_installation: bool = json_data['SystemInstallation']
            return system_installation
            f.close()

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
    except:
        print(" - Done")


    info("Creating config files. ", end="")
    try:
        os.chdir('..')
        with open("Files/config/users.json", "w") as f:
            data = {"users": ["root"]}
            json.dump(data, f)
            f.close()
        os.chdir('Apps')
    except:
        pass
    

def execute():
    is_installed: bool = checkInstallation()
    if is_installed:
        print(Fore.GREEN + "System already installed.", end=" ")
        print("(", end="")
        print(Fore.BLACK + Style.BRIGHT + "Type 'dragon' to run the system.", end="")
        print(")")
    else:
        beginInstallation()
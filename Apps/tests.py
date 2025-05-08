import json
from pprint import pprint
from colorama import Fore, Style, init
init(autoreset=True)

def test():
    with open("Files/config/register.json", 'r') as f:
        packages: dict = json.load(f)["*"][0]["SYSTEM"][0]["Packages"]

    for package in packages:
        print(f"Name: {package['package_name']}")
        print(f"Description: {package['package_desc']}")
        print(f"Version: {package['version']}")
        print(f"Creator: {package['creator']}")
        if package['enabled']: print(f"{Fore.GREEN + Style.BRIGHT}Enabled")
        else: print(f"{Fore.RED + Style.BRIGHT}Disabled")
        for attr in package['attributes']:
            if attr == "SYS": print("System critical", end=" ")
            elif attr == "ND": print("Cannot delete", end=" ")
            elif attr == "DOM": print("Immutable", end=" ")
            elif attr == "PKG": print("Package", end=" ")
            else: print("Unknown attribute")
        print()
import os

def crash(code: list) -> None:
    os.system("cls" if os.name == "nt" else "clear")

    raised: str = code[1]
    code: str = code[0]

    os.system("color 9F")
    print("    ____                               ____  _____".center(os.get_terminal_size().columns))
    print("   / __ \_________ _____ _____  ____  / __ \/ ___/".center(os.get_terminal_size().columns))
    print("  / / / / ___/ __ `/ __ `/ __ \/ __ \/ / / /\__ \ ".center(os.get_terminal_size().columns))
    print(" / /_/ / /  / /_/ / /_/ / /_/ / / / / /_/ /___/ / ".center(os.get_terminal_size().columns))
    print("/_____/_/   \__,_/\__, /\____/_/ /_/\____//____/  ".center(os.get_terminal_size().columns))
    print("                 /____/                           ".center(os.get_terminal_size().columns))

    print("\n" * 2)

    os.system("color 9F")
    print("A code exception has occured".center(os.get_terminal_size().columns))

    os.system("color 9F")
    print(f"Exception: {code}".center(os.get_terminal_size().columns))
    print(f"Raised by: {raised}".center(os.get_terminal_size().columns))
    print("\n" * 3)

    os.system("color 9F")
    print("Press any key to continue.".center(os.get_terminal_size().columns))
    print("\n")

    os.system("color 9F")
    os.system("pause >nul")

    os.system("color 07")
    os.system("py main.py")
    exit(-1)
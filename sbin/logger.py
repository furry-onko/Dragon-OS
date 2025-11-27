import os
from time import gmtime, strftime
import dsr.share.termUtil.colors as c

class LogJournal:
    def __init__(self, name: str, who: str = "") -> object:
        creation_time: str = strftime("%Y-%m-%d %H:%M:%S", gmtime())

        # Shadowing prevention
        if name in os.listdir("var/logs/"):
            c.error("Failed to create a log journal.")
            return

        self.location: str = f"var/logs/{name}.log"
        self.name: str = name
        self.who: str = who
        
        # Create file
        with open(f"{name}.log", "w") as f:
            f.write(f"Log name: {name}\n")
            f.write(f"Created: {creation_time}\n")
            f.write(f"{'-' * 50}\n")

    def log(self, message: str, who: str = self.who) -> None:
        time: str = strftime("%Y-%m-%d %H:%M:%S", gmtime())

        with open(self.location, "a") as f:
            if who.strip() == "":
                f.write(f"{time} | {message}\n")
            else:
                f.write(f"{time} [{who}] {message}\n")

def systemLog(message: str, who: str = "SYSTEM") -> None:
    time: str = strftime("%Y-%m-%d %H:%M:%S", gmtime())
    
    with open("var/logs/dragon.log", "w") as f:
        f.write("Dragon System Log\n")
        f.write("-" * 50)

    with open("var/logs/dragon.log", "a") as f:
        f.write(f"{time} [{who}] {message}\n")
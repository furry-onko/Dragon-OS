import os, sys
from boot import get_dev

def checkRoot() -> None:
	path: str = os.path.dirname(__file__) + "/.."
	folders: list = [name for name in os.listdir(path) if os.path.isdir(os.path.join(path, name))]
	folders = sorted(folders)
	req_folders: tuple = (".git", "bin", "boot", "const", "dev", "dsr", "home", "reg", "root", "sbin", "sys", "var")

	if len(folders) < len(req_folders):
		print("\033[0;31mError IERR_1: Number of folders in root directory are not equal to number of folders that are expected")
		exit("IERR_1")

	if set(req_folders) in set(folders):
		print("\033[0;31mError IERR_2: Unexpected folder names")
		exit("IERR_2")

	get_dev.start()

def start() -> None:
	print("\033[0;35mStarting Dragon OS\033[0m")

	if os.geteuid() != 0:
		print("\033[0;31mError IERR_0: System must be started using sudo\033[0m")
		exit("IERR_0")
	checkRoot()

if __name__ == "__main__":
	start()
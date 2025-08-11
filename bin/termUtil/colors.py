def info(text: str, desc: bool = False) -> None:
	if text:
		if desc:
			print(f"[\033[0;34mINFO\033[0m] {text}")
		else:
			print(f"\033[0;34m{text}\033[0m")
	else:
		print("")

def warn(text: str, desc: bool = False) -> None:
	if text:
		if desc:
			print(f"[\033[1;33mWARN\033[0m] {text}")
		else:
			print(f"\033[1;33m{text}\033[0m")
	else:
		print("")

def error(text: str, desc: bool = False) -> None:
	if text:
		if desc:
			print(f"[\033[0;31mERROR\033[0m] {text}")
		else:
			print(f"\033[0;31m{text}\033[0m")
	else:
		print("")

def crit(text: str, desc: bool = False) -> None:
	if text:
		if desc:
			print(f"[\033[0;35mCRITICAL\033[0m] {text}")
		else:
			print(f"\033[0;35m{text}\033[0m")
	else:
		print("")
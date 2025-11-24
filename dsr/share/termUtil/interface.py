# Squeak squeak, mf! :3
from typing import Callable
from dsr.share.termUtil.colors as clr
import copy

# Empty function to be executed (fallback)
def nullFn() -> None:
	pass

# Await input from user
def awaitInput (
	display_text: str = "",
	error: Callable[[], None] = nullFn
) -> str:
	user_input: str = ""
	
	while True:
		user_input = input(display_text)
		if len(user_input.strip()) == 0:
			error()
		else: break
	
	return user_input

# Ordered List
def ordList(
	*options: list[str],
	**additionals: dict
) -> None:
	opt_count: int = len(options)

	if opt_count == 0:
		return

	if additionals.get("reverse", False) == True:
		reversed_options: list = copy.deepcopy(options)[::-1]

		for i in range(opt_count, 0, -1):
			if additionals.get("char", False):
				print(f"{i}{additionals.get('char').strip()} {reversed_options[i-1]}")
			else:
				print(f"{i}. {reversed_options[i-1]}")

	else:
		for i in range(0, opt_count, 1):
			if additionals.get("char"):
				print(f"{i+1}{additionals.get('char').strip()} {options[i]}")
			else:
				print(f"{i+1}. {options[i]}")

# Unordered list
def unordList(
	*options: list[str],
	char: str = ""
) -> None:
	options = list(options)
	opt_count: int = len(options)
	i: int = 0

	while i < opt_count:
		if char.strip():
			print(f"{char.strip()} {options[i]}")
		else:
			print(f"- {options[i]}")

		i += 1

def snakeList(
	title: str,
	*options: list[str]
) -> None:
	options = list(options)
	opt_count: int = len(options) -1
	i: int = 0

	if opt_count == 0:
		return

	print(title)
	while i < opt_count:
		print(f"|- {options[i]}")
		i += 1

	print(f"\\- {options[i]}")

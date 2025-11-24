# User Manager
# Onko Aikuu (@furry_onko) 2025
import configparser as cp
import dsr.share.termUtil.colors as clr
import copy

class UserControl:
	@staticmethod
	def addUser() -> None:
		...

	@staticmethod
	def remUser() -> None:
		...

	@staticmethod
	def hideUser() -> None:
		...

	@staticmethod
	def modUser() -> None:
		...

	@staticmethod
	def listCmds() -> None:
		print("Commands:")
		print("|- add - Add a new user")
		print("|- remove - Remove user")
		print("|- hide - Hide user")
		print("|- modify - Modify user")
		print("|- help - Show the help page")
		print("\\- exit - Quit")

def compareUsers():
	...

def userControl(userObjects: list[dict]) -> None:
	cmd_inp: str = ""
	print("Type \"help\" to get all commands.")
	
	while True:
		cmd_inp = input("usermanager> ")
		
		match cmd_inp.strip().lower():
			case "add": UserControl.addUser()
			case "remove": UserControl.remUser()
			case "hide": UserControl.hideUser()
			case "modify": UserControl.modUser()
			case "help": UserControl.listCmds()
			case "exit": exit(0)
			case _: clr.warn("Unknown operation")

def main() -> None:
	# Init parser
	parseObj: object = cp.ConfigParser()
	parseObj.read("const/USERS.ini")

	# Exit if no users in /const/USERS.ini
	users: list[str] = parseObj.sections()
	users2: list[str] = copy.deepcopy(users)
	if len(users) == 0:
		clr.crit("No users found in /const/USERS.ini", True)
		exit(1)

	# Get users
	userObjects: list[dict] = []
	for user in users:
		try:
			userObjects.append (
				{
					"user_name": user,
					"disp_name": parseObj[user]["disp_name"]
				}
			)
		except KeyError:
			clr.error(f"Malformed user definition for user \"{user}\". Missing \"disp_name\" key.", True)
			users2.remove(user)
		except Exception:
			clr.error(f"An unknown error has occured.")
	users = copy.deepcopy(users2)
	
	# User Control Section
	if len(users) == 0:
		clr.crit("No correct user definition found in /const/USERS.ini", True)
		exit(1)

	userControl(userObjects)
if __name__ == '__main__': main()
import configparser as cfp
from boot import init
import os

if __name__ == "__main__":
	os.chdir(os.path.dirname(__file__))
	
	parser: cfp.ConfigParser = cfp.ConfigParser(allow_no_value=True)
	parser.read("reg/BOOT.cfg")

	skip_package_checking: int = parser["FastBoot"]["skip_package_checking"]
	skip_system_update_checking: int = parser["FastBoot"]["skip_system_update_checking"]
	show_system_logo: int = parser["FastBoot"]["show_system_logo"]

	if parser["FastBoot"]["skip_init"] == 0:
		init.start()
	
	if parser["FastBoot"]["skip_root_checking"] == 0:
		init.checkRoot()
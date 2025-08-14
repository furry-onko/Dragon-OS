# Dragon OS Documentation

## Description
Dragon OS is a small minimalistic OS written in python and being able to execute terminal apps and TUI apps written in Python.
The DragonKernel can execute programs written in DragonScript, a syntax being similar to Assembly, but it does not support everything that Assembly can do and it doesn't fully work like this language


## Booting stages
1. Launching
	- Starting the system should be **ONLY** done from `launch.py` **OR** `launch.sh`
	- Always use `sudo` command to start.
	- To avoid making `__pycache__` folders, potentially breaking a part of a system, you can do these things:
		* Type `sudo pythonX -B launch.py` (replace X with a number of your python command, like `python3`)
		* Use `launch.sh` to do everything for you

2. Initializing
	1) Checking for privilleges. You must run this with root privilleges.
	2) Counting folders in your root directory. System will stop when the amount of folders is lesser than the amount of folders that are required. See <ins>**Dragon root directory**</ins> to see more
	3) Checking folder names. System will stop when there will be any missing required folders
	These steps can be omitted when in `/reg/BOOT.cfg` the value `FastBoot/skip_root_ckecking` is set to `1`

3. Getting and checking devices
	1) Loading `.ddev` files from `/dev`
	2) Checking for USB devices and assigning new USB devices
	3) Checking for SATA/PCI devices and assigning new SATA/PCI devices
	4) Checking for RAM, assigning new RAM pieces and checking for amount of it
	5) Checking for CPU devices and assigning new CPU devices
	6) Checking for any disks and assigning new disks and checking free space
	7) Checking for monitor(s) and assigning new monitor(s)
	These steps can be omitted when in `/reg/BOOT.cfg` the value `FastBoot/skip_init` is set to `1`
	To stop halting system and exitting to the terminal, you can change any value in `/reg/BOOT.cfg` in `halt_when_X_404` where `X` stands for either: `usb`, `sata_pci`, `cpu`
	To stop halting system when RAM and disk are too low change `halt_when_X_too low` where `X` stands for either: `ram`, `disk_space`
	To stop halting on any internal error, set `halt_on_internal_error` to `0`

## Dragon root directory
The system 
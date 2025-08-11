import usb.core
import usb.util
import json
from bin import colors as c
from boot import dragonKernel

devices: list = []

dev_vendors: list = []
dev_names: list = []
dev_serial_numbers: list = []

def getDevData(dev_path: str) -> dict:
	with open(dev_path, "r") as dev:
		return json.load(dev)

def addDev(dev_path: str, dev_data: dict) -> None:
	with open(dev_path, "w") as dev:
		json.dump(dev_data, dev, indent=4)

def assignDevices() -> None:
	for dev in devices:
		dev_data: dict = getDevData(dev)
		if not dev_data["name"] in dev_names and dev_data["vendor"] in dev_vendors and dev_data["serial_number"] in dev_serial_numbers:
			addDev(f"dev/USB{len(devices) +1}.ddev", dev_data)
			initDevices()

def initDevices() -> None:
	usb_devs: list = os.path.listdir("dev")
	for usb_dev_name in usb_devs:
		if not usb_dev_name.startswith("USB"):
			usb_devs.remove(usb_dev_name)

	devices = usb_devs
	usb_dev_nums: int = len(usb_devs)

	if usb_dev_nums == 0:
		c.warn("System could not find any USB device.", True)
		dragonKernel.terminal()
	else:
		assignDevices()

def start() -> None:
	try:
		devices = usb.core.find(find_all=True)
	except Exception as x:
		c.error(f"IERR_X: Error finding USB devices: {x}")
		exit("IERR_X")

	initDevices()
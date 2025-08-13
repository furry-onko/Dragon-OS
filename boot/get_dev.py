import usb.core
import usb.util
import os, sys, json
from boot import dragonKernel
from bin.termUtil import colors as c

dev_dir: list = []

usb_dev_obj: list = []
usb_dev_vendors: list = []
usb_dev_names: list = []
usb_dev_serials: list = []

class DevActions:

	@staticmethod
	def loadDevDirectory() -> list: #>-Load `dev` folder
		dev_content: list = []
		for dev in os.listdir("dev"):
			if dev.endswith(".ddev"):
				dev_content.append(dev)
			else:
				try: os.remove(os.path.join("dev", dev))
				except Exception as x:
					c.warn(f"Error while deleting device {dev}. Reason: {x}")
		return dev_content

	@staticmethod
	def filterDev(dev_type: str) -> list: #>-Filter devices by type
		dev_content: list = DevActions.loadDevDirectory()
		for dev in dev_content:
			if not dev.startswith(dev_type):
				dev_content.remove(dev)
		return dev_content

	@staticmethod
	def retDevInfo(dev: str) -> dict: #>-Returns dict with dev data or {}
		with open(dev, 'r') as d:
			dev_data: dict = json.load(d)
			if set(dev_data.keys()) == set(["vendor", "name", "serial"]):
				return dev_data
			else:
				return {}

class UsbActions(DevActions):

	@staticmethod
	def countConnectedUsb() -> int: #>-Counting connected USB devices
		global usb_dev_obj
		usb_dev_obj = list(usb.core.find(find_all=True))

		return len(usb_dev_obj)

	@staticmethod
	def checkUsb() -> bool: #>-Checks whether or not system could find any saved or pluged in USB device
		if UsbActions.countConnectedUsb() == 0 \
		and DevActions.filterDev("USB") == []:
			return False
		else:
			return True

	@staticmethod
	def retUsbDevInfo(usb_obj: object) -> dict: #>-Returns dict with device info
		try:
			vendor: str = usb.util.get_string(usb_obj, usb_obj.iManufacturer) or "Unknown vendor"
		except:
			vendor: str = "Unknown vendor"

		try:
			name: str = usb.util.get_string(usb_obj, usb_obj.iProduct) or "Unknown name"
		except:
			name: str = "Unknown name"

		try:
			serial: str = usb.util.get_string(usb_obj, usb_obj.iSerialNumber) or "Unknown serial number"
		except:
			serial: str = "Unknown serial number"

		return {"vendor": vendor, "name": name, "serial": serial}

	@staticmethod
	def addUsbFile(file_content: dict, file_id: int) -> None:
		with open(f"dev/USB{file_id}.ddev", 'w') as dev:
			json.dump(file_content, dev, indent=4)
		c.info(f"Added USB device USB{file_id}.ddev", True)

	@staticmethod
	def compareUsbDevs() -> None:
	    global usb_dev_obj
	    usb_dev_obj = list(usb.core.find(find_all=True))

	    if len(usb_dev_obj) == 0 and DevActions.filterDev("USB") == []:
	        c.warn("System could not find any USB device. System halted", True)
	        dragonKernel.console(throw="nousbdev")
	        return

	    existing_files = DevActions.filterDev("USB")
	    existing_numbers = []
	    for f in existing_files:
	        try:
	            num = int(f[3:-5])
	            existing_numbers.append(num)
	        except ValueError:
	            continue

	    saved_devices = [
	        DevActions.retDevInfo(os.path.join("dev", f))
	        for f in existing_files
	    ]

	    for usb_obj in usb_dev_obj:
	        info = UsbActions.retUsbDevInfo(usb_obj)
	        if info not in saved_devices:
	            current_file = 1
	            while current_file in existing_numbers:
	                current_file += 1
	            existing_numbers.append(current_file)
	            UsbActions.addUsbFile(info, current_file)

def start() -> None:
	UsbActions.compareUsbDevs()
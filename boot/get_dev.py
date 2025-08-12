import usb.core
import usb.util
import os, sys, json
from bin.termUtil import colors as c
from boot import dragonKernel

usb_dev_obj:			list = []
usb_dev_vendors:		list = []
usb_dev_names:			list = []
usb_dev_serial_numbers: list = []
usb_dev_data:			list = []

pci_dev_obj: 			list = []
pci_dev_vendors: 		list = []
pci_dev_names: 			list = []
pci_dev_serial_numbers: list = []

stor_dev_obj: 			list = []
stor_dev_vendors: 		list = []
stor_dev_names: 		list = []
stor_dev_serial_numbers:list = []

cpu_dev_obj:			list = []
cpu_dev_vendors:		list = []
cpu_dev_names:			list = []
cpu_dev_serial_numbers: list = []

class UsbActions:
	@staticmethod
	def addUsb(vendor: str, name: str, serial: str) -> None:
		file_path: str = f"dev/USB{len(os.listdir('dev')) +1}.ddev"
		to_add: dict = {"vendor": vendor, "name": name, "serial": serial}

		with open(f"dev/USB{len(os.listdir('dev')) +1}.ddev", "w") as dev:
			json.dump(to_add, dev, indent=4)
			c.info(f"Saved USB device (Identifier: USB{len(os.listdir('dev'))}.ddev)", True)

	@staticmethod
	def retDevData(name: str) -> dict:
		filename, ext = os.path.splitext(name)
		if filename.startswith("USB") and ext == ".ddev":
			with open(os.path.join("dev", name), "r") as dev:
				return json.load(dev)

	@staticmethod
	def scanSaved() -> None:
		usb_dev_data.clear()
		for dev in os.listdir("dev"):
			data = UsbActions.retDevData(dev)
			if data: usb_dev_data.append(data)

	@staticmethod
	def scanUsb() -> None:
		global usb_dev_obj
		usb_dev_obj = usb.core.find(find_all=True)

		for dev in usb_dev_obj:
			try:
				vendor: str = usb.util.get_string(dev, dev.iManufacturer) or "Unknown vendor"
			except:
				vendor: str = "Unknown vendor"

			try:
				name: str = usb.util.get_string(dev, dev.iProduct) or "Unknown name"
			except:
				name: str = "Unknown name"

			try:
				serial: str = usb.util.get_string(dev, dev.iSerialNumber) or "Unknown serial number"
			except:
				serial: str = "Unknown serial number"

			if (vendor, name, serial) != ("Unknown vendor", "Unknown name", "Unknown serial number"):
				c.info(f"Detected USB device: {vendor}: {name} ; SN: {serial}", True)
				if not {"vendor": vendor, "name": name, "serial": serial} in usb_dev_data:
					UsbActions.addUsb(vendor, name, serial)

	@staticmethod
	def initUsb() -> None:
		UsbActions.scanSaved()
		if len(usb_dev_data) == 0:
			c.warn("System could not find any USB device. System halted", True)
			dragonKernel.console(mode="nousbdev")

def start() -> None:
	try:
		UsbActions.scanSaved()
		UsbActions.scanUsb()
		UsbActions.initUsb()
	except Exception as x:
		c.error(f"IERR_3: Error finding USB devices: {x}")
		exit("IERR_3")

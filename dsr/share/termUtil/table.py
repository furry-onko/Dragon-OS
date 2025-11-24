from enum import Enum
from dsr.share.termUtil import colors as c
from itertools import zip_longest

def tableHelp() -> None:
	print("Tables help page")
	print("Table types: DUMMYTABLE, KEYVALUETABLE, TOPDOWNTABLE, XYTABLE\n")
	print("Init table:")
	print("tab: Table = Table(TableTypes.DUMMYTABLE)")

class TableTypes (Enum):
	DUMMYTABLE = 1
	KEYVALUETABLE = 2
	TOPDOWNTABLE = 3
	XYTABLE = 4

class TableStyles (Enum):
	CENTER = 1
	LEFT = 2
	RIGHT = 3

class Table:
	# >>= Constructor
	def __init__(
		self,
		table_type: TableTypes = TableTypes.DUMMYTABLE,
		table_style: TableStyles = TableStyles.LEFT,
		table_title: str = "",
		table_title_style: TableStyles = TableStyles.CENTER		
	) -> None:
		self.table_type: TableTypes = table_type
		self.table_style: TableStyles = table_style
		self.table_title: str = table_title
		self.table_title_style: TableStyles = table_title_style

		self.dummy_table_content: list[str] = []
		self.keyValue_table_content: list[dict[str, str]] = []
		self.topDown_table_content: list[dict[str, list[str]]] = []

		self.xy_table_head_X: list[str] = []
		self.xy_table_head_Y: list[str] = []
		self.xy_table_content: list[list[str]] = []

	# >>= Type G/S
	def setType(self, type: TableTypes) -> None:
		self.table_type = type
	def getType(self) -> TableTypes:
		return self.table_type

	# >>= Title G/S
	## Title text G/S
	def setTitle(self, title: str) -> None:
		self.table_title = title
	def getTitle(self) -> str:
		return self.table_title

	## Title style G/S
	def setTitleStyle(self, style: TableStyles) -> None:
		self.table_title_style = style
	def getTitleStyle(self) -> TableStyles:
		return self.table_title_style
	# <<=

	# >>= Style G/S
	def setStyle(self, style: TableStyles) -> None:
		self.table_style = style
	def getStyle(self) -> TableStyles:
		return self.table_style

	# >>= Dummy Table G/S
	def setDummyTableContent(self, content: list[str]) -> None:
		if self.table_type == TableTypes.DUMMYTABLE:
			self.dummy_table_content = content
		else:
			c.error("Method executed on the wrong type of table.")
	def getDummyTableContent(self) -> list[str]:
		return self.dummy_table_content

	# >>= Key Value Table G/S
	def setKeyValueTableContent(self, content: list[dict[str, str]]) -> None:
		if self.table_type == TableTypes.KEYVALUETABLE:
			self.keyValue_table_content = content
		else:
			c.error("Method executed on the wrong type of table.")
	def getKeyValueTableContent(self) -> list[dict[str, str]]:
		return self.keyValue_table_content

	# >>= Top Down Table G/S
	def setTopDownTableContent(self, content: list[dict[str, list[str]]]) -> None:
		if self.table_type == TableTypes.TOPDOWNTABLE:
			self.topDown_table_content = content
		else:
			c.error("Method executed on the wrong type of table.")
	def getTopDownTableContent(self) -> list[dict[str, list[str]]]:
		return self.topDown_table_content

	# >>= XY Table G/S
	## Head X G/S
	def setXyTableHeadX(self, content: list[str]) -> None:
		if self.table_type == TableTypes.XYTABLE:
			self.xy_table_head_X = content
		else:
			c.error("Method executed on the wrong type of table.")
	def getXyTableHeadX(self) -> list[str]:
		return self.xy_table_head_X
	
	## Head Y G/S
	def setXyTableHeadY(self, content: list[str]) -> None:
		if self.table_type == TableTypes.XYTABLE:
			self.xy_table_head_Y = content
		else:
			c.error("Method executed on the wrong type of table.")
	def getXyTableHeadY(self) -> list[str]:
		return self.xy_table_head_Y

	## Content G/S
	def setXyTableContent(self, content: list[list[str]]) -> None:
		if self.table_type == TableTypes.XYTABLE:
			self.xy_table_content = content
		else:
			c.error("Method executed on the wrong type of table.")
	def getXyTableContent(self) -> list[list[str]]:
		return self.xy_table_content
	# <<=

def createTable(tab: Table) -> None:
	# >>= Get Table's Core Data
	table_type: TableTypes = tab.getType()
	table_style: TableStyles = tab.getStyle()
	table_title: str = tab.getTitle()
	table_title_style: TableStyles = tab.getTitleStyle()
	
	# >>= Get Table's Type
	match table_type:
		case TableTypes.DUMMYTABLE:
			dummy_table_content: list[str] = tab.getDummyTableContent()
		case TableTypes.KEYVALUETABLE:
			keyValue_table_content: list[dict[str, str]] = tab.getKeyValueTableContent()
		case TableTypes.TOPDOWNTABLE:
			topDown_table_content: list[dict[str, list[str]]] = tab.getTopDownTableContent()
		case TableTypes.XYTABLE:
			xy_table_head_X: list[str] = tab.getXyTableHeadX()
			xy_table_head_Y: list[str] = tab.getXyTableHeadY()
			xy_table_content: list[list[str]] = tab.getXyTableContent()
		case _:
			c.error("Unknown table type.")

	# >>= Print Table
	## Dummy
	if table_type == TableTypes.DUMMYTABLE:
		table_length: int = len(dummy_table_content)
		longest: int = max(
			[
				len(element)
				for element in dummy_table_content
			]
		) +2

		print(f"+{'-' * longest}+")

		i: int = 0
		while i < table_length:
			print(f"|{dummy_table_content[i]}{' ' * (longest - len(dummy_table_content[i]))}|")
			i += 1
		
		print(f"+{'-' * longest}+")

	## Key-Value
	elif table_type == TableTypes.KEYVALUETABLE:
		table_length: int = len(keyValue_table_content)
		
		key_names: tuple = (
			[
				list(pair.keys())[0]
				for pair in keyValue_table_content
			]
		)
		longest_key: int = max(
			[
				len(key)
				for key in key_names
			]
		) +2

		value_names: tuple = (
			[
				list(pair.values())[0]
				for pair in keyValue_table_content
			]
		)
		longest_value: int = max(
			[
				len(value)
				for value in value_names
			]
		) +2

		print(f"+{'-' * longest_key}+{'-' * longest_value}+")
		
		i: int = 0
		while i < table_length:
			print(f"|{key_names[i]}{' ' * (longest_key - len(key_names[i]))}|{value_names[i]}{' ' * (longest_value - len(value_names[i]))}|")
			i += 1

		print(f"+{'-' * longest_key}+{'-' * longest_value}+")

	elif table_type == TableTypes.TOPDOWNTABLE:
		longest_header: int = max(
			[
				
			]
		)

dm_tab: Table = Table()
dm_tab.setDummyTableContent(["a", "asd", "negro"])
createTable(dm_tab)

kv_tab: Table = Table()
kv_tab.setType(TableTypes.KEYVALUETABLE)
kv_tab.setKeyValueTableContent([{"name": "onko"}, {"age": "nuh uhh"}, {"fav_pooltoy": "Nyika"}])
createTable(kv_tab)

dt_tab: Table = Table()
dt_tab.setType(TableTypes.TOPDOWNTABLE)
dt_tab.setTopDownTableContent([{"cat": ["meow","mrrr","purrrr", "nyaaauuuwww"]}, {"dawg": ["woof", "huff", "awooooo"]}])
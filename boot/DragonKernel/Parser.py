from dsr.share.termUtil import colors as c

class Parser:
	def __init__(file_path: str) -> None:
		try:
			with open(file_path, 'r') as f:
				self.file_content = f.read()
		except Exception as x:
			c.error(f"Error loading file: {x}")
			
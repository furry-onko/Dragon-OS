from boot import init
import os

if __name__ == "__main__":
	os.chdir(os.path.dirname(__file__))
	init.start()
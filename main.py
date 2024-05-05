# HalloFriend
# copyright by Mayank (https://github.com/MayankDevil)
# ./main.py

import sys

sys.path.append("src")	# add the source directory to path

from hallo import Hallo
from how import How

if __name__ == "__main__":

	How.loader()
	How.welcome("To new system")
	Hallo.friend(How.areYou)
	How.done()

# ---{ the end }---

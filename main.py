# HalloFriend
# copyright by Mayank (https://github.com/MayankDevil)
# ./main.py

import sys

sys.path.append("src")	# add the source directory to path

from hallo import Hallo
from how import How
from theme import Theme

if __name__ == "__main__":

	Theme.welcome("To new system")
	Hallo.friend(How.are)

# ---{ the end }---

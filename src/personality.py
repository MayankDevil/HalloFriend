# HalloFriend
# copyright by Mayank (https://github.com/MayankDevi)
# ./src/personality.py

import sys
import time

class Person:


	# constructor ---
	def __init__(self):
		self.name = ""
		self.sex = 0
		self.friend = ""
		self.isShe = False
		self.likeShe = False
		self.hasMale = False
		self.hasDeveloper = False


	# choice function ---
	def choice(self, choice_text):

		user_choice = input("\n "+choice_text+" [Yes/No]: ")

		if user_choice[0].upper() == "Y":
			return True
		else:
			return False


	# introduction function ---
     def ami(self):
          if self.hasDeveloper:
               print("\n-\tI am your, whore master")
          else:
               print("\n-\t let me tell about myself.")
               time.sleep(2)
               print("\n\t i am (Attempt Listen In Simple Humanoid Application)")
               input(" : ")
               print("\t\t You are call me, ALISHA")


	# enter name function ---
	def enter_name(self):
		while True:
			self.name = input("\n what is your Name, Dear = ")
			if len(self.name) != 0:
				return self.name.upper()


	# is Developer function ---
	def isDeveloper(self, name):
		if name.upper() == 'MAYANK' or name.upper() == 'DEVIL':
			self.hasDeveloper = True
			self.hasMale = True
			print("\n\t Welcome Sinilich MutterFicker)") # welcome sexy motherfucker
		else:
			print("\n\t"+name+", Good Name")
			self.gender()


	# done function ---
	def done():
		animation = "|/-\\"
		idx = 0
		for i in range(0,9):
			sys.stdout.write("\r"+animation[idx% len(animation)])
			sys.stdout.flush()
			idx += 1
			time.sleep(0.1)
		print("\b successed!")


	# loader function ---
	def loader():
		width = 50
		progress = 0
		print("\n")
		while progress <= width:
			sys.stdout.write("\r ["+ "#" * progress + " " * (width - progress) +"]")
			sys.stdout.flush()
			progress = (progress+1)
			time.sleep(0.1)
		print("\b] loaded {100%}\n")


# ---{ the end }---


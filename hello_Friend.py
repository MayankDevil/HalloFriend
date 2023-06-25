# ==========================================================
# Hello_Friend : developed by mayank class Hallo
# ==========================================================

import time

name = ""
she_name = ""
sex = 0

# ENTER NAME : get name of program user
def enter_name():
     while 1:
          name = input("\n what is your Name, Dear = ")
          if len(name) != 0:
               return name.upper()

# ------------------------
# WHO ARE : verify master
# ------------------------
def who_are(name):
     if name.upper() == "MAYANK" or name.upper() == "DEVIL":
          print("\n\t Welcome Sinilich MutterFicker :)")
          # welcome sexy motherfucker
          master = 1
     else:
          print("\n\t"+name+", Good Name")
          gender()

# --------------------------------------------
# CHOICE : if any question return yes else no
# --------------------------------------------
def choice(choice_text):
     n = input("\n "+choice_text+" [Yes/No]: ")
     if n[0].upper() == "Y":
          return 1
     else:
          return 0

def who():
     print("\n\t My name is")
     time.sleep(3)
     print(" [ ALISHA ]")
     input()
     print("( Advance Language Interact Smart High Application )")

#
def but_iam():
     print("\n\t but I am she!")

#
def let_friend():
     if choice("if you don't mind let be friends"):
          print("yes")
     else:
          print("no")

#
def she_name():
     while 1:
          she_name = input("\n what is her name "+name+" = ")
          if len(she_name) != 0:
               break

#
def was_she():
     if choice("Are she"):
          she_name()
     else:
          but_iam()

#
def bye():
     if choice("Give me permission to leave"):
          print("\n\t Bye Dear")

# 
def execute_Hallo():
     
     who_name(enter_name())

     if choice("Are you Male"):
          print("\n\t So are you Dog!")
     else:
          print("\n\t Mean you are bitch!")

     time.sleep(2)

     print("\n\t Sorry! It is Joke :)")

     input()

     if choice("Have any friend"):
          was_she()
     else:
          print("\n\t But I am here")

     let_friend()

     bye()


#  =========================================================

execute_Hallo()


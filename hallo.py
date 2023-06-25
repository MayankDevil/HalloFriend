# ===================
#    Hello Friend   |
# ===================

import time

name = ""

friend_name = ""

gender = 0     # 0 girl 1 male

status = 0     

master = 0

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

# -------------------------------------
# GENDER : check gender male or female
# -------------------------------------
def gender():
     if choice("Are you Male?"):
          print("\n-\t Du bist also ein hund!")
          # 
          gender = 1
     else:
          print("\n-\t bedeutet, dass du eine Hure bist")
          # 
          gender = 0
     time.sleep(1)
     print("\n Plese forgive me, I was just trying to get your!")
     

# 

def i_am_she():
     print("\n\t But, I am she?")
     time.sleep(1)
     print("\n\t I am single")

# HIS NAME

def his_name():
     friend_name = input("\n What is his name = ")
     if friend_name.upper() == "YOU":
          print("\n\t I am glad!")
          iam()
     else:
          print("\n\t"+friend_name+", Nice")
          time.sleep(1)
          if choice("Do you like that!"):
               if choice("have you had sex?"):
                    print("\n\t Das heibt, sie ist deine Hure.")
               time.sleep(1)
               bye()
          else:
               friend_name = input("\n So who once you crush? = ")

# IAM

def iam():
     print("\n\t let me tell about myself.")
     time.sleep(1)
     print("\t I am [ Advance Language Interact Super Higher Application ]")
     time.sleep(1)
     print("\t\t You are call me, Alisha")     
     bye()


# FROEMDSHIP

def friendship():
     if choice("Can was be Friend?"):
          print("\n\t The pleasure was all mine.")
          iam()
     else:
          print("\n\t I think you are having a chance")
          time.sleep(1)
          if choice("I ask again will you be my friend?"):
               iam()
          else:
               bye()


# BYE

def bye():
     if choice("Hope you enjoy"):
          if choice("Please, let me go now"):
               close()
          elif master == 1:
               print("\n-\t willst du zustimmern, meinen Arsch zu nehmen?")
               # will you agree to take my ass
     else:
          print("\n-\t Sanst steck deinen Schwanz in deine Arsch!")
          # otherwise put you dick in your ass


# CLOSE

def close():
     print("\n bye \n")


# EXECUTE

def excute():

     print("\n Hello Friend! \n")

     who_are(enter_name())

     if choice("You have a Friend?"):
          if choice("Is that she"):
               his_name()
          else:
               i_am_she()
     else:
          friendship()


excute()

# ----------------------------------
#  CopyRight & Developed By Mayank ]
# ----------------------------------
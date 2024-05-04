# HalloFriend
# copyright by Mayank (https://github.com/MayankDevi)
# ./src/hallo.py

import time

from personal import Personal

class Hallo(Personal):


     # gender function ---
     def gender(self):
          if self.choice("Are you male?"):
               print("\n - \t Du bist also ein hund!") #
               self.hasMale = True
          else:
               print("\n - \t bedeutet, dass du eine Hure bist") #

          time.sleep(1)
          print("\n Plese forgive me, I was just trying to get your!")


     # isShe function ---
     def hisShe(self):
          if self.choice("His She"):
               self.isShe = True
               self.whoShe()
          else:
               print("\n-\tbut i am, She!")
               time.sleep(2)
               self.purposeal()

     # whoShe function ---
     def whoShe(self):
          if self.his_name() == "YOU":
               print("\n\t I am glad!")
               self.iam()
          else:
               print("\n\t"+self.friend+", Nice")
               time.sleep(1)
               if self.choice("Do you like that!"):
                    self.likeShe = True
                    if self.choice("have you had sex?"):
                         self.sex = 1
                         print("\n\t Das heibt, sie ist deine Hure.")
                    time.sleep(1)
               else:
                    if self.choice("So have any crush"):
                         pass
          self.purposeal()


     # his_name function ---
     def his_name(self):
          while True:
               self.friend = input("\n What is his name = ")
               if len(self.friend) != 0:
                    return self.friend.upper()


     # purposeal function ---
     def purposeal(self):
          if ("Can was be firend"):
               print("\n\t The pleasure was all mine.")
               self.ami()
          else:
               print("\n\t I think you are having a chance")
               time.sleep(1)
               if choice("I ask again will you be my friend?"):
                    self.ami()
               else:
                    self.bye()


     # bye function ---
     def bye(self):
          if self.choice("Hope you enjoy"):
               if self.choice("Please, let me go now"):
                    return
               elif self.hasDeveloper:
                    print("\n-\t willst du zustimmern, meinen Arsch zu nehmen?") # will you agree to take my ass
          if self.hasDeveloper:
               print("\n-\t so punish me, to take my!")
          else:
               print("\n-\t Sanst steck deinen Schwanz in deine Arsch!") # otherwise put you dick in your ass


     # friend execute ---
     def friend(self):
          
          self.isDeveloper(self.enter_name())
          
          input(" : ")

          print("\n ok \n")

          if self.choice("Have any friend"):
               self.hisShe()
          else:
               self.purposeal()
     

# ---{ the end }---


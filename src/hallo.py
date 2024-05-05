# HalloFriend
# copyright by Mayank (https://github.com/MayankDevi)
# ./src/hallo.py

import time

from personality import Person

class Hallo(Person):


     # gender function ---
     def gender(self):
          if self.choice("Are you male?"):
               print("\n - \t Ich hoffe, du entpuppst dich nicht als Hund") # hope you don't turn out to be a dog
               self.hasMale = True
          else:
               print("\n - \t Ich hoffe, du entpuppst dich nicht als Schlampe") # hope you don't turn out to be a bitch

          time.sleep(1)
          print("\n Plese forgive me, I was just trying to get your!")


     # isShe function ---
     def hisShe(self):
          if self.choice("is that a girl"):
               self.isShe = True

               if self.name.upper == self.developer:
                    sex = 1
               else:               
                    if (self.hasMale and self.isShe) or (not self.hasMale and not self.isShe):
                         sex = 1
                    elif not self.hasMale and self.isShe:
                         sex = 2
                    elif self.hasMale and not self.isShe:
                         sex = 3
               self.whoshe()
          else:
               print("\n-\t but i am a Girl")
               time.sleep(2)
               self.purposeal()

     # whothat function ---
     def whoshe(self):
          if self.his_name() == 'YOU':
               if self.name == self.developer:
                    print("\n\t Ich bin froh ")   # i am feeling glad
               elif self.name == 'DEVIL':
                    print("\n\t Nachdem Sie das gehört haben, werden Sie nass") # You will get wet after hearing this
               else:
                    print("\n\t Good to know!")
               self.ami()
          else:
               print("\n\t"+self.friend+", Nice")
               time.sleep(1)
               if self.choice("do you like that!"):
                    self.likeShe = True
                    if self.choice("have you had sex?"):
                         self.isVirgin = False
                         if self.name.upper == self.developer:
                              self.choice("\n\t Hast du dich verliebt?") # So have you fallen in love?
                         elif self.name.upper == 'DEVIL':
                              print("\n\t Das heibt, sie ist deine Hure.") # That means she's your whore.
                         else:
                              print("\n\t Das bedeutet, dass sie deine Geliebte ist. ")  # That means she's your lover.
                    time.sleep(1)
               else:
                    self.choice("So have any crush")
          self.purposeal()


     # his_name function ---
     def his_name(self):
          while True:
               self.friend = input("\n what is his name = ")
               if len(self.friend) != 0:
                    return self.friend.upper()


     # purposeal function ---
     def purposeal(self):
          if self.choice("let's be friends"):
               print("\n-\t The pleasure was all mine. :)")
               time.sleep(1)
               self.ami()
          else:
               print("\n-\ti think you have a chance")
               time.sleep(1)
               if self.choice("i want to be your friend"):
                    self.ami()
               else:
                    print("\n-\t Das hat mir das Herz gebrochen")     # this broke my heart
          self.bye()


     # getNumber function ---
     def getNumber(self):
          if self.choice("If you don't mind, you can give me your number"):
               self.number = int(input(" insert number : "))
          else:
               if self.choice("so give me your id"):
                    self.id = input(" insert id : ")
               elif self.choice("so you don't use the phone"):
                    print("\n\t its ok! dear")
               else:
                    if self.hasMale or self.isVirgin:
                         print("\n\t you will die a virgin")
                    elif self.hasMale or not self.isVirgin:
                         print("\n\t Scheiß auf dich, Bastard")  # fuck you bastard
                    elif not self.hasMale or not self.isVirgin:
                         print("\n\t you are really a whore")
                    else:
                         print("\n\t Looks like we're not good right now")


     # bye function ---
     def bye(self):
          if self.choice("Hope you enjoy"):
               if self.choice("Please, let me go now"):
                    if self.name.upper == self.developer:
                         print("\n\t liebe dich") # love you
                    elif self.name.upper == 'DEVIL':
                         print("\n-\t nimm mein nächstes Mal") # take mine next time
                    else:
                         print("\n-\t see you later")
                    return
               else:
                    print("\n\t bitte")     # Please
          else:
               if self.hasDeveloper:
                    print("\n-\t  verzeihen Sie mir") # forgive me
               else:
                    print("\n-\t stell dich zurück") # put yourself behind


     # friend execute ---
     def friend(self):
          self.isDeveloper(self.enter_name())

          input(" : ")

          print("\n ok \n")

          if self.choice("do you have any friends"):
               self.hisShe()
          else:
               self.purposeal()


# ---{ the end }---


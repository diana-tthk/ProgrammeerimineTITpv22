#we have class Warrior
#every warrior has some health (100 p. at the beginning)
#Warrior may attack. When attacking,
#the warrior he attack looses health 
#random number between 1 and 20
#Write a game, with two warriors attacking in random order
#After each attack print who attacked whom and how 
#many health they have left. Once someone has no health
#left, game is over and the winner is printed
import random
class Warrior:
    __name = ""
    hp = 100

    def name(self):
        return self.__name

    def __init__(self, name):
        self.__name = name

    def attack(self, warrior):
        if isinstance(warrior, Warrior):
            print(self.__name, "is attacking", warrior.__name)
            warrior.under_attack()
        else:
            print("Cannot attack this object!")
        return
    
    def under_attack(self):
        self.hp = self.hp - random.randint(1,20)
        print(self.__name, "has", self.hp, "health")
        return

    


#main logic
war1 = Warrior("Marek") 
war2 = Warrior("Peter")

def end_game(w1, w2):
    if w1.hp <= 0 or w2.hp <= 0:
        return True
    else:
        return False

while True:
    lot = random.randint(1,2)
    if lot == 1:
        war1.attack(war2)
        if(end_game(war1, war2)):
            print(war1.name(), "has won the game!")
            break
    else:
        war2.attack(war1)
        if(end_game(war1, war2)):
            print(war2.name(), "has won the game!")
            break

input()
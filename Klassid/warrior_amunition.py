# we have warrior (can use the one from warrior.py as a
# basis). Also we have several weapons: sword, frist
# Sword makes 10-20 of damage. Frist makes 0-15
# Warrior can have sword (if no weapon, then 
# warrior uses only frists). At the begginig of game
# warriors roll the dice. If ones score is 3 or more,
# one gets a sword. Extend the game writen previously 
# according to this scenario
import random

class Frist:
    def get_damage(self):
        return random.randint(0, 15)

class Sword:
    def get_damage(self):
        return random.randint(10, 20)

class Warrior:
    name = ""
    hp = 100
    weapon = Frist()

    def __init__(self, name):
        self.name = name

    def attack(self, warrior):
        if isinstance(warrior, Warrior):
            print(self.name, "is attacking", warrior.name)
            warrior.under_attack(self.weapon.get_damage())
        else:
            print("Cannot attack this object!")
        return
    
    def under_attack(self, damage):
        self.hp = self.hp - damage
        print(self.name, "has", self.hp, "health")
        return



war1 = Warrior("Marek") 
war2 = Warrior("Peter")
#pick up weapons


def end_game(w1, w2):
    if w1.hp <= 0 or w2.hp <= 0:
        return True
    else:
        return False
#main game loop
while True:
    lot = random.randint(1,2)
    if lot == 1:
        war1.attack(war2)
        if(end_game(war1, war2)):
            print(war1.name, "has won the game!")
            break
    else:
        war2.attack(war1)
        if(end_game(war1, war2)):
            print(war2.name, "has won the game!")
            break

input()
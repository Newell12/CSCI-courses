class Hero:
    '''
    Purpose: An object of this class represents a Hero
    Instance variables:
        Name: This is a string representing the name of the Hero
        Level: This is an int representing the level of the Hero
        Strength: This is an int representing the strength of the Hero
        Magic: This is an int representing the magic power of the Hero
        HP: This is an int representing the Health Points of the Hero
        Hidden: This is a boolean representing wether the Hero is hidden
    Methods:
        __init__: This is a constructor method which instantiates the instance variables of the class
        __repr__: This method overwrites what happens when you call the Hero object
        __lt__: This method overwrites waht happens when you call less than on two Hero objects
        attack: This method uses the stats of one Hero for it to deal an amount of damage to a target Hero
    '''
    def __init__(self, name, level, strength, magic):
        self.name = name
        self.level = level
        self.strength = strength
        self.magic = magic
        self.HP = level * 5
        self.hidden = False
    def __repr__(self):
        return self.name + ": " + str(self.HP) + " HP"
    def __lt__(self, other):
        return self.HP < other.HP
    def attack(self, target):
        if target.hidden == True :
            print(self.name + " can't see " + target.name)
        else:
            damage = self.strength + 3
            target.HP = target.HP - damage
            print(self.name + " attacks " + target.name + " for " + str(damage) + " damage")
class Thief(Hero):
    '''
    Purpose: An object of this class represents a Thief and inherits from the Hero class
    Instance variables:
        Name: This is a string representing the name of the Thief
        Level: This is an int representing the level of the Thief
        Strength: This is an int representing the strength of the Thief
        Magic: This is an int representing the magic power of the Thief
        HP: This is an int representing the Health Points of the Thief
        Hidden: This is a boolean representing wether the Thief is hidden
    Methods:
        __init__: This is a constructor method which instantiates the instance variables of the class overwriting the Hero class so that the HP calculates differently and the hidden is True
        attack: This method uses the stats of one Thief for it to deal an amount of damage to a target either calling the Hero attack or performing a sneak attack
    '''
    def __init__(self, name, level, strength, magic):
        Hero.__init__(self, name, level, strength, magic)
        self.HP = level * 8
        self.hidden = True
    def attack(self, target):
        if self.hidden == False:
            Hero.attack(self, target)
        elif self.hidden == True:
            damage = (self.strength + self.level) * 4
            self.hidden = False
            target.hidden = False
            target.HP = target.HP - damage
            print(self.name + " sneak attacks " + target.name + " for " + str(damage) + " damage")
class Ninja(Thief):
    '''
    Purpose: An object of this class represents a Ninja and inherits from the Thief class
    Instance variables:
        Name: This is a string representing the name of the Ninja
        Level: This is an int representing the level of the Ninja
        Strength: This is an int representing the strength of the Ninja
        Magic: This is an int representing the magic power of the Ninja
        HP: This is an int representing the Health Points of the Ninja
        Hidden: This is a boolean representing wether the Ninja is hidden
    Methods:
        attack: This method uses the stats of one Thief for it to deal an amount of damage to a target either calling the Hero attack or performing a sneak attack
    '''
    def attack(self, target):
        Thief.attack(self, target)
        self.hidden = True
        self.HP = self.HP + self.level
class Mage(Hero):
    '''
    Purpose: An object of this class represents a Mage and inherits from the Hero class
    Instance variables:
        Name: This is a string representing the name of the Mage
        Level: This is an int representing the level of the Mage
        Strength: This is an int representing the strength of the Mage
        Magic: This is an int representing the magic power of the Mage
        HP: This is an int representing the Health Points of the Mage
        Hidden: This is a boolean representing wether the Mage is hidden
        Fireballs: This is an int representing the amount of the fireballs
    Methods:
        __init__: This is a constructor method which instantiates the instance variables of the class overwriting the Hero class so that the mage has fireballs
        attack: This method uses the stats of one Mage for it to deal an amount of damage to a target either calling the Hero attack or performing a fireball attack
    '''
    def __init__(self, name, level, strength, magic):
        Hero.__init__(self, name, level, strength, magic)
        self.fireballs = magic
    def attack(self, target):
        if self.fireballs == 0:
            Hero.attack(self, target)
        else:
            damage = self.level * 4
            target.hidden = False
            self.fireballs = self.fireballs - 1
            target.HP = target.HP - damage
            print(self.name + " casts fireball on " + target.name + " for " + str(damage) + " damage")
class Wizard(Mage):
    '''
    Purpose: An object of this class represents a Wizard and inherits from the Mage class
    Instance variables:
        Name: This is a string representing the name of the Wizard
        Level: This is an int representing the level of the Wizard
        Strength: This is an int representing the strength of the Wizard
        Magic: This is an int representing the magic power of the Wizard
        HP: This is an int representing the Health Points of the Wizard
        Hidden: This is a boolean representing wether the Wizard is hidden
        Fireballs: This is an int representing the amount of the fireballs
    Methods:
        __init__: This is a constructor method which instantiates the instance variables of the class overwriting the Hero class so that the wizard has fireballs
    '''
    def __init__(self, name, level, strength, magic):
        Mage.__init__(self, name, level, strength, magic)
        self.HP = level * 3
        self.fireballs = magic * 2

def battle(user_team, enemy_team):
    while(len(user_team)>=1 and len(enemy_team)>=1):
        print()
        print("-------- Your Turn --------")
        print("Your Team: ")
        for i in range(len(user_team)):
            print(user_team[i])
        for i in range(len(user_team)):
            print()
            for j in range(len(enemy_team)):
                print("Enemy " + str(j+1) + " - " + enemy_team[j].name + ": " + str(enemy_team[j].HP) + " HP")
            target = int(input("Choose a target for " + user_team[i].name + ": ", ))
            user_team[i].attack(enemy_team[target-1])
            if enemy_team[target-1].HP <= 0:
                print(enemy_team[target-1].name + " was defeated")
                enemy_team.remove(enemy_team[target-1])
                if len(enemy_team)<=0:
                    print("You win")
                    return user_team
        print()
        print("-------- Enemy Turn --------")
        for h in range(len(enemy_team)):
            enemy_target = min(user_team)
            enemy_team[h].attack(enemy_target)
            if enemy_target.HP <=0:
                print(enemy_target.name + " was defeated")
                user_team.remove(enemy_target)
                if len(user_team)<=0:
                    print("You lose")
                    return enemy_team

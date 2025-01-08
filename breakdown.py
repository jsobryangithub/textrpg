####ADVENTURE RPG####

####BASIC STUFF TO ADD###
#help menu to display current stats, equipment, skill definitions, etc
#encounters / combat system
#initial setup (introduction text, show starting stats, equipment)
#skill descriptions / let player choose which skills to add

####LONG TERM GOALS####
#make it a web-based app
#gui / tkinter?
#create images to go along with encounters, etc

##GAMEPLAY / MECHANICS DECISIONS
#do an actual Lone Wolf clone (stick to original game texts, mechanics etc)
#make the encounters and decisions simpler (i.e. player is given a fixed number of skills.  Encounters will consist of the player attempting to use those skills on NPCs / enemies with the results dependent on the skill used)
#simple approach will be better if going for a more humorous tone.  It can be silly without being overly vulgar or gross

#GENERAL IDEAS / NOTES
#if it's going to be an original story, write the story and decision trees first, then worry about the encounter logic




import random
from dataclasses import dataclass

#random number generator
randNum = random.randint(0,10)

###character setup
@dataclass
class Character:

###player stats
#refer to notion for post_init definition
    endurance: int = 0
    maxEndurance: int = 0
    combatSkill: int = 0
    gold: int = 0 #max 50
    equipment = []  #max 8.  Meals count as equipment.  Player starts with 1 meal
    items = []
    weapons = [] #max 2.  Player starts with axe 
    skills = [] #max 5

    def __post_init__(self):
        enduranceStat = random.randint(0,10) + 20
        self.Maxendurance = enduranceStat
        self.endurance = enduranceStat
        self.combatSkill = random.randint(0,10) + 10
        self.gold = random.randint(0,10)


#random choice of items
#player will start with an additional item chosen at random from the following using randNum
#1 sword
#2 helmet - adds 2 endurance
#3 two meals
#4 chainmail waistcoat - adds 4 endurance
#5 mace
#6 healing potion - restores 4 endurance when used.  
#7 quarterstaff
#8 spear
#9 12 gold crowns
#0 broadsword

#player functions

    def statChange(self, value: int, statName: str):
        # Modify the specified stat
        if statName == "endurance":
            self.endurance += value
        elif statName == "combatSkill":
            self.combatSkill += value
        else:
            raise ValueError(f"Invalid stat name: {statName}")
        
@dataclass
class Equipment:
    name: str
    equipmentType: str
    maxAmount: int = 0
    currentAmount: int = 0
    canUse: bool = False

    def addItem(self, amount: int=1) -> str:
        if self.currentAmount + amount > self.maxAmount:
            return f"Cannot add {amount} {self.name}(s). You can carry a maximum of {self.maxAmount}."
        self.currentAmount += amount
        return f"Added {amount} {self.name}(s). You are now carrying {self.currentAmount}."
    
    def removeItem(self, amount: int = 1) -> str:
        if self.currentAmount - amount < 0:
            return f"Cannot remove {amount} {self.name}(s). You only have {self.currentAmount}."
        self.currentAmount -= amount
        return f"Removed {amount} {self.name}(s). You are now carrying {self.currentAmount}."
    
    def healthItem(self, character: Character, effect: int = 0) -> str:
        if not self.canUse:
            return f"This is not a usable item."

        if character.endurance == character.maxEndurance:
            return f"You cannot use the {self.name} right now. You are already at full health."

        # Adjust the character's endurance (use statChange if implemented)
        character.endurance = min(character.endurance + effect, character.maxEndurance)
        return f"You use the {self.name}. Added {effect} Endurance. Your endurance is now {character.endurance}."
    

@dataclass
##goal here is to have to print a list of skills.  Player should be able to either choose the skill or have an 'info' option to display the skill text.  Player can only choose 5 skills.

class Skills:
    skills = {
       'camouflage':'This Discipline enables a Kai Lord to blend in with his surroundings. In the countryside, he can hide undetected among trees and rocks and pass close to an enemy without being seen. In a town or city, it enables him to look and sound like a native of that area, and can help him to find shelter or a safe hiding place.',
       'Hunting':'This skill ensures that a Kai Lord will never starve in the wild. He will always be able to hunt for food for himself except in areas of wasteland and desert. The skill also enables a Kai Lord to be able to move stealthily when stalking his prey',
    }

    @staticmethod
    def addSkill(self, character: Character, skillName) -> str:
        character.skills.append(skillName)
        
        

                

    



if __name__ == "__main__":
    pass
    
    
    
    
    
    
    
    
    
    ##EXAMPLE USAGES
    # player = Character()
    # print(f"Initial stats: Endurance={player.endurance}, CombatSkill={player.combatSkill}")


    # player.statChange(5, "endurance")
    # player.statChange(-3, "combatSkill")
    # print(f"Updated stats: Endurance={player.endurance}, CombatSkill={player.combatSkill}")
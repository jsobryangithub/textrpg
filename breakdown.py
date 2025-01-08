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

import random
from dataclasses import dataclass

#random number generator
randNum = random.randint(0,10)

###character setup
@dataclass
class Character:

###player stats

    endurance: int = 0
    maxEndurance: int = 0
    combatSkill: int = 0
    gold: int = 0 #max 50
    equipment = {}  #max 8.  Meals count as equipment.  Player starts with 1 meal
    items = {}
    weapons = [] #max 2.  Player starts with axe 
    skills = {} #max 5

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

##should probably have a help menu for player to reference

class Skills:
    skills = {
       'Camouflage':'This Discipline enables a Kai Lord to blend in with his surroundings. In the countryside, he can hide undetected among trees and rocks and pass close to an enemy without being seen. In a town or city, it enables him to look and sound like a native of that area, and can help him to find shelter or a safe hiding place.',
       'Hunting':'This skill ensures that a Kai Lord will never starve in the wild. He will always be able to hunt for food for himself except in areas of wasteland and desert. The skill also enables a Kai Lord to be able to move stealthily when stalking his prey',
       'Sixth Sense':'This skill may warn a Kai Lord of imminent danger. It may also reveal the true purpose of a stranger or strange object encountered in your adventure.',
       'Tracking':'This skill enables a Kai Lord to make the correct choice of a path in the wild, to discover the location of a person or object in a town or city and to read the secrets of footprints or tracks.',
       'Healing':'This Discipline can be used to restore ENDURANCE points lost in combat. If you possess this skill you may restore 1 ENDURANCE point to your total for every section you pass through in which you are not involved in combat. (This is only to be used after your ENDURANCE has fallen below its original level.) Remember that your ENDURANCE cannot rise above its original level.',
       'Weaponskill':'Upon entering the Kai Monastery, each initiate is taught to master one type of weapon. If Weaponskill is to be one of your Kai Disciplines, pick a number in the usual way from the Random Number Table, and then find the corresponding weapon from the list below. This is the weapon in which you have skill. When you enter combat carrying this weapon, you add 2 points to your COMBAT SKILL.',
       'Mindshield':'The Darklords and many of the evil creatures in their command have the ability to attack you using their Mindforce. The Kai Discipline of Mindshield prevents you from losing any ENDURANCE points when subjected to this form of attack.',
       'Mindblast':'This enables a Kai Lord to attack an enemy using the force of his mind. It can be used at the same time as normal combat weapons and adds two extra points to your COMBAT SKILL. Not all the creatures encountered on this adventure will be harmed by Mindblast. You will be told if a creature is immune.',
       'Animal Kinship':'This skill enables a Kai Lord to communicate with some animals and to be able to guess the intentions of others.',
       'Mind Over Matter':'Mastery of this Discipline enables a Kai Lord to move small objects with his powers of concentration.'

    }

    #SPECIAL SKILL NOTES
    #'Healing' skill adds +1 END up to max for each non-combat section
    #'weaponskill' grants 2 points to CS for randomly chosen weapon
    #0=dagger, 1=spear, 2=mace, 3=short sword, 4=warhammer, 5=sword 6=axe, 7=sword, 8=quarterstaff, 9=broadsword
    #'Mindshield' negates enemy 'Mindforce' attacks
    #'Mindblast' adds 2 points to CS unless enemy is immune
    
    #will need to add a check in each non-combat encounter if player has chosen healing
    #check for weapon matching weaponskill 
    #combat encounters will need to check for mindblast immunity as well as checking for mindshield if enemy has mindforce attacks



    
    @staticmethod
    def printSkills():
        for key in Skills.skills.keys():
            print(key)

    @staticmethod
    def skillDesc(name):
        description = Skills.skills.get(name)
        return description
    
    @staticmethod
    def addSkill(self, character: Character, skillName) -> str:
        character.skills.append(skillName)
    

        
        

                

    



if __name__ == "__main__":
    Skills.printSkills()
    
    
    
    
    
    
    
    
    
    ##EXAMPLE USAGES
    # player = Character()
    # print(f"Initial stats: Endurance={player.endurance}, CombatSkill={player.combatSkill}")


    # player.statChange(5, "endurance")
    # player.statChange(-3, "combatSkill")
    # print(f"Updated stats: Endurance={player.endurance}, CombatSkill={player.combatSkill}")
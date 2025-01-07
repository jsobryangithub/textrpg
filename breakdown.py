####ADVENTURE RPG####

####BASIC STUFF TO ADD###
#help menu to display current stats, equipment, skill definitions, etc
#encounters / combat system
#initial setup (introduction text, show starting stats, equipment)
#skill descriptions / let player choose which skills to add

####LONG TERM GOALS####
#make it a web-based app
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
    gold: int = 0
    equipment = []
    items = []
    skills = []

    def __post_init__(self):
        enduranceStat = random.randint(0,10) + 20
        self.Maxendurance = enduranceStat
        self.endurance = enduranceStat
        self.combatSkill = random.randint(0,10) + 10
        self.gold = random.randint(0,10)

#skill choices


#starting equipment
#axe, meal, goldcrowns

#random choice of items

#player functions

    def statChange(self, value: int, statName: str):
        # Modify the specified stat
        if statName == "endurance":
            self.endurance += value
        elif statName == "combatSkill":
            self.combatSkill += value
        else:
            raise ValueError(f"Invalid stat name: {statName}")
        



###How Much Can You Carry?
# Weapons
# The maximum number of weapons that you may carry is two.
# Backpack Items
# These must be stored in your Backpack. Because space is limited, you may only keep a maximum of eight articles, including Meals, in your Backpack at any one time.
# Special Items
# Special Items are not carried in the Backpack. When you discover a Special Item, you will be told how to carry it.
# Gold Crowns
# These are always carried in the Belt Pouch. It will hold a maximum of fifty crowns.
# Food
# Food is carried in your Backpack. Each Meal counts as one item.
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
class Skills:
    skillName = str
    skillDefinition = str

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
import random, time
from tkinter import * 

# The base skill set of all characters
 skills = {
        'Accounting': 10,
        'Anthropology': 0,
        'Archaeology': 0,
        'Astronomy': 0,
        'Bargain': 5,
        'Botany': 0,
        'Camoflauge': 25,
        'Chemistry': 0,
        'Climb': 40,
        'Credit Rating': 15,
        'Cthulhu Mythos': 0,
        'Debate': 10,
        'Diagnose Disease': 5,
        'Dodge': 'DEX * 2',
        'Drive Automobile': 20,
        'Electrical Repair': 10,
        'Fast Talk': 5,
        'First Aid': 30,
        'Geology': 0,
        'Hide': 10,
        'History': 20,
        'Jump': 25,
        'Law': 5,
        'Library Use': 25,
        'Linguist': 0,
        'Listen': 25,
        'Make Maps': 10,
        'Mechanical Repair': 20,
        'Occult': 5,
        'Operate Heavy Machinery': 0,
        'Oratory': 5,
        'Pharmacy': 0,
        'Photography': 10,
        'Pick Pocket': 5,
        'Pilot Aircraft': 0,
        'Psychoanalysis': 0,
        'Psychology': 5,
        'Read/Write English': 'EDU * 5',
        'Read/Write ...': 0,
        'Read/Write ...': 0,
        'Read/Write ...': 0,
        'Ride': 5,
        'Sing': 5,
        'Sneak': 10,
        'Speak ...': 0,
        'Speak ...': 0,
        'Spot Hidden': 25,
        'Swim': 25,
        'Throw': 25,
        'Track': 10,
        'Treat Disease': 5,
        'Treat Poison': 5,
        'Zoology': 0
    }

# Roll 3d6 for 5 times to create the statistics for str, dex, con, app, and pow. 
# Also, give the player the option to reroll 3 times to make up for potentially crummy rolls. 
def rollDice():
    reroll = 'y'
    rerollAmt = 1
    input("Press enter when you're ready to roll your statistics...")
    while True:
        print("Rolling 3d6 5 times...")
        time.sleep(2)
        
        rollOne = random.randint(3, 18)                       
        rollTwo = random.randint(3, 18)                       
        rollThree = random.randint(3, 18)                     
        rollFour = random.randint(3, 18)                      
        rollFive = random.randint(3, 18)                      

        print("You have rolled the following: ", rollOne, rollTwo, rollThree, rollFour, rollFive)

        if rerollAmt <= 2:
            print("You may roll your stats up to " + str(3 - rerollAmt) + " more times. \nWould you like to reroll? (y/n) ")
            pass
        else:
            print("You can no longer reroll.")
            break

        reroll = input()
        if reroll == 'y':
            rerollAmt += 1
            pass
        elif reroll == 'n':
            break
        else:
            print("Incorrect input.")
            time.sleep(1)
    return [rollOne, rollTwo, rollThree, rollFour, rollFive]

# Assigns statistics either in order rolled or order chosen by player
def assignStats(rolledStats):
    while True:
        charStats = []
        print("You statistics you have rolled for are Strength, Dexterity, Constitution, \nAppearance, and Power.\nYour stats are currently assigned as:"
            "\nStrength", str(rolledStats[0]),
            "\nDexterity", str(rolledStats[1]),
            "\nConstitution", str(rolledStats[2]),
            "\nAppearance", str(rolledStats[3]),
            "\nPower", str(rolledStats[4]),
            "\nWould like like to assign your stats in their present order? (y/n) ")
        randomStats = input()

        if randomStats == 'y':
            charStats = rolledStats
            break
        elif randomStats == 'n':
            chooseStats = rolledStats
            statList = ["Strength", "Dexterity", "Constitution", "Appearance", "Power"]
            for stat in statList:
                print("Set " + stat + " as: ", str(chooseStats))
                choice = input()
                while int(choice) not in chooseStats:
                    time.sleep(2)
                    print("Invalid option.\nSet " + stat + " as: ", str(chooseStats))
                    choice = input()
                charStats.append(int(choice))
                i = 0
                while i <= 5:
                    if int(choice) == chooseStats[i]:
                        del chooseStats[i]
                        break
                    else:
                        i += 1
            break
        else:
            print(randomStats + " is not a valid choice.")
            time.sleep(2)
    print(charStats)
    return charStats

# Sets skill selections based on what player indicates
def selectSkills():
   pass

# Welcomes player to program and explains CoC character gen. basics
def welcome():
    print("Welcome to Amaryllis' Call of Cthulhu (3rd Ed.) character generator!",
    "***PLEASE READ INSTRUCTIONS CAREFULLY TO ENSURE YOU GET THE CHARACTER YOU WANT***",
    "This character generator anticipates that you have a physical copy of the character",
    "sheet and a pencil with you as you create your character, as no information will be",
    "saved after the program is closed. At the end of the program, all generated",
    "character information will be displayed for you to transcribe to your character's",
    "sheet.",
    "This program is maintained on a voluntary basis, so please report any errors you",
    "obtain, but the issue may not be fixed in a timely manner. This program was created", 
    "with Python 3.4.",
    "This character generator is intended for creating highschool-aged",
    "characters. As such, all EDU stats will be set to 12. Instead of choosing a",
    "profession, you will be selecting a club for your skills.")
    input('Press enter to continue...')

    print("You may have heard of Call of Cthulhu characters as 'Investigators' before.",
    "This is reflects the main goal of all CoC players: to investigate. Before you",
    "start creating your character, you should consider what type of person you want",
    "your character to be and what the best type of character to unfold mysteries might",
    "be.",
    "For instance, you may conclude that being a Detective or Private Eye is the best",
    "way to go, as you will have the skills Sneak, Spot Hidden, and Hide (among others),"
    "which will make it easier to find secret stair cases and spy upon crazed cultists."
    "Your compatriot might conclude that being a Historian is the best, since the skills",
    "Make Maps and Read/Write Other Language will make is easier to document hidden",
    "catacombs and decipher ancient texts of mythos. Ultimately, no one career path is",
    "superior to another. The advantage comes from the quick wit of the player and their",
    "use of the skills at their disposal.",
    "Since your character is a highschooler, instead of choosing a career path, you'll be",
    "choosing an after-school club to be a part of to obtain your skill set.")
    input("Press enter to continue...")

# Descriptions of the career paths for skill set selection
def afterSchoolClubs():
    clubs = {
        'Creative Writing': ['History', 'Library Use', 'Oratory', 'Psychology','Read/Write English', 'Read/Write ...', '']
    }

welcome()
rolledStats = rollDice()
charStats = assignStats(rolledStats)
print(rolledStats)
input('Press enter to end program')
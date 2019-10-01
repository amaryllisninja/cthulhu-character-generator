import random, time
from tkinter import * 

# The base skill set of all characters
 skills = {
    'Art': 0,
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
    "Make Maps and Read/Write Read/Write ... will make is easier to document hidden",
    "catacombs and decipher ancient texts of mythos. Ultimately, no one career path is",
    "superior to another. The advantage comes from the quick wit of the player and their",
    "use of the skills at their disposal.",
    "Since your character is a highschooler, instead of choosing a career path, you'll be",
    "choosing an after-school club to be a part of to obtain your skill set.")
    input("Press enter to continue...")

# Descriptions of the career paths for skill set selection
def afterSchoolClubs():
    clubs = {
        'Advanced Placement': ['Bargain', 'Credit Rating', 'Library Use', 'Read/Write ...', 'Persuade', 'Psychology','Anthropology', 'Archaeology', 'Astronomy', 'Biology', 'Chemistry', 'Electronics', 'Geology', 'History', 'Law', 'Medicine', 'Natural History', 'Physics'],
        'Antiquarian': ['Art', 'Bargain', 'Craft', 'History', 'Library Use', 'Read/Write ...', 'Spot Hidden'],
        'Art': ['Art', 'Craft', 'Fast Talk', 'History', 'Photography', 'Psychology', 'Spot Hidden'],
        'Athletics': ['Climb', 'Dodge', 'Jump', 'Martial Arts', 'Ride', 'Swim', 'Throw'],
        'Band': ['Art', 'Bargain', 'Craft', 'Fast Talk', 'Listen', 'Persuade', 'Psychology'],
        'BSA': ['Dodge', 'First Aid', 'Hide', 'Listen', 'Mechanical Repair', 'Rifle', 'Sneak'],
        'Creative Writing': ['History', 'Library Use', 'Occult', 'Read/Write ...', 'Read/Write English', 'Persuade', 'Psychology'],
        'Crime Theory': ['Bargain', 'Disguise', 'Fast Talk', 'Handgun', 'Locksmith', 'Sneak', 'Spot Hidden'],
        'Detective': ['Bargain', 'Fast Talk', 'Law', 'Listen', 'Persuade', 'Psychology', 'Spot Hidden'],
        'Drama': ['Art', 'Credit Rating', 'Disguise', 'Dodge', 'Fast Talk', 'Listen', 'Psychology'],
        'Farming': ['Craft', 'Electrical Repair', 'First Aid', 'Mechanical Repair', 'Natural History', 'Operate Heavy Machine', 'Track'],
        'Journalism': ['Fast Talk', 'History', 'Library Use', 'Read/Write English', 'Persuade', 'Photography', 'Psychology'],
        'Law and Order': ['Bargain', 'Credit Rating', 'Fast Talk', 'Law', 'Library Use', 'Persuade', 'Psychology'],
        'Missionary': ['Art', 'Bargain', 'Craft', 'First Aid', 'Mechanical Repair', 'Medicine', 'Natural History', 'Persuade'],
        'Medical Sciences': ['Biology', 'Credit Rating', 'First Aid', 'Latin', 'Medicine', 'Pharmacy', 'Psychoanalysis', 'Psychology'],
        'No Club': ['Art', 'Craft', 'Credit Rating', 'Read/Write ...', 'Ride', 'Shotgun'],
        'Parapsychology': ['Anthropology', 'History', 'Library Use', 'Occult', 'Read/Write ...', 'Photography', 'Psychology'],
        'Pilot': ['Astronomy', 'Electrical Repair', 'Mechanical Repair', 'Navigate', 'Operate Heavy Machine', 'Physics', 'Pilot'],
        'Police': ['Dodge', 'Fast Talk', 'First Aid', 'Grapple', 'Law', 'Psychology', 'Bargain', 'Drive Automobile', 'Martial Arts', 'Ride', 'Spot Hidden'],
        'Private Eye': ['Bargain', 'Fast Talk', 'Law', 'Library Use', 'Locksmith', 'Photography', 'Psychology'],
        'Religious Studies': ['Accounting', 'History', 'Library Use', 'Listen', 'Read/Write ...', 'Persuade', 'Psychology'],
        'Robotics': ['Chemistry', 'Electrical Repair', 'Geology', 'Library Use', 'Mechanical Repair', 'Operate Heavy Machine', 'Physics'],
        'ROTC': ['Accounting', 'Bargain', 'Credit Rating', 'Law', 'Navigate', 'Persuade', 'Psychology'],
        'Urban Exploration': ['Bargain', 'Fast Talk', 'Hide', 'Listen', 'Natural History', 'Psychology', 'Sneak'],
    }
    clubDesc = {
        'Advanced Placement': "This club is for those with their sights set on an ivy league college. It is an intensive learning club, where college level classes are taken regularly.",
        'Antiquarian': "A club for those into antiques and thrift store crawling.",
        'Art': "A club for painters, sculpters, and all other mixed media artists.",
        'Athletics': "The club for the football, basketball, baseball, and other sports players. They meet up regularly to exercise and talk strategy.",
        'Band': "A club for all school musicians.",
        'BSA': "The longest running club of the school for the boys and girls in Scouts. They regularly have camping trips.",
        'Creative Writing': "For all the aspiring authors to gather and bounce ideas off of each other.",
        'Crime Theory': "A club for those with a fascination with the criminal mind and how it works.",
        'Detective': "For those that are interested in solving cold cases and unsolvable crimes.",
        'Drama': "A club for those with a dramatic flair. They have a performance at the end of each semester.",
        'Farming': "A club for those with an interest in ",
        'Journalism': "The club for intrepid reports with a story to find.",
        'Law and Order': ,
        'Missionary': ,
        'Medical Sciences': ,
        'No Club': ,
        'Parapsychology': ,
        'Pilot': ,
        'Police': ,
        'Private Eye': ,
        'Religious Studies': ,
        'Robotics': ,
        'ROTC': ,
        'Urban Exploration': ,
    }

welcome()
rolledStats = rollDice()
charStats = assignStats(rolledStats)
print(rolledStats)
input('Press enter to end program')
# Rebekah shi
# 2/8/24
# Basic TTRPG Project 2
import random

global score


def get_name():
    character_name = input("Please input your character name: ")
    print(character_name)
    return character_name


get_name()

sum_of_list = 0


def sum_of_four_six_side_dice_with_lowest_dropped():
    random_list = [random.randint(1, 6), random.randint(1, 6), random.randint(1, 6), random.randint(1, 6)]
    random_list.remove(min(random_list))
    # declaring as global to acess later on
    global sum_of_list
    sum_of_list = sum(random_list)
    return sum_of_list


def score_modifier(s):
    s = input("Enter your unmodified score: ")
    s = int(s)
    s = (s - 10)
    s = s / 2
    s = int(s)
    print("Here is your modified score: " + str(s))
    return int(s)


# assign traits
trait = ["strength", "dexterity", "constitution", "intelligence", "wisdom", "charisma"]

# score modifier


for value in trait:
    score_list = []
    score = sum_of_four_six_side_dice_with_lowest_dropped()
    print("here is your unmodified score for " + value + ":" + str(score))
    score = int(score)
    score = score_modifier(score)

    if value == "strength":
        strength = score

    if value == "dexterity":
        dex = score

    if value == "constitution":
        con = score

    if value == "intelligence":
        intel = score

    if value == "wisdom":
        wise = score

    if value == "charisma":
        charm = score


def treasure():
    treasure_type = random.randint(1,3)
    if treasure_type == 1:
       print("Gems")
    if treasure_type == 2:
       print("Gold and Silver")
    if treasure_type == 3:
        print("Jade and gold figurines")
    return treasure_type

def menu():
    print("Pick an action:\n")
    print("Attack, enter 1\n")
    print("Negotiate, enter 2\n")
    print("Search, enter 3\n")
    print("Eat enter 4\n")
    action = input("Enter your input")
    action = int(action)
    if action == 1:
        roll_die = random.randint(1, 20)
        if strength > dex and roll_die + strength >= 12 or dex > strength and roll_die + dex >= 12:
            print("Hit!")
        if strength > dex and roll_die + strength < 12 or dex > strength and roll_die + dex < 12:
            print("Missed")

    if action == 2:
        roll_die = random.randint(1, 20)
        total = int(charm) + roll_die
        if total >= 15:
            print("Negotiations Sucessful, truce")
        else:
            print("Negotiations Failed")

    if action == 3:
        roll_die = random.randint(1, 20)
        if intel > wise and roll_die + intel >= 12 or wise > intel and roll_die + wise >= 12:
            print("Treasure!")
            treasure()
        else:
            print("Nothing found")

    if action == 4:
        print("Food was rancid")
        roll_die = random.randint(1, 20)
        if roll_die + int(con) >=10:
            print("Congrats! You can handle the food.")
        else:
            print("You got sick. Stay in bed")
i = 0
while i < 4:
    menu()
    i = i + 1










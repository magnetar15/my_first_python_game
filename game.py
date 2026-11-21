# Project Exam: “Survive 5 Days on the Island”
# Create a game in which the player tries to survive on an island for five days.
#     At the beginning of each expedition, the player enters their name.
import sys
import random
import subprocess


# Starting an Expedition
# At the beginning of each expedition, the player has:
# - 100 health points;
# - 3 portions of food;
# - 3 portions of water;
# - 0 exploration points.
# The goal is to stay alive for five days. The player loses if their health reaches 0.
day = 1
action = 0
STATUS = 0
name = ""
stats = {
            "hp": 100,
            "food": 3,
            "water": 3,
            "exploration points": 0
        }

def easter_egg(text): # EASTER EGG FOR A FRIEND
    if sys.platform == "win32": # EASTER EGG FOR A FRIEND
        subprocess.run(["clip"], input=text.encode("utf-16le"), check=True) # EASTER EGG FOR A FRIEND
    elif sys.platform == "darwin": # EASTER EGG FOR A FRIEND
        subprocess.run(["pbcopy"], input=text.encode("utf-8"), check=True)# EASTER EGG FOR A FRIEND
    else:# EASTER EGG FOR A FRIEND
        subprocess.run(["xclip", "-selection", "clipboard"], input=text.encode("utf-8"), check=True)# EASTER EGG FOR A FRIEND




def insert_name():
    while True:
        special_characters = "!@#$%^&*()_-=+:\"|?><,."
        global name
        name = input("Insert your name : ").capitalize().strip()
        has_special = False
        for i in special_characters:
            if name.find(i) != -1:
                has_special = True
        if name == "":
            print("Name can't be empty")
            continue
        elif has_special == True:
            print("Name cannot contain special characters")
            continue
        elif name.isdigit() == True:
            print("The name can't be numeric")
            continue
        elif len(name) < 3:
            print("The name is too short")
            continue
        elif name == "Andra":  # EASTER EGG FOR A FRIEND
            print("Hei Andra, iti multumesc ca imi incerci jocul")  # EASTER EGG FOR A FRIEND
            print(
                "Tocmai ai deblocat un EASTER EGG !\n Deschide browserul si unde se introduce linkul\n apasa CTRL + V")  # EASTER EGG FOR A FRIEND
            easter_egg("https://i.imgur.com/xO56E2c.jpeg")  # EASTER EGG FOR A FRIEND
            input("Press ENTER to continue")  # EASTER EGG FOR A FRIEND
            break  # EASTER EGG FOR A FRIEND
        else:
            print("Hello World and Hello", name)
            input("Press ENTER to continue")
            break

def intro():
    print("Hello", name)
    print("Your planes has crashed and now you're stuck on this island")
    print("You have to survive for 5 days until the rescue crew arrives")
    print("Good luck")
    print("+3 water bottles")
    print("+3 Food portions")
    print("HP : 100")
    input("Press ENTER to continue")
    return

def day_passed():
    global stats
    global day
    if stats["hp"] > 0:
        print("The day has passed")
        day = day + 1
        print(f"Day : {day}")
        print(f"HP : {stats['hp']}")
        print(f"Food : {stats['food']} Water : {stats['water']}")
        input("Press ENTER to continue")
        return(day)

#1. Search for food: Receive a random amount of 1 to 3 portions of food, but lose 5 health points.
def search_food():
    global stats
    print("Searching for food..")
    x = random.randint(1, 3)
    print("You found", x, "portions of food")
    stats["food"] = stats["food"] + x
    if stats["hp"] >= 5:
        stats["hp"] = stats["hp"] - 5
    elif stats["hp"] < 5:
        stats["hp"] = 0
    if stats["hp"] == 0:
        return (stats["hp"], stats["food"], 5)
    elif stats["hp"] > 0:
        return (stats["hp"], stats["food"], 1)
    else:
        return (stats["hp"], stats["food"], 0)

#2. Search for water: Receive a random amount of 1 to 3 portions of water, but lose 5 health points.
def search_water():
    global stats
    print("Searching for water..")
    x = random.randint(1, 3)
    print("You found", x, "water bottles")
    stats["water"] = stats["water"] + x
    if stats["hp"] >= 5:
        stats["hp"] = stats["hp"] - 5
    elif stats["hp"] < 5:
        stats["hp"] = 0
    if stats["hp"] == 0:
        return (stats["hp"], stats["water"], 5)
    if stats["hp"] > 0:
        return (stats["hp"], stats["water"], 1)
    else:
        return (stats["hp"], stats["water"], 0)

#3. Rest: Recover 20 health points, up to a maximum of 100.
def rest():
    global stats
    if stats["hp"] < 80:
        print("You rest for a bit...")
        stats["hp"] = stats["hp"] + 20
        print("HP:", stats["hp"])
        input("Press ENTER to continue")
        return (stats["hp"], 1)
    elif stats["hp"] >= 80 and stats["hp"] < 100:
        print("You rest for a bit...")
        stats["hp"] = 100
        print("HP:", stats["hp"])
        input("Press ENTER to continue")
        return (stats["hp"], 1)
    elif stats["hp"] == 100:
        print("You have enough energy")
        input("Press ENTER to continue")
        return(stats["hp"], 0)

#4. Explore the island: One of these events happens at random, with equal chances:
#   - Find 2 portions of food and gain 10 exploration points.
#   - Find 2 portions of water and gain 10 exploration points.
#   - Get injured and lose 15 health points.
#An invalid choice does not use up the day; the player is asked to choose again.
    # After the action, the program displays the player’s remaining health and resources.
    # If the player is still alive, they move on to the next day.

def explore_island():
    global stats
    while True:
        z = random.choice(["a", "b", "c"])
        if z == "a":
            print("You found food!")
            print("+2 Food portions")
            print("+10 Exploration points")
            stats["food"] = stats["food"] + 2
            stats["exploration points"] = stats["exploration points"] + 10
            input("Press ENTER to continue")
            return (stats["food"], 1)
        elif z == "b":
            print("You found water!")
            print("+2 Water bottles")
            print("+10 Exploration points")
            stats["water"] = stats["water"] + 2
            stats["exploration points"] = stats["exploration points"] + 10
            input("Press ENTER to continue")
            return (stats["water"], 1)
        elif z == "c":
            print("You got injured while exploring")
            print("You took damage")
            if stats["hp"] > 15:
                stats["hp"] = stats["hp"] - 15
                print("HP left :", stats["hp"])
                return (stats["hp"], 1)
            elif stats["hp"] == 15:
                stats["hp"] = 0
                print("HP left :", stats["hp"])
                return (stats["hp"], 5)
            elif stats["hp"] < 15:
                stats["hp"] = 0
                print("HP left :", stats["hp"])
                return (stats["hp"], 5)

# Each Day
# At the beginning of each day, the player consumes one portion of food and one portion of water.
# - If the player has the required resource, that resource decreases by one portion.
# - If the player does not have food or water, their health decreases by 15 points for each missing resource.
# - Resources cannot drop below 0, and health cannot drop below 0 or rise above 100.
# - If health reaches 0, the expedition ends in a loss.
def daily_consume(food, water, hp):
    global stats
    print("A new day, a new me")
    print("I'm hungry and thirsty")
    if food > 0:
        stats["food"] = stats["food"] - 1
        print("I ate a portion of food")
    elif food == 0 and stats["hp"] > 15:
        stats["hp"] = stats["hp"] - 15
        print("I don't have any food")
        print("--you took damage--")
        print("HP left :", stats["hp"])
    elif food == 0 and stats["hp"] <= 15:
        print("I don't have any food")
        print("--you took damage--")
        return (stats["hp"], stats["food"], stats["water"], 5)
    if water > 0:
        stats["water"] = stats["water"] - 1
        print("I drank a bottle of water")
        return (stats["hp"], stats["food"], stats["water"], 0)
    elif food == 0 and stats["water"] > 15:
        stats["water"] = stats["water"] - 15
        print("I don't have any water")
        print("--you took damage--")
        print("HP left :", stats["hp"])
        return (stats["hp"], stats["food"], stats["water"], 0)
    elif food == 0 and stats["hp"] <= 15:
        print("I don't have any water")
        print("--you took damage--")
        return (stats["hp"], stats["food"], stats["water"], 5)

# Main Menu
# The program displays this menu and returns to it after each action:
# 1. Start a new expedition
# 2. View expedition history
# 3. View statistics
# 4. Quit
while True:
    print("""
    1. Incepe o expeditie noua
    2. Vezi istoricul expeditiilor
    3. Vezi statisticile
    4. Iesire
    """)
    choice = input("Alege o optiune")
    if choice == "1":
        while True:
            if day == 1:
                insert_name()
                intro()
#If the player is still alive, they choose one action for that day:
#2. Search for water: Receive a random amount of 1 to 3 portions of water, but lose 5 health points.
#3. Rest: Recover 20 health points, up to a maximum of 100.
#4. Explore the island: One of these events happens at random, with equal chances:
            print("""
            1. Search food 
            2. Search water
            3. Rest
            4. Explore the island
            5. Quit
            """)
            action = input("Chose an option")
            if day == 6:
                action = "9"

            if STATUS == 5:
                print("You died !")
                break
            if action == "1":
                stats["hp"], stats["food"], STATUS = search_food()
                if STATUS == 1:
                    day = day_passed()
                    daily_consume()
                    action = "0"
                elif STATUS == 0:
                    action = "0"
                    continue
                else:
                    continue

            elif action == "2":
                stats["hp"], stats["water"], STATUS = search_water()
                if STATUS == 1:
                    day = day_passed()
                    daily_consume()
                    action = "0"
                elif STATUS == 0:
                    action = "0"
                    continue
                else:
                    continue

            elif action == "3":
                rest()
                stats["hp"], STATUS = search_food()
                if STATUS == 1:
                    day = day_passed()
                    daily_consume()
                    action = "0"
                    continue
                elif STATUS == 0:
                    action = "0"
                    continue

            elif action == "4":
                explore_island()
                if STATUS == 1:
                    day = day_passed()
                    daily_consume()
                    action = "0"
                elif STATUS == 0:
                    action = "0"
                    continue
                else:
                    continue
            elif action == "5":
                sys.exit()
            elif action == "0":
                continue
            elif action == "9":
                print("Congratulations, you survived")
                print("Rescue team is arriving")
                print("")
            else:
                print("Invalid option")
                continue


    elif choice == "2":
        pass
    elif choice == "3":
        pass
    elif choice == "4":
        sys.exit("See you soon")
    elif choice == "0":
        continue
    else:
        print("Optiune invalida")
        continue

# Istoric și statistici
# Istoricul păstrează expedițiile desfășurate de la pornirea programului. Pentru fiecare, afișează:
# - numele jucătorului;
# - rezultatul: câștigată sau pierdută;
# - numărul de zile supraviețuite;
# - scorul final.
# Statisticile afișează numărul expedițiilor, câte au fost câștigate și pierdute,
#  cel mai mare și cel mai mic scor, totalul punctelor și media scorurilor.

# Dacă jucătorul cere istoricul sau statisticile înainte să termine vreo expediție,
#  programul afișează un mesaj potrivit. Istoricul trebuie să rămână disponibil cât timp programul rulează.

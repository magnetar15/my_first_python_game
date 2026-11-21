# Examen-proiect: „Supraviețuiește 5 zile pe insulă”
# Creează un joc în care jucătorul încearcă să supraviețuiască pe o insulă timp de 5 zile. La începutul fiecărei expediții,
#  jucătorul își introduce numele.
# Meniul principal
# Programul afișează meniul și îl readuce după fiecare acțiune:
# 1. Începe o expediție nouă
# 2. Vezi istoricul expedițiilor
# 3. Vezi statisticile
# 4. Ieșire
# Dacă jucătorul introduce o opțiune care nu există, programul îi afișează un mesaj și îi cere din nou să aleagă.
import sys
import random

day = 1
action = 0



# Începutul expediției
# La începutul fiecărei expediții, jucătorul are:
# - 100 de puncte de sănătate;
# - 3 porții de hrană;
# - 3 porții de apă;
# - 0 puncte de explorare.
# Scopul este să rămână în viață timp de 5 zile. Jucătorul pierde dacă sănătatea ajunge la 0.
# Desfășurarea unei zile
# La începutul fiecărei zile, jucătorul consumă o porție de hrană și una de apă.
# - Dacă are resursa necesară, aceasta scade cu o porție.
# - Dacă nu are hrană sau apă, sănătatea scade cu 15 puncte pentru fiecare resursă lipsă.
# - Resursele nu pot scădea sub 0, iar sănătatea nu poate scădea sub 0 sau depăși 100.
# - Dacă sănătatea ajunge la 0, expediția se încheie ca pierdută.
# Dacă jucătorul este încă în viață, alege o acțiune pentru ziua respectivă:
# 1. Caută hrană: primește aleatoriu între 1 și 3 porții de hrană, dar pierde 5 puncte de sănătate.
# 2. Caută apă: primește aleatoriu între 1 și 3 porții de apă, dar pierde 5 puncte de sănătate.
# 3. Odihnește-te: recuperează 20 de puncte de sănătate, fără să depășească 100.
# 4. Explorează insula: are loc aleatoriu unul dintre următoarele evenimente, cu șanse egale:
#    - găsește 2 porții de hrană și câștigă 10 puncte de explorare;
#    - găsește 2 porții de apă și câștigă 10 puncte de explorare;
#    - se rănește și pierde 15 puncte de sănătate.
# O alegere invalidă nu consumă ziua; jucătorului i se cere să aleagă din nou. După acțiune,
#  programul afișează sănătatea și resursele rămase. Dacă jucătorul rămâne în viață, trece la ziua următoare.


# Jucătorul câștigă dacă supraviețuiește până la sfârșitul zilei a cincea.
# Scorul expediției
# La sfârșitul fiecărei expediții, câștigată sau pierdută, se calculează scorul astfel:
# - 10 puncte pentru fiecare zi supraviețuită;
# - se adaugă sănătatea rămasă;
# - se adaugă 5 puncte pentru fiecare porție rămasă de hrană sau apă;
# - se adaugă punctele de explorare câștigate.
# Programul afișează dacă jucătorul a câștigat sau a pierdut, câte zile a supraviețuit și scorul final.
def scenario1():
    global stats
    stats["food"] = stats["food"] + 2
    stats["exploration points"] = stats["exploration points"] + 10
    print("You found 2 portions of food")
    return (stats["exploration points"], stats["food"])
def scenario2():
    global stats
    stats["water"] = stats["water"] + 2
    stats["exploration points"] = stats["exploration points"] + 10
    print("You found 2 bottles of water")
    return (stats["exploration points"], stats["water"])

def explore_island():
    global stats
    z = random.choice("a", "b")
    if z == "a":
        scenario1()
        return(1)
    elif z == "b":
        scenario2()
        return(1)
    else:
        print("invalid option")
        return(0)


def day_passed():
    global stats
    global day
    if stats["hp"] > 0:
        print("The day has passed")
        day = day + 1
        print(f"Day : {day}")
        print(f"HP : {stats['hp']}")
        print(f"Food : {stats['food']} Water : {stats['water']}")

def rest():
    global stats
    if stats["hp"] < 80:
        print("You rest for a bit...")
        stats["hp"] = stats["hp"] + 20
        return (stats["hp"])
    elif stats["hp"] > 80 and stats["hp"] < 100:
        print("You rest for a bit...")
        stats["hp"] = 100
        return (stats["hp"])
    elif stats["hp"] == 100:
        print("You have enough energy")


def search_food():
    print("Searching for food..")
    x = random.randint(1, 3)
    print("You found", x, "portions of food")
    global stats
    stats["hp"] = stats["hp"] - 5


def search_water():
    print("Searching for water..")
    x = random.randint(1, 3)
    print("You found", x, "water bottles")
    global stats
    stats["hp"] = stats["hp"] - 5


def daily_consume(food, water, hp):
    if food > 0:
        stats["food"] -= 1
        print("You eaten a portion of food")
    elif food == 0 and hp >= 15:
        print("You didn't had enough food, you take 15 damage")
    elif food == 0 and hp == 15:
        print("You didn't had enough food you took 15 damage and you died")
        return (stats["food"], stats["water"], stats["hp"])
    if water > 0:
        stats["water"] -= 1
        print("You drank a bottle of water")
        return(stats["food"], stats["water"], stats["hp"])
    elif water == 0:
        print("you didn't had enough water, you take 15 damage")
    elif water == 0 and hp == 15:
        print("You didn't had enough water you took 15 damage and you died")
        return(stats["food"], stats["water"], stats["hp"])


while True:
    print("""
    1. Incepe o expeditie noua
    2. Vezi istoricul expeditiilor
    3. Vezi statisticile
    4. Iesire
    """)
    choice = input("Alege o optiune")
    if choice == "1":
        stats = {
            "hp": 100,
            "food": 3,
            "water": 3,
            "exploration points": 0
        }
        while True:
            print("""
            1. Search food
            2. Search water
            3. Rest
            4. Explore the island
            5. Quit
            """)
            action = input("Chose an option")
            if action == "1":
                pass
            elif action == "2":
                pass
            elif action == "3":
                pass
            elif action == "4":
                pass
            elif action == "5":
                sys.exit()


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

import random
import csv

class Character:
    def __init__(self, name, health, attack):
        self.name = name
        self.health = health
        self.attack = attack

    def damage(self, target_character):
        target_character.health -= self.attack

    def is_alive(self):
        return self.health > 0

def getting_info():
    # get  players information

    first_name = input("What will be your trainer name?")
    full_name = first_name
    print(full_name)

    role = input("What group would you like? (FIRE, WATER, GRASS)")

    type = ""
    with open('C:\MySTUDENT\PokemonStarters.csv') as csvfile:
        pokemonreader = csv.reader(csvfile, delimiter=',')
        for row in pokemonreader:

        #print(" ".join(row))
        #print(row[0])
            if row[2] == role:
                if type == "":
                    type = row[1]
                #fire_type = input(row[1])
                else:
                    type =type +" " + row[1]

    valid_input = False
    while valid_input == False:
        #player = Character(type)
        pokemon=input(type)
        player = Character(pokemon, 8888, 1980)
        valid_input = True
        if valid_input == False:
            role = input("Please enter a valid role")


    print("Hello", full_name)
    print("Your pokemon has", player.health, "health")
    print("Your pokemon has", player.attack, "attack")
    print()
    return player

def enemy_info():
    enemy_name = "The wild pokemon"
    enemy_health = random.randint(1000, 2100)
    enemy_attack = random.randint(900, 1160)
    enemy = Character(enemy_name, enemy_health, enemy_attack)
    print("A wild pokemon has appeared")
    print(enemy.name, "has", enemy.health, "health")
    print(enemy.name, "has", enemy.attack, "attack")
    print()
    return enemy

def fight(player, enemy):
    print()
    valid_input = False
    role = input("What type of attack from your group? (fire, water, grass)")


    while valid_input == False:
        if role == "fire":
            print("Choose a move")
            print("1.flamethrower")
            print("2.fire blast")
            print("3.incinerate")
            print("4.heat wave")

            move_selection = int(input("Please enter a valid number from 1 - 4"))
            if move_selection == 1:
                player = Character("flamethrower", 0, 130)
                valid_input = True
            if move_selection == 2:
                player = Character("fire blast", 0, 130)
                valid_input = True
            if move_selection == 3:
                player = Character("incinerate", 0, 130)
                valid_input = True
            if move_selection == 4:
                player = Character("heat wave", 0, 130)
                valid_input = True
            if valid_input == False:
                move_selection = int(input("Please input a valid group"))
        if role == "water":
            print("Choose a move")
            print("1.hydro pump")
            print("2.water pulse")
            print("3.water gun")
            print("4.aquajet")

            move_selection = int(input("Please enter a valid number from 1 - 4"))
            if move_selection == 1:
                player = Character("hydro pump", 0, 130)
                valid_input = True
            if move_selection == 2:
                player = Character("water pulse", 0, 130)
                valid_input = True
            if move_selection == 3:
                player = Character("water gun", 0, 130)
                valid_input = True
            if move_selection == 4:
                player = Character("aquajet", 0, 130)
                valid_input = True
            if valid_input == False:
                move_selection = int(input("Please input a valid group"))
        if role == "grass":
            print("Choose a move")
            print("1.solar beam")
            print("2.vine whip")
            print("3.leaf storm")
            print("4.frenzy plant")

            move_selection = int(input("Please enter a valid number from 1 - 4"))
            if move_selection == 1:
                player = Character("solar beam", 0, 130)
                valid_input = True
            if move_selection == 2:
                player = Character("vine whip", 0, 130)
                valid_input = True
            if move_selection == 3:
                player = Character("leaf storm", 0, 130)
                valid_input = True
            if move_selection == 4:
                player = Character("frenzy plant", 0, 130)
                valid_input = True
            if valid_input == False:
                move_selection = int(input("Please input a valid group"))

def play_game():
    player = getting_info()
    enemy = enemy_info()
    enemy = enemy_info()
    fight(player, enemy)
    fight(player, enemy)
    while player.is_alive() and enemy.is_alive():
        player.damage(enemy)
        enemy.damage(player)
        print("You have", player.health, "health remaining")
        print("Enemy has", enemy.health, "health remaining")
        print()

        if player.is_alive():
            print("You won!")
        elif enemy.is_alive():
            print("You lost!")
        else:
            print("It was a draw")


play_game()

print("Great, you have come so far young trainer. There are alot of Pokemon out there in the world. Gotta catch them all")
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
        #print(type(self.health))
        return self.health > 0

def getting_info():
    # get  players information

    first_name = input("What will be your trainer name?")
    full_name = first_name
    print(full_name)

    role = input("What group would you like? (fire, water, grass)")

    type = ""
    with open('C:/Users/kwanke/PycharmProjects/Pokemon/PokemonStarters.csv') as csvfile:
        pokemonreader = csv.reader(csvfile, delimiter=',')
        for row in pokemonreader:
            if row[2] == role:
                print (row[1])

    valid_input = False
    while valid_input == False:
        # player = Character(type)
        pokemon = input(type)
        with open('C:/Users/kwanke/PycharmProjects/Pokemon/PokemonStarters.csv') as csvfile:
            pokemonreader = csv.reader(csvfile, delimiter=',')
            for row in pokemonreader:
                if row[1] == pokemon:
                    print (pokemon)
                    print (row[4], row[5])
                    hp = int(row[4])
                    attack = int(row[5])
                if row[1] == pokemon:
                    print(row[6])
                    species = row[6]

        player = Character(pokemon, hp, attack)
        valid_input = True
        if valid_input == False:
            role = input("Please enter a valid role")

    print(" ")

    print("Hello", full_name)
    print(" ")
    print("Professor: Welcome to the world of Pokemon")
    print(" ")
    print("Professor: Paul will show you around")
    print(" ")
    print("Paul: Nice to meet you, my name is Paul")
    print(" ")
    print("Paul: Let's go find some Pokemon")
    print(" ")
    print("Go to the grass and soon enough you will find a Pokemon")
    print()
    return player


def enemy_info():
    enemy_name = "The wild pokemon"
    enemy_health = random.randint(35, 70)
    enemy_attack = random.randint(40, 80)
    enemy = Character(enemy_name, enemy_health, enemy_attack)
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
    fight(player, enemy)
    #print(type(player.health), (type(enemy.health)))
    while player.is_alive() and enemy.is_alive():
        player.damage(enemy)
        enemy.damage(player)
        print(" ")
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

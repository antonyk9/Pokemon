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

    test = input("Professor: Hello "+ full_name)
    test = input("Professor: Welcome to the world of Pokemon")
    test = input("Professor: Paul will show you around")
    test = input("Paul: Nice to meet you, my name is Paul")
    test = input("Paul: Let's go find some Pokemon")
    test = input("Paul: Go to the grass and soon enough you will find a Pokemon")
    print()
    return player


def enemy_info():
    enemy_name = "The wild pokemon"
    enemy_health = random.randint(35, 70)
    enemy_attack = random.randint(40, 80)
    enemy = Character(enemy_name, enemy_health, enemy_attack)
    print("A wild pokemon has appeared")
    print(enemy.name, "has", enemy.health, "health and", enemy.attack, "attack")
    print()
    return enemy

def fight(player, enemy):
    print()
    valid_input = False
    role = input("What type of attack from your group? (fire, water, grass)")


    while valid_input == False:
        if role == "fire":
            print("Choose a move")
            print("1.tackle")
            print("2.ember")
            print("3.flame charge")
            print("4.flame wheel")

            move_selection = int(input("Please enter a valid number from 1 - 4"))
            if move_selection == 1:
                player = Character("tackle", 0, 50)
                valid_input = True
            if move_selection == 2:
                player = Character("ember", 0, 45)
                valid_input = True
            if move_selection == 3:
                player = Character("flame charge", 0, 50)
                valid_input = True
            if move_selection == 4:
                player = Character("flame wheel", 0, 60)
                valid_input = True
            if valid_input == False:
                move_selection = int(input("Please input a valid group"))
        if role == "water":
            print("Choose a move")
            print("1.tackle")
            print("2.water gun")
            print("3.bubble")
            print("4.bit")

            move_selection = int(input("Please enter a valid number from 1 - 4"))
            if move_selection == 1:
                player = Character("tackle", 0, 50)
                valid_input = True
            if move_selection == 2:
                player = Character("water gun", 0, 40)
                valid_input = True
            if move_selection == 3:
                player = Character("bubble", 0, 40)
                valid_input = True
            if move_selection == 4:
                player = Character("bite", 0, 60)
                valid_input = True
            if valid_input == False:
                move_selection = int(input("Please input a valid group"))
        if role == "grass":
            print("Choose a move")
            print("1.tackle")
            print("2.vine whip")
            print("3.take down")
            print("4.razor leaf")

            move_selection = int(input("Please enter a valid number from 1 - 4"))
            if move_selection == 1:
                player = Character("tackle", 0, 50)
                valid_input = True
            if move_selection == 2:
                player = Character("vine whip", 0, 45)
                valid_input = True
            if move_selection == 3:
                player = Character("take down", 0, 90)
                valid_input = True
            if move_selection == 4:
                player = Character("razor leaf", 0, 55)
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

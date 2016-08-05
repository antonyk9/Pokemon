with open('C:/MySTUDENT/PokemonMoves.csv') as csvfile:
    pokemonreader = csv.reader(csvfile, delimiter=',')
    for row in pokemonreader:
        if pokemon == fire:
            print(row[1])
        if pokemon == water:
            print(row[2])
        if pokemon == grass:
            print(row[3])

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

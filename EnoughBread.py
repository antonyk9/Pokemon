slices_bread = int(input("How many slices of bread?"))
slices_cheese = int(input("How any slices of cheese?"))
slices_ham = int(input("How many slices of ham?"))
slices_tomatoes = int(input("How many slices of tomatoes?"))
num_students = 8


if slices_bread / 2 >= num_students:
    print("Enough bread!")
else:
    print("Not enough bread.")

if slices_cheese >= num_students:
    print("Enough cheese!")
else:
    print("Not enough cheese.")

if slices_ham >= num_students:
    print("Enough ham!")
else:
    print("Not enough ham.")

if slices_tomatoes >= num_students:
    print("Enough tomatoes!")
else:
    print("Not enough tomatoes.")


enough_bread = slices_bread /2 >= num_students
enough_cheese = slices_cheese >= num_students
enough_ham = slices_ham >= num_students

if enough_bread and enough_cheese and enough_ham:
    print("Sandwiches for everyone")



import random
#guessingisfun
#pokemonisfun

answer = random.randint(0, 20)
print("I am thinking of a number between 0 - 20. Try to find that number.")
guess = int(input("what is your guess?"))

guess_count = 1


while guess != answer:
    if guess > answer:
        guess = int(input("too high...what's your new guess?"))
        guess_count = guess_count + 1
    elif guess < answer:
        guess = int(input("too low...what's your new guess?"))
        guess_count = guess_count + 1
    elif guess == answer:
        print("Correct")
        break
    else:
        guess = int(int(input("What is your guess?")))


print("You guessed the number", guess_count,"times. Good job! Come play again!")
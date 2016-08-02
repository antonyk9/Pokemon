import random

answer = random.randint(0, 20)
guess = int(input("what is your guess?"))
(x) = "number of guess == answer"

while guess != answer:
    if guess > answer:
        guess = int(input("what is your guess?"))
    elif guess < answer:
        guess = int(input("what is your guess?"))
    elif guess == answer:
        print("Correct")
        break
    else:
        guess = int(int(input("What is your guess?")))


print("You guessed the number. Good job! Come back next time!")
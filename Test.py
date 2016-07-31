import random 
import sys 

print("pick a number between 1 and 10") 

computernum = random.randrange(1, 10) 
guess1 = input('My guess is:') 

if guess1 == computernum: 
    print("YOU WIN WELL DONE")
else: 
    print("sorry try again")
    print("YOU HAVE 2 GUESSES REMAINING")
guess2 = input("My second guess is:") 

if guess2 == computernum: 
    print("WOW YOUR AMAZING YOU WIN")
else:
    print("Sorry, one more try")
    print("YOU HAVE ONE FINAL GUESS REMAINING")
guess3 = input("My final guess is:") 

if guess3 == computernum: 
    print("WINNER,WINNER,WINNER,WINNER")
else: 
    print("GAME OVER ")

    print("wanna try again?")

    print("if so here we gooo")
    print("pick a number")

computernum = random.randrange(1, 100) 
guess1 = input('My guess is:') 

if guess1 == computernum: 
    print("YOU WIN WELL DONE")
else: 
    print("sorry try again")
    print("YOU HAVE 2 GUESSES REMAINING")
guess2 = input("my second guess is:") 

if guess2 == computernum: 
    print("WOW YOUR AMAZING YOU WIN")
else: 
    print("sorry, one more try")
    print("YOU HAVE ONE FINAL GUESS REMAINING")
guess3 = input("My final guess is:") 

if guess3 == computernum: 
    print("WINNER,WINNER,WINNER,WINNER")
else: 
    print("GAME OVER YOU LOOSE")
    print("Youre not so good at this then you thought lets step it up a bit ")
    print("Pick a number between 1 and 20")


import random 
import sys 



computernum = random.randrange(1, 20) 
guess1 = input('My guess is:') 

if guess1 == computernum: 
    print("YOU WIN WELL DONE")
else: 
    print("Sorry try again")
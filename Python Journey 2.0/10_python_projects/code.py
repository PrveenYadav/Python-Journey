# Roll dice game
import math
import random

def dice_roll():
    while True:
        a = math.floor(random.random()*100)
        b = math.floor(random.random()*100)
        choice = str(input("Roll the dice(y/n): "))
        if choice == 'y' or choice == 'Y':
            print(f"{a, b}")
        elif choice == 'n' or choice == 'N':
            print(f"{a, b}")
        elif choice == 's' or choice == 'break':
            break
        else:
            print("Invalid choice")   

dice_roll()

def rock_paper():
    while True:
        choicesList = ('r', 'p', 's')
        random_choice = random.choice(choicesList)
        choice = str(input("choose any one(r/p/s): "))

        if choice == 'r' and random_choice == 's':
            print("You Choose: 🪨")
            print("Computer Choose: ✂️")
            print("You Win")
        elif choice == 'p' and random_choice == 'r':
            print("You Choose: 📄")
            print("Computer Choose: 🪨")
            print("You Win")
        elif choice == 's' and random_choice == 'p':
            print("You Choose: ✂️")
            print("Computer Choose: 📄")
            print("You Win")
        elif choice == 'p' and random_choice == 's':
            print("You Choose: 📄")
            print("Computer Choose: ✂️")
            print("You Lose")
        elif choice == 'r' and random_choice == 'p':
            print("You Choose: 🪨")
            print("Computer Choose: 📄")
            print("You Lose")
        elif choice == 's' and random_choice == 'r':
            print("You Choose: ✂️")
            print("Computer Choose: 🪨")
            print("You Lose")
        else:
            print("Please choose right character(r/p/s)")

def rock_paper_game():
    while True:
        choicesList = ('r', 'p', 's')
        random_choice = random.choice(choicesList)
        choice = str(input("choose any one(r/p/s): "))

        if (choice == 'r' and random_choice == 's') or (choice == 'p' and random_choice == 'r') or (choice == 's' and random_choice == 'p'):
            print("You Choose: ", choice)
            print("Computer Choose: ", random_choice)
            print("You Win")
        elif (choice == 'p' and random_choice == 's') or (choice == 'r' and random_choice == 'p') or (choice == 's' and random_choice == 'r'):
            print("You Choose: ", choice)
            print("Computer Choose: ", random_choice)
            print("You Lose")
        elif choice == 'stop':
            break
        else:
            print("Please choose right character(r/p/s)")

# rock_paper()
rock_paper_game()
import random
def game():
    randNum = random.randint(1,50)
    while True:
        luckyNum = int(input("Enter a number(1-50): "))

        if luckyNum == randNum:
            print("You won!")
            break
        elif luckyNum > randNum:
            print("Too high. Try again")
        else:
            print("Too low. Try again")

    print("Thanks for playing!")

game()    
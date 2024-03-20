import random
comp= random.randint(1,6)
player1 = input("Pick a number between 1 and 6:")

if player1== comp:
    print("Correct! They rolled a "+ str(comp))
else:
    print("Wrong! They rolled a " + str(comp))
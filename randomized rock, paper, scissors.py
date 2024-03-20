import random
comp = random.choice(["rock", "paper", "scissors"])
player1 = input("rock, paper, or scissors:")

if player1== "rock" and comp == "paper":
    print("computer wins!") 
elif player1 == "paper" and comp == "scissors":
    print("computer wins!")
elif player1 == "scissors" and comp == "rock":
    print("computer wins!")
elif player1== "paper" and comp == "rock":
    print("player1 wins!") 
elif player1 == "rock" and comp == "scissors":
    print("player1 wins!")
elif player1 == "scissors" and comp == "paper":
    print("computer wins!")
else:
    print("It's a tie!")
    
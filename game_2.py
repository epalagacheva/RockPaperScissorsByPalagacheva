#Simple game rock,paper,scissors; at 3th win user recieves image with "*".
import random
rock = "Rock"
paper = "Paper"
scissors = "Scissors"

grand_prize = 0

player_move = input("Chose [r]ock, [p]aper or [s]cissors:")

if player_move == "r":
    player_move = rock
elif player_move == "p":
    player_move = paper
elif player_move == "s":
    player_move = scissors
else:
    raise SystemExit("Invalid Input. Try again...")

    
comp_move = random.randrange(0,2)

if comp_move == 0:
    comp_move = rock
    print("The computer chose Rock.")
        
elif comp_move == 1:
    comp_move = paper
    print("The computer chose Paper.")
elif comp_move == 2:
    comp_move = scissors
    print("The computer chose Scissors.")

if (player_move == rock and comp_move == scissors) or (player_move == paper and comp_move == rock) or \
        (player_move == scissors and comp_move == paper):
    print("You win!")
    

elif player_move == comp_move:
    print("Draw")
    

else:
    print("You lose!")


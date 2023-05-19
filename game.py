import random
rock = "Rock"
paper = "Paper"
scissors = "Scissors"

player_move = input("Chose [r]ock, [p]aper or [s]cissors:")

if player_move == "r":
    player_move = rock
elif player_move == "p":
    player_move = paper
elif player_move == "s":
    player_move = scissors
else:
    raise SystemExit("Invalid Input. Try again...")

computer_move = ""
for move in range (1, 4):
    comp_move = random.randrange(1)

if comp_move == 1:
    comp_move = rock
elif comp_move == 2:
    comp_move = paper
elif comp_move == 3:
    comp_move = scissors



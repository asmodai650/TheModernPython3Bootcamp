
## IMPORT MODULE
from random import randint

player_wins = 0
pc_wins = 0
total_wins = 3

## GAME INTRO
print("Rock!")
print("Paper!!")
print("Scissors!!!")
print("")
print("Best out of three. Get Ready!")
print("")

while player_wins < total_wins and pc_wins < total_wins:
    print(f"Player Score: {player_wins} , PC Score: {pc_wins} ")
    print("")

    ## ALLOW USER TO ENTER A VALUE
    player = input("Player, make your move! ").lower()

    ## CREATE RANDOM MOVE FOR COMPUTER PLAYER
    print("Computer, make your move! ")
    num = randint(0,99)
    if num >= 0 and num < 33:
        computer = "rock"
    elif num >= 33 and num < 66:
        computer = "paper"
    else:
        computer = "scissors"

    ## ACCOUNT FOR TIE AT THE BEGINNING
    if player == computer:
        print(f"It's a draw! Both of you played {player}.")

    ## DETERMINE WINNER
    if player == "rock":
        if computer == "scissors":
            print(f"Computer played {computer}.")
            print("You win!")
            player_wins += 1
        else:
            print(f"Computer played {computer}.")
            print("The computer wins!")
            pc_wins += 1
    elif player == "paper":
        if computer == "rock":
            print(f"Computer played {computer}.")
            print("You win!")
            player_wins += 1
        else:
            print(f"Computer played {computer}.")
            print("The computer wins!")
            pc_wins += 1
    elif player == "scissors":
        if computer == "paper":
            print(f"Computer played {computer}.")
            print("You win!")
            player_wins += 1
        else:
            print(f"Computer played {computer}.")
            print("The computer wins!")
            pc_wins += 1
    ## ACCOUNT FOR INVALID MOVE BY PLAYER
    else:
        print("You must be playing a different game!")
        print("You didn't play rock or paper or scissors.")

if player_wins > pc_wins:
    print("You Won!")
elif player_wins == pc_wins:
    print("It's a tie!")
else:
    print("PC Wins!")
print("")
print("GAME OVER")
print("")
print("Final Scores!")
print(f"Player: {player_wins} , PC: {pc_wins} ")
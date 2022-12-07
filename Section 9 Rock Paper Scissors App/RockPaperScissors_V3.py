
## IMPORT MODULE
from random import randint

## GAME INTRO
print("Rock!")
print("Paper!")
print("Scissors!")

## ALLOW USER TO ENTER A VALUE
player = input("Player, make your move!").lower()

## CREATE RANDOM MOVE FOR COMPUTER PLAYER
print("Computer, make your move!")
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
    else: # computer == "paper":
        print(f"Computer played {computer}.")
        print("The computer wins!")
elif player == "paper":
    if computer == "rock":
        print(f"Computer played {computer}.")
        print("You win!")
    else: # computer == "scissors":
        print(f"Computer played {computer}.")
        print("The computer wins!")
elif player == "scissors":
    if computer == "paper":
        print(f"Computer played {computer}.")
        print("You win!")
    else: # computer == "rock":
        print(f"Computer played {computer}.")
        print("The computer wins!")
## ACCOUNT FOR INVALID MOVE BY PLAYER
else:
    print("You must be playing a different game!")
    print("You didn't play rock or paper or scissors.")
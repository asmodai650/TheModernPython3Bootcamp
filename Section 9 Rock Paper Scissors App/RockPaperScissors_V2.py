#placeholder

print("Rock!")
print("Paper!")
print("Scissors!")

player1 = input("Player 1, make your move!").lower()
print("****NO PEAKING****\n" * 100)
player2 = input("Player 2, make your move!").lower()


if player1 == player2:
    print(f"It's a draw! You both played {player1}")

if player1 == "rock":
    if player2 == "scissors":
        print("Player 1 wins!")
    elif player2 == "paper":
        print("Player 2 wins!")
elif player1 == "paper":
    if player2 == "rock":
        print("Player 1 wins!")
    elif player2 == "scissors":
        print("Player 2 wins!")
elif player1 == "scissors":
    if player2 == "paper":
        print("Player 1 wins!")
    elif player2 == "rock":
        print("Player 2 wins!")
else:
    print("You must be playing a different game!")
    print("Someone didn't play rock or paper or scissors.")
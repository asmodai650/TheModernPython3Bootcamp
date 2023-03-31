import random

random_number = random.randint(1,10)
guess = None


while guess != random_number:
    guess = input("Pick a number between 1 and 10: ")
    guess = int(guess)
    if guess < random_number:
        print("too low")
    elif guess > random_number:
        print("too high")
    else:
        print(f"you guessed it. the number was {random_number}")

print("")
print(random_number)

random_number = random.randint(1,10)
guess = None


# version2
##while True:
##    guess = input("Pick a number between 1 and 10: ")
##    guess = int(guess)
##    if guess < random_number:
##        print("too low")
##    elif guess > random_number:
##        print("too high")
##    else:
##        print(f"you guessed it. the number was {random_number}")
##        play_again = input("want to play again? (y/n)")
##        if play_again == "y":
##            random_number = random.randint(1,10)
##            guess = None
##        else:
##            print("ok")
##            break

for num in range(1,21):
    if num == 4 or num == 13:
        print(f"{num} is UNLUCKY")
    elif num % 2 == 0:
        print(f"{num} is Even")
    else:
        print(f"{num} is Odd")

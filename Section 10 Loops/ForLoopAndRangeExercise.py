# Add up all odd numbers between 10 and 20
# Store the result in x:
x = 0

# YOUR CODE GOES HERE:
for n in range(10, 21):
    if n % 2 != 0:
        x += n
        print(f"{x}")
print(f"Total of all odd numbers between 10 and 20 is {x}.")
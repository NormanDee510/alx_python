import random

number = random.randint(-10, 10)  # Generate a random signed number between -10 and 10

print(f"{number} is", end=" ")

if number > 0:
    print("positive")
elif number == 0:
    print("zero")
else:
    print("negative")
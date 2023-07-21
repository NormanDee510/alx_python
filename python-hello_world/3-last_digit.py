import random

number = random.randint(-10000, 10000)  # Generate a random signed number between -10000 and 10000

last_digit = abs(number) % 10
is_greater_than_5 = last_digit > 5

print(f"Last digit of {number} is {last_digit} and is", end=" ")

if last_digit == 0:
    print("0")
elif is_greater_than_5:
    print("greater than 5")
else:
    print("less than 6 and not 0")
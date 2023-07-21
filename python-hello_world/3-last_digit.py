#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
# Print the random number
#Sprint("The number:", number)

# Check if the number is positive, zero, or negative and print the result
if number > 0:
    print("is positive")
elif number == 0:
    print("is zero")
else:
    print("is negative")
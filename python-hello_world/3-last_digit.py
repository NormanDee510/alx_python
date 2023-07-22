#!/usr/bin/python3
import random

number = random.randint(-10000, 10000)

last_digit = abs(number) % 10
sign = "less than 6 and not 0"

if last_digit > 5:
    sign = "greater than 5"
elif last_digit == 0:
    sign = "0"

print("Last digit of", number, "is", last_digit, "and is", sign)
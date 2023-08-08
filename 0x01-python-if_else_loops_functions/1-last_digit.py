#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)

# Extract the last digit of the number
lst = abs(number) % 10

if lst > 5:
    print(f'Last digit of {number} is {lst} and is greater than 5')
elif last_digit == 0:
    print(f'Last digit of {number} is {lst} and is 0')
else:
    print(f'Last digit of {number} is -{lst} and is less than 6 and not 0')

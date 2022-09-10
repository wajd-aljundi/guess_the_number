import math
import random

lower_bound = int(input("input the lower bound "))
upper_bound = int(input("input the upper bound "))

chances = round(math.log(upper_bound-lower_bound+1, 2))
x = random.randint(lower_bound, upper_bound)
print(f"you have {chances} tries to guess the number ")

tries = 0

while tries < chances:
    tries += 1
    guess = int(input("guess the number "))

    if guess == x:
        print(f"congrats! u did it in {tries}")
        break

    elif guess > x:
        print("you guessed too high")
        print(f"you have {chances-tries} tries left")

    elif guess < x:
        print("you guessed too low")
        print(f"you have {chances-tries} tries left")

if tries > chances:
    print("you have no chances left! ")
    print(f"the number is {x}")
    print("better luck next time! ")

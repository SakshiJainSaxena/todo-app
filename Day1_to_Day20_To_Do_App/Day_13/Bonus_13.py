""" Create a program where user is asked to enter feet and inches and the program converts it to meters.
Then check if the result is >1 or not to allow a child to use the ride or can not use the ride."""


def parse(feetinches):
    parts = feetinches.split(" ")
    feet = float(parts[0])
    inches = float(parts[1])
    return feet, inches


def convert(feet, inches):
    meters = feet * 0.3048 + inches * 0.0254
    return meters


"""
def convert(feet_inches):
    parts = feet_inches.split(" ")
    feet = float(parts[0])
    inches = float(parts[1])

    meters = feet * 0.3048 + inches * 0.0254
"""
# Decoupling is dividing a function in parts to make it more useful.
# In this case we divided the convert function into first parse to get feet and inches
# and then used the same to convert into meters.
# This helps use feet, inches and meters all the items while writing the actual extended code.


feet_inches = input("Enter feet and inches: ")

ft, inch = parse(feet_inches)

result = convert(ft, inch)

print(f"{ft} feet and {inch} inches are equal to {result} meters.")

if result > 1:
    print("The kid can use the ride")
else:
    print("The kid is too short for the ride")


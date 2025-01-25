""" Today we will optimize the code by saving the functions in another file
and importing them to perform some actions in this code.
"""
from Day1_to_Day20_To_Do_App.Day_14.Bonus_functions_14 import parse, convert
# This line for import was automatically added by python when we refactored the functions and moved them.

"""
def parse(feetinches):
    parts = feetinches.split(" ")
    feet = float(parts[0])
    inches = float(parts[1])
    return feet, inches


def convert(feet, inches):
    meters = feet * 0.3048 + inches * 0.0254
    return meters
"""

feet_inches = input("Enter feet and inches: ")

ft, inch = parse(feet_inches)

result = convert(ft, inch)

print(f"{ft} feet and {inch} inches are equal to {result} meters.")

if result > 1:
    print("The kid can use the ride")
else:
    print("The kid is too short for the ride")


""" Create a program where user is asked to enter feet and inches and the program converts it to meters.
Then check if the result is >1 or not to allow a child to use the ride or can not use the ride."""


def convert(feet_inches):
    parts = feet_inches.split(" ")
    feet = float(parts[0])
    inches = float(parts[1])

    meters = feet * 0.3048 + inches * 0.0254
    # return f"{feet} feet and {inches} inches are equal to {meters} meters."
    # Here we did not return this string cz string can not be used in the code further.
    # Value returned should be precise instead of complex.
    # This is called decoupling.
    return meters


feet_inches = input("Enter feet and inches: ")

result = convert(feet_inches)

if result > 1:
    print("The kid can use the ride")
else:
    print("The kid is too short for the ride")


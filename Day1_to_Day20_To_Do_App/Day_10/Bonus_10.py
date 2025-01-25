"""
Create a program that asks width and length of a rectangle from the user and returns the area of the rectangle.
1. Cater to value error if user enters the number in alphabet form instead of numerical.
2. Make sure the values entered by the user are of a rectangle only. If it is a square, tell the user it is a
square and so numbers are invalid.
"""








try:
    width = float(input("Please enter the width of the rectangle: "))

    length = float(input("Please enter the length of the rectangle: "))

    if width == length:
        exit("Oops! It looks like a square.")

    area = width * length
    print(f"Area of the rectangle is {area}.")

except ValueError:
    print("Please enter a number!")

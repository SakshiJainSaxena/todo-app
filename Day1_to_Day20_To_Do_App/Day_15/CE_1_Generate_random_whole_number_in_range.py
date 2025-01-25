"""Create a program that generates a random whole number.
First ask the user to enter a whole number. Then, once the user enters a number,
the program asks the user again to enter another number.
Then, the program returns a random number that falls between the two whole numbers."""

import random

lower_bound = int(input("Enter the lower bound: "))
upper_bound = int(input("Enter the upper bound: "))

number = random.randint(lower_bound, upper_bound)
print(number)

# number = random.randrange(lower_bound, upper_bound)
# print(number)

"""Both the methods can be used in this program but randint is more suitable
 as we do not need to provide any step as argument.
The difference between the two is that with randrange we can provide a step as well in the arguments."""

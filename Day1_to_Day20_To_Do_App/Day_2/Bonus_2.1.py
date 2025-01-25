"""Take password as user input.
Check if the password entered is correct.
Ask to enter password again if incorrect.
Say 'Correct password!' if the password entered is correct"""

password = input("Enter password: ")

while password != "pass123":
    print("Please enter correct password!")
    password = input("Enter password: ")

print("Correct Password!")


"""
Write a code where you ask the user to enter a new password
and return if the password is weak or strong checking the following conditions:
1. Length >= 8
2. It contains at least 1 digit
3. It contains at least 1 uppercase letter.

write the code using result as list and return strong password only if
all conditions are true.
"""

password = input("Enter new password: ")

result = []

if len(password) >= 8:
    result.append(True)
else:
    result.append(False)

digit = False
for i in password:
    if i.isdigit():
        digit = True
result.append(digit)

uppercase = False
for u in password:
    if u.isupper():
        uppercase = True
result.append(uppercase)

print(result)

if all(result):
    print("Strong Password")
else:
    print("Weak Password")


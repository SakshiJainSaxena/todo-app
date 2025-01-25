"""
Write a code where you ask the user to enter a new password
and return if the password is weak or strong checking the following conditions:
1. Length >= 8
2. It contains at least 1 digit
3. It contains at least 1 uppercase letter.

write the code using result as dictionary and return strong password only if
all conditions are true.
"""

password = input("Enter new password: ")

result = {}

if len(password) >= 8:
    result["length"] = True
else:
    result["length"] = False

digit = False
for i in password:
    if i.isdigit():
        digit = True
result["digit"] = digit

uppercase = False
for u in password:
    if u.isupper():
        uppercase = True
result["uppercase"] = uppercase

print(result)

if all(result.values()):
    print("Strong Password")
else:
    print("Weak Password")


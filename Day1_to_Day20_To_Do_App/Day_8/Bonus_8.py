"""
Create a directory called 'Journal'
Write a code jo 3 types k inputs leta hai user se and then date ko as text file create karta hai in journal directory.
Usme Mood and Thoughts ko write karke save karta hai as text file.
"""

date = input("Enter the date: ")
mood = input("How do you rate your mood today from 1 to 10?: ")
thoughts = input("let your thoughts flow: \n")

with open(f"Bonus_8_Journal\\{date}.txt", 'w') as file:
    file.write(f"Your mood scale for today is {mood}" + 2 * "\n")
    file.write(thoughts)

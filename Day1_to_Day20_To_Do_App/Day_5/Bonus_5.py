""" Print the items of the list starting with number 1 and dot in start but in ascending order
and first letter capitalised for each item"""

names = ["sen", "benji", "mona", "tom", "jerry"]
names.sort()

for index, name in enumerate(names):
    print(f"{index + 1}. {name.capitalize()}")



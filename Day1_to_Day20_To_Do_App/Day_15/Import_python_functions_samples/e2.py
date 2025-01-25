import csv

with open('weather.csv', 'r') as file:
    data = list(csv.reader(file))

city = input("Please enter the city: ")

for row in data:
    if row[0] == city:
        print(row[1])

"""csv helps access csv files and apply various codes to the data present in the csv file.
csv files mostly have data 
that can be represented in form of lists."""
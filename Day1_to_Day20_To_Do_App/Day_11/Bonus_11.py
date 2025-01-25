""" data vali file me jo numbers hain unki avg nikalne k liye function create karna hai so that
data me se numbers fetch karke uski avg nikal kr de code"""


def get_average():
    with open('Bonus_11_files/data', 'r') as file:
        data = file.readlines()

    values = data[1:]
    values = [float(i) for i in values]

    average_local = sum(values) / len(values)
    return average_local


average = get_average()
print(average)

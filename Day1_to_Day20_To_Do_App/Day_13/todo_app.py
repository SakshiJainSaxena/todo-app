def get_todos(filepath=r'C:\Users\Parv Jain\PycharmProjects\pythonProject2024\Day1_to_Day20_To_Do_App\Day_6\todos'):
    """ Opens the textfile in read mode and returns the list of to-do items. """
    with open(filepath, 'r') as file_local:
        todos_local = file_local.readlines()
        return todos_local
# filepath ko we have assigned default file name so that we do not have to write it again and again in the code.
# However, we can still assign a new filename if we want to use the same defined function elsewhere.
# Basically agar hum filename define ni karenge to by default vo iss file ko uthaega
# but define karenge to defined file name uthaega.


def write_todos(todos_arg, filepath=r'C:\Users\Parv Jain\PycharmProjects\pythonProject2024\Day1_to_Day20_To_Do_App'
                                    r'\Day_6\todos'):
    """ Writes the lst of to-do items in the textfile. """
    with open(filepath, 'w') as file_local:
        file_local.writelines(todos_arg)
# Non default argument pehle likhte hain and default vala badme.


""" Triple quotes are used for documenting the code so that you can read them to know what the code does.
These are suitable for multiline string as well and can be used as string if assigned to a variable.
Can also be used as comments when there are multiline comments like this one. """


while True:
    user_action = input("Type add, show, edit, complete or exit: ")
    user_action = user_action.strip()

    if user_action.startswith("add"):
        todo = user_action[4:]

        todos = get_todos()

        todos.append(todo)

        write_todos(todos)

    elif user_action.startswith("show"):

        todos = get_todos()

        for index, item in enumerate(todos):
            item = item.strip('\n')
            row = f"{index + 1}. {item.capitalize()}"
            print(row)

    elif user_action.startswith("edit"):
        try:
            number = int(user_action[5:])
            number = number - 1

            todos = get_todos()

            new_todo = input("Enter new todo: ")
            todos[number] = new_todo + '\n'

            write_todos(todos)

        except ValueError:
            print("Please enter a valid command!")
            continue

    elif user_action.startswith("complete"):
        try:
            number = int(user_action[9:])

            todos = get_todos()

            index = number - 1
            todo_to_remove = todos[index].strip('\n')
            todos.pop(index)

            write_todos(todos)

            message = f"Todo number '{number}' was '{todo_to_remove}' " \
                      f"and has been removed from the todo list successfully."
            print(message)

        except IndexError:
            print("Please enter a valid number.")
            continue

    elif user_action.startswith("exit"):
        break

    else:
        print("Please enter a valid command")

print("Bye!")

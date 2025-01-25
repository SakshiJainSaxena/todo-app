def get_todos(filepath):
    with open(filepath, 'r') as file_local:
        todos_local = file_local.readlines()
        return todos_local
# Filepath function me likhne ki jagah if we write an argument like filepath in this case,
# it will help us use the defined function dynamically.
# Filepath can be defined while calling the function by writing it in the parenthesis while calling the function.


def write_todos(filepath, todos_arg):
    with open(filepath, 'w') as file_local:
        file_local.writelines(todos_arg)
# Todos ko likhne k liye we have defined the writing function.
# It has 2 parameters filepath and todos_arg
# todos_arg is basically what is to be written vali value assign hogi is argument ko for writing in the textfile.


while True:
    user_action = input("Type add, show, edit, complete or exit: ")
    user_action = user_action.strip()

    if user_action.startswith("add"):
        todo = user_action[4:]

        todos = get_todos(r'/Day1_to_Day20_To_Do_App/todos')
        # Here we are calling the defined function for reading the text file
        # by providing the filepath of the required text file as argument.

        todos.append(todo)

        """with open(r'C:\Users\Parv Jain\PycharmProjects\pythonProject2024\Day1_to_Day20_To_Do_App\Day_6\todos', 'w')\
                as file:
            todos = file.writelines(todos)"""

        write_todos(r'/Day1_to_Day20_To_Do_App/todos', todos)

        # Here we are calling the defined function to write in the text file
        # Filepath and what to write (todos) are provided as the arguments or vales for the respective perimeters.

    elif user_action.startswith("show"):

        todos = get_todos(r'/Day1_to_Day20_To_Do_App/todos')

        for index, item in enumerate(todos):
            item = item.strip('\n')
            row = f"{index + 1}. {item.capitalize()}"
            print(row)

    elif user_action.startswith("edit"):
        try:
            number = int(user_action[5:])
            number = number - 1

            todos = get_todos(r'/Day1_to_Day20_To_Do_App/todos')

            new_todo = input("Enter new todo: ")
            todos[number] = new_todo + '\n'

            write_todos(r'/Day1_to_Day20_To_Do_App/todos', todos)

        except ValueError:
            print("Please enter a valid command!")
            continue

    elif user_action.startswith("complete"):
        try:
            number = int(user_action[9:])

            todos = get_todos(r'/Day1_to_Day20_To_Do_App/todos')

            index = number - 1
            todo_to_remove = todos[index].strip('\n')
            todos.pop(index)

            write_todos(r'/Day1_to_Day20_To_Do_App/todos', todos)

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

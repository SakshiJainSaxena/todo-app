def get_todos():
    with open(r'/Day1_to_Day20_To_Do_App/todos', 'r') \
            as file_local:
        todos_local = file_local.readlines()
        return todos_local
# This function is created cz ye same code 4 times repeat ho rha hai and code ko more efficient banane k liye
# we can just call the function instead of writing the same code many times.


while True:
    user_action = input("Type add, show, edit, complete or exit: ")
    user_action = user_action.strip()

    if user_action.startswith("add"):
        todo = user_action[4:]

        # with open(r'C:\Users\Parv Jain\PycharmProjects\pythonProject2024\Day1_to_Day20_To_Do_App\Day_6\todos', 'r')\
        #         as file:
        #     todos = file.readlines()

        todos = get_todos()

        todos.append(todo)

        with open(r'/Day1_to_Day20_To_Do_App/todos', 'w')\
                as file:
            todos = file.writelines(todos)

    elif user_action.startswith("show"):

        todos = get_todos()

        for index, item in enumerate(todos):
            item = item.strip('\n')
            row = f"{index + 1}. {item.capitalize()}"
            print(row)

    elif user_action.startswith("edit"):
        # try except block is added to attend to the error that might occur if the user enters an invalid command.
        try:
            number = int(user_action[5:])
            number = number - 1

            todos = get_todos()

            new_todo = input("Enter new todo: ")
            todos[number] = new_todo + '\n'

            with open(r'/Day1_to_Day20_To_Do_App/todos', 'w')\
                    as file:
                todos = file.writelines(todos)

        except ValueError:
            print("Please enter a valid command!")
            continue

    elif user_action.startswith("complete"):
        # try except block is added to attend to the error that might occur if the user enters an invalid command.
        try:
            number = int(user_action[9:])

            todos = get_todos()

            index = number - 1
            todo_to_remove = todos[index].strip('\n')
            todos.pop(index)

            with open(r'/Day1_to_Day20_To_Do_App/todos', 'w')\
                    as file:
                todos = file.writelines(todos)

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

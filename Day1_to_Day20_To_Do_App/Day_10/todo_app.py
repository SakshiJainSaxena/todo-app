while True:
    user_action = input("Type add, show, edit, complete or exit: ")
    user_action = user_action.strip()

    # if "add" in user_action: (same was done for all other user_actions.
    if user_action.startswith("add"):
        todo = user_action[4:]

        with open(r'/Day1_to_Day20_To_Do_App/todos', 'r')\
                as file:
            todos = file.readlines()

        todos.append(todo)

        with open(r'/Day1_to_Day20_To_Do_App/todos', 'w')\
                as file:
            todos = file.writelines(todos)

    elif user_action.startswith("show"):

        with open(r'/Day1_to_Day20_To_Do_App/todos', 'r')\
                as file:
            todos = file.readlines()

        for index, item in enumerate(todos):
            item = item.strip('\n')
            row = f"{index + 1}. {item.capitalize()}"
            print(row)

    elif user_action.startswith("edit"):
        # try except block is added to attend to the error that might occur if the user enters an invalid command.
        try:
            number = int(user_action[5:])
            number = number - 1

            with open(r'/Day1_to_Day20_To_Do_App/todos', 'r')\
                    as file:
                todos = file.readlines()

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

            with open(r'/Day1_to_Day20_To_Do_App/todos',
                      'r') as file:
                todos = file.readlines()

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

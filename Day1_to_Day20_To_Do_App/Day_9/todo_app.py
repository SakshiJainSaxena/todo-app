while True:
    user_action = input("Type add, show, edit, complete or exit: ")
    user_action = user_action.strip()

    if "add" in user_action:
        todo = user_action[4:]

        # file = open(r'C:\Users\Parv Jain\PycharmProjects\pythonProject2024\Day1_to_Day20_To_Do_App\Day_6\todos
        # ', 'r')
        # todos = file.readlines() file.close()

        with open(r'/Day1_to_Day20_To_Do_App/todos', 'r')\
                as file:
            todos = file.readlines()

        todos.append(todo)

        # file = open(r'C:\Users\Parv Jain\PycharmProjects\pythonProject2024\Day1_to_Day20_To_Do_App\Day_6\todos',
        # 'w')
        # todos = file.writelines(todos)
        # file.close()

        with open(r'/Day1_to_Day20_To_Do_App/todos', 'w')\
                as file:
            todos = file.writelines(todos)

    elif "show" in user_action:
        # file = open(r'C:\Users\Parv Jain\PycharmProjects\pythonProject2024\Day1_to_Day20_To_Do_App\Day_6\todos',
        # 'r')
        # todos = file.readlines()
        # file.close()

        with open(r'/Day1_to_Day20_To_Do_App/todos', 'r')\
                as file:
            todos = file.readlines()

        # new_todos = []
        #    for item in todos:
        #        new_item = item.strip('\n')
        #        new_todos.append(new_item)

        # new_todos = [item.strip('\n') for item in todos]

        for index, item in enumerate(todos):
            item = item.strip('\n')
            row = f"{index + 1}. {item.capitalize()}"
            print(row)

    elif "edit" in user_action:
        number = int(user_action[5:])
        number = number - 1

        with open(r'/Day1_to_Day20_To_Do_App/todos', 'r')\
                as file:
            todos = file.readlines()

        new_todo = input("Enter new todo: ")
        todos[number] = new_todo + '\n'
        # \n add kia hai yahan taki new todo ke sath bhi extra line add hojae.

        with open(r'/Day1_to_Day20_To_Do_App/todos', 'w')\
                as file:
            todos = file.writelines(todos)

    elif "complete" in user_action:
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

    elif "exit" in user_action:
        break

    else:
        print("Please enter a valid command")

print("Bye!")

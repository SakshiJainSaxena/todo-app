while True:
    user_action = input("Type add, show, edit, complete or exit: ")
    user_action = user_action.strip()

    match user_action:
        case "add":
            todo = input("Enter a todo: ") + "\n"

            file = open(r"/Day1_to_Day20_To_Do_App/todos", 'r')
            todos = file.readlines()
            file.close()

            todos.append(todo)

            file = open(r'/Day1_to_Day20_To_Do_App/todos', 'w')
            todos = file.writelines(todos)
            file.close()

        case "show":
            file = open(r'/Day1_to_Day20_To_Do_App/todos', 'r')
            todos = file.readlines()
            file.close()

            #""" new_todos = []
            #    for item in todos:
            #        new_item = item.strip('\n')
            #        new_todos.append(new_item) """

            #""" new_todos = [item.strip('\n') for item in todos] """

            for index, item in enumerate(todos):
                item = item.strip('\n')
                row = f"{index + 1}. {item.capitalize()}"
                print(row)

        case "edit":
            number = int(input("Enter the number of todo to edit: "))
            number = number - 1
            new_todo = input("Enter new todo: ")
            todos[number] = new_todo

        case "complete":
            number = int(input("Enter the number of todo to complete: "))
            todos.pop(number - 1)

        case "exit":
            break

print("Bye!")

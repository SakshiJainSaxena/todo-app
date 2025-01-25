from Day1_to_Day20_To_Do_App import functions
""" We will use this one instead of 'import functions' cz else daily todo app ke sath 
functions ko bhi copy karna padega in every new directory. 
In code we write 'functions.get_todos()' which helps the code know ki get_todos
ko kahan se fetch karna hai. """

# from functions import get_todos, write_todos
""" This is used when functions are in same directory and there are only few functions, 
so we can write the names of those functions."""

# import functions
""" This is used when functions is in same directory but has too many functions making it difficult to mention all.
So instead of writing all the names in code we write 'functions.get_todos()' which helps the code know ki get_todos
ko kahan se fetch karna hai. """


while True:
    user_action = input("Type add, show, edit, complete or exit: ")
    user_action = user_action.strip()

    if user_action.startswith("add"):
        todo = user_action[4:]

        # todos = get_todos()
        todos = functions.get_todos()

        todos.append(todo)

        # write_todos(todos)
        functions.write_todos(todos)

    elif user_action.startswith("show"):

        todos = functions.get_todos()

        for index, item in enumerate(todos):
            item = item.strip('\n')
            row = f"{index + 1}. {item.capitalize()}"
            print(row)

    elif user_action.startswith("edit"):
        try:
            number = int(user_action[5:])
            number = number - 1

            todos = functions.get_todos()

            new_todo = input("Enter new todo: ")
            todos[number] = new_todo + '\n'

            functions.write_todos(todos)

        except ValueError:
            print("Please enter a valid command!")
            continue

    elif user_action.startswith("complete"):
        try:
            number = int(user_action[9:])

            todos = functions.get_todos()

            index = number - 1
            todo_to_remove = todos[index].strip('\n')
            todos.pop(index)

            functions.write_todos(todos)

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

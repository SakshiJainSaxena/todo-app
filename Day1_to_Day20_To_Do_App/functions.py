FILEPATH = r'C:\Users\Parv Jain\PycharmProjects\pythonProject2024\Day1_to_Day20_To_Do_App\Day_6\todos'


def get_todos(filepath=FILEPATH):
    """ Opens the textfile in read mode and returns the list of to-do items. """
    with open(filepath, 'r') as file_local:
        todos_local = file_local.readlines()
        return todos_local


def write_todos(todos_arg, filepath=FILEPATH):
    """ Writes the lst of to-do items in the textfile. """
    with open(filepath, 'w') as file_local:
        file_local.writelines(todos_arg)


if __name__ == "__main__":
    print("Hello, it is the functions file.")

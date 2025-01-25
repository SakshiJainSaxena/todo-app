import glob

myfiles = glob.glob(r"/Day1_to_Day20_To_Do_App/Day_15/Import_python_functions_samples/files\*")

for filepath in myfiles:
    with open(filepath, 'r') as file:
        print(file.read().upper())

""" glob helps open or access all the text files saved in one directory at the same time. """

user_input = input("Add a new member: ")

file = open("C:\\Users\\Parv Jain\\PycharmProjects\\pythonProject2024\\Day1_to_Day20_To_Do_App\\Day_6\\members", 'r')
text = file.readlines()
file.close()

text.append(user_input + "\n")

file = open("C:\\Users\\Parv Jain\\PycharmProjects\\pythonProject2024\\Day1_to_Day20_To_Do_App\\Day_6\\members", 'w')
file.writelines(text)
file.close()


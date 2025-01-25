contents = ["All carrots are to be sliced longitudinally.",
            "The carrots were reportedly sliced.",
            "The slicing process was well presented."]

filenames = ["doc", "report", "presentation"]

"""Contents vale strings ko filenames wale files me save karna hai 
such that doc open karo to contents vali pehli line show ho and so on"""

"""CODE"""

for content, filename in zip(contents, filenames):
    file = open(f"C:\\Users\\Parv Jain\\PycharmProjects\\pythonProject2024\\Day1_to_Day20_To_Do_App\\Day_6\\{filename}", 'w')
    file.write(content)
    file.close()


filenames = ["file1.txt", "file2.txt"]

for filename in filenames:
        file = open(filename, 'w')
        file.write("Hello")
        file.close()

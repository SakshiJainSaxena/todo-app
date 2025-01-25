"""
List vali items me se '.' ko '-' se replace karna hai and last me '.txt' add karna hai.
Ex-(1.doc) turns to (1-doc.txt)
"""

filenames = ["1.doc", "1.report", "1.presentation"]

filenames = [filename.replace('.', '-') + '.txt' for filename in filenames]

print(filenames)

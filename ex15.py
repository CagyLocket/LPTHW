# This line import a module of argument variable from sys library
from sys import argv

# This line specifies a script (file) and a file name
# script, filename = argv

# This line gives a variable txt which call a function to open the file
# txt = open(filename)

# This line prints out a message to a user and gives the file name
# print(f"Here's your file {filename}:")
# This line reads the file and print out its content
# print(txt.read(filename))

# This line shows a message to a user
print("Type the filename again:")

# This line asks a user for an input of the file name
file_again = input("> ")

# This line open the file given by a user
txt_again = open(file_again)

# This line reads the file and prints out its content to the user
print(txt_again.read())
txt_again.close()

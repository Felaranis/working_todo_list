from data_file.funclist import *


print("Welcome to To-DoList. Below is the list of options of your choice\n")

for key in options:
    print(key + ":" + options[key])
while True:
    choice = input("Please choose one of the following options below:\n")
    if choice == "n":
        break

cls()
from data_file.funclist import *
import os
import json

path = os.path.join(os.getcwd(), "data_file", "tasks.json")
print(path)

TODO_LIST = []

is_file = os.path.isfile(path)
if is_file == True:
    with open(path, "r") as file:
        try:
            our_file = json.load(file)
            TODO_LIST = our_file
        except json.JSONDecodeError:
            print("There is no information in this file")

    


# json.JSONDecodeError




# print("Welcome to To-DoList. Below is the list of options of your choice\n")



# for key in options:
#     print(key + ":" + options[key])
# while True:
#     choice = input("Please choose one of the following options below:\n")
#     if choice == "n":
#         break

# cls()
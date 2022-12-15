from data_file.funclist import *
from helpers.test_prog import TEST_DATA
from helpers.all_functions import task_search
import os
import json

TODO_LIST = []

path = os.path.join(os.getcwd(), "data_file", "tasks.json")
print(path)

def read_json(path):
    is_file = os.path.isfile(path)
    if is_file == True:
        with open(path, "r") as file:
            try:
                our_file = json.load(file)
                return our_file
            except json.JSONDecodeError:
                print("Something wrong with file")
                return []

def dump_json(path, add_list):
    with open(path, "w") as file:
        json.dump(add_list, file)

# dump_json(path, TEST_DATA)
TODO_LIST = read_json(path)
print(type(TODO_LIST))
task_search(TODO_LIST)


 

# json.JSONDecodeError




# print("Welcome to To-DoList. Below is the list of options of your choice\n")



# for key in options:
#     print(key + ":" + options[key])
# while True:
#     choice = input("Please choose one of the following options below:\n")
#     if choice == "n":
#         break

# cls()
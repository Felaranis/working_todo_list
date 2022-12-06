from test_prog import TEST_DATA
from all_functions import *


#  Переглянути всі заплановані справи (тільки назви) у порядку їхнього додавання
# def assigned_task_by_add(task_list):
#     """Printing the task by ID creation from 1 to .... Return the name of the task"""

#     sorted_tasks = sorted(task_list, key=lambda x: (x["id"]))
#     for task in sorted_tasks:
#         print(task["title"])

# assigned_task_by_add(TEST_DATA)

# Переглянути всі заплановані справи (тільки назви) у порядку спадання пріоритету
# def assigned_task_priority(task_list):
#     """Checking the task by priority level from High to low. Return the name of the task"""

#     sorted_tasks = sorted(task_list, key=lambda x: x["priority"], reverse=True)
#     for task in sorted_tasks:
#         print(task["title"])
# assigned_task_priority(TEST_DATA)

# Переглянути всі невиконані справи (тільки назви)
# def uncompleted_task(task_list):
#     """Checking if the task was uncompleted and return title of pending task"""

#     for task in task_list:
#         if task["done"] == False:
#             print(task["title"])

# uncompleted_task(TEST_DATA)

# Переглянути виконані справи (тільки назви)
def completed_task(task_list):
    """Checking if the task was completed and return the title of completed task"""
    
    for task in task_list:
        if task['done'] == True:
            print(task["title"])


completed_task(TEST_DATA)
from test_prog import TEST_DATA
from all_functions import print_task, task_search

# Знайти та помітити справу, як виконану

def task_completed(task_list):

    """This func would ask user to input task's name and return it as completed """
    task = task_search(task_list)
    task["done"] = True
    print_task(task)
        
task_completed(TEST_DATA)

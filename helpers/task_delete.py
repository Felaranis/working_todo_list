from test_prog import TEST_DATA
from all_functions import print_task, task_search

# Знайти та видалити справу
def task_delete(task_list):

    """The func delte chosen task"""
    if not task_list:
        return print("No task created")
    del_task = task_search(task_list)
    task_list.remove(del_task)
    print_task(del_task)

task_delete(TEST_DATA)
print(len(TEST_DATA))

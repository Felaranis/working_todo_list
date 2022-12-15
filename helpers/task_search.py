from helpers.test_prog import TEST_DATA
from helpers.all_functions import print_task, task_search
# Знайти запис за частиною назви та переглянути її деталі
        
def task_details(task_list):

    """The func would return the task that user is looking for"""

    print_task(task_search(task_list))
if __name__ == "__main__":
    task_details(TEST_DATA)
from test_prog import TEST_DATA

# Переглянути статистику (загальна кількість справ, кількість виконаних/невиконаних/прострочених справ)
def num_of_tasks(task_list):
    """ Return a sum of total amount of tasks user has in test data"""

    task_len = len(task_list)
    print(task_len)

num_of_tasks(TEST_DATA)

# невиконаних
def num_of_uncompleted(task_list):
    """ Return a sum of total uncompleted tasks in the test data"""

    number_of_tasks = 0
    for task in task_list:
        if task["done"] == False:
            number_of_tasks += 1
    print(number_of_tasks)

num_of_uncompleted(TEST_DATA)
# виконаних
def num_of_completed(task_list):
    """Return a sum of total completed tasks in the test data"""

    number_of_tasks = 0
    for task in task_list:
        if task["done"] == "Completed":
            number_of_tasks += 1
    print(number_of_tasks)


num_of_completed(TEST_DATA)

print(f"You have a total of {num_of_tasks()} tasks!\n{num_of_uncompleted()} need to be completed and {num_of_completed()} is done succesfully.")
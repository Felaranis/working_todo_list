from datetime import datetime, timedelta, date
from test_prog import TEST_DATA
# Переглянути прострочені справи (тільки назви)

def task_overdue(task_list):
    """This func prints the name of all overdue tasks"""
    if not task_list:
        return print("No task created")
    overdue = datetime.today()
    for task in task_list:
        if task["due_date"].date() <= overdue.date() and not task["done"]:
            print(task["title"])
task_overdue(TEST_DATA)
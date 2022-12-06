from datetime import datetime

all_tasks = []

def add_task():
    task = {}
    print("Input your new task")
    task["id"] = len(all_tasks) + 1
    user_title_input = input("In short, what would you like to do \n")
    task["title"] = user_title_input[0:50]
    task["description"] = input("Provide us with a detailed explanation of the task\n")
    if not task["description"]:
        task["description"] = user_title_input
    while True:
        try:
            task["priority"] = int(input("Please choose a priority from 1 to 10\n"))
        except ValueError:
            continue
        if task["priority"] >= 1 or task["priority"] <= 10:
            break

    choose_date = input("Please choose a completion due date in the following format: Year/Month/Day, Hours:Minutes\n")
    time_format = "%Y/%m/%d, %H:%M"
    try:
        task["due_date"] = datetime.strptime(choose_date, time_format)
    except ValueError:
        task["due_date"] = datetime.today()
    task["done"] = False
    all_tasks.append(task)


add_task()
print(all_tasks)
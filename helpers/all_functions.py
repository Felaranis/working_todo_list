def task_search(task_list):
    ask = input("Which task would you like to review?\n").lower()
    if not task_list:
        return print("No task created")
    for task in task_list:
        if ask in task["title"].lower():
            return task
        

def print_task(task_list):
    """This func would print key/values in a readeable format"""
    if not task_list:
        return print("No task created")
    for item in task_list:
        print(item.title().replace("_", " ") + " : " + str(task_list[item]))

def prior():
    while True:
        try:
            priority = int(input("Insert your new priority from 1 to 10\n"))
        except ValueError:
            continue
        if 1 <= priority <= 10:
            return priority
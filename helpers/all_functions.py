def task_search(task_list):
    ask = input("Which task would you like to review?\n").lower()
    for task in task_list:
        if ask in task["title"].lower():
            return task
    else:
        print("No task created")

        

def print_task(task):
    """This func would print key/values in a readeable format"""
    if task == None:
        return 
    for item in task:
        print(item.title().replace("_", " ") + " : " + str(task[item]))


def prior():
    while True:
        try:
            priority = int(input("Insert your new priority from 1 to 10\n"))
        except ValueError:
            continue
        if 1 <= priority <= 10:
            return priority

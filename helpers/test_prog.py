from datetime import date, datetime, timedelta

TEST_DATA = [
    {
        "id": 1,
        "title": "Shop",
        "description": "Grocery shopping",
        "priority": 3,
        "due_date": datetime(2022, 12, 7, 12, 0),
        "done": False
    },
    {
        "id": 2,
        "title": "Work",
        "description": "Go to work",
        "priority": 5,
        "due_date": datetime(2022, 11, 30, 12, 0),
        "done": False
    },
]




# def print_task(task):

#     """This func would print key/values in a readeable format"""
    
#     for item in task:
#         print(item.title().replace("_", " ") + " : " + str(task[item]))

# def task_search(task_list):
#     ask = input("Which task would you like to review?\n").lower()
#     for task in task_list:
#         if ask in task["title"].lower():
#             return task

# def task_priority(task_list):

#     task = task_search(task_list)
#     while True:
#         try:
#             priority = int(input("Insert your new priority from 1 to 10\n"))
#         except ValueError:
#             continue
#         if 1 <= priority <= 10:
#             break
#     task["priority"] = priority
        
#     print_task(task)

# task_priority(TEST_DATA)

        

# task_completed(TEST_DATA)




# def print_task(task):
#     """This func would print key/values in a readeable format"""
#     for item in task:
#         print(item.title().replace("_", " ") + " : " + str(task[item]))








# for task in TEST_DATA:
#     if user_input in task.get('title', 'There is not such task').lower():
#         my_task.update(task)
# result = '\n'.join(f'{key}: {value}' for key, value in my_task.items())
# print(result)







# Переглянути прострочені справи (тільки назви)

# def tasks_due_week(task_list):
#     task_in_week = datetime.today() + timedelta(days=7)
#     for task in task_list:
#         if task["due_date"].date() <= task_in_week.date():
#             print(task["title"])

# tasks_due_week(TEST_DATA)

# def task_overdue(task_list):
#     overdue = datetime.today()
#     for task in task_list:
#         if task["due_date"].date() <= overdue.date():
#             print(task["title"])
# task_overdue(TEST_DATA)








# with open("test_d.txt", "w") as file:
#     json.dump(TEST_DATA, file)

# with open("test_d.txt", "r") as file:
#     t_list = json.load(file)

# print(t_list )


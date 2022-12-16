from test_prog import TEST_DATA
from all_functions import print_task, task_search, prior


def task_priority(task_list):
    
    if not task_list:
        return print("No task created")
    task = task_search(task_list)
    
    task["priority"] = prior()
        
    print_task(task)

task_priority(TEST_DATA)



            
        
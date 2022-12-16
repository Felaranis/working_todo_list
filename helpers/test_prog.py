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



# with open("test_d.txt", "w") as file:
#     json.dump(TEST_DATA, file)

# with open("test_d.txt", "r") as file:
#     t_list = json.load(file)

# print(t_list )


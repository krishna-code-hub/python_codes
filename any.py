

# List of tasks with completion status
tasks = [
    {"name": "Do laundry", "completed": True},
    {"name": "Wash dishes", "completed": False},
    {"name": "Walk the dog", "completed": False},
    {"name": "Grocery shopping", "completed": True}
]

# Check if at least one task is completed
if any(task["completed"] for task in tasks):
    print("There are completed tasks.")
else:
    print("No completed tasks.")

# Output: There are completed tasks.


my_tuple = (False, False, True, False)
print(any(my_tuple))  # Output: True

my_set = {0, '', False, None}
print(any(my_set))  # Output: False


my_dict = {'a': False, 'b': False, 'c': True, 'd': False}

# Check if any of the values in the dictionary evaluate to True
print(any(my_dict.values()))  # Output: True

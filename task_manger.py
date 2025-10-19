tasks = list()
# Function to add a task
def add_task():
    task_name = input("Enter your task: ")
    task_description = input("Describe your task: ")
    tasks.append({"Task Name":task_name, "Descripetion":task_description})
    view_task()

def view_task():
    if tasks:
        n=1
        for i in tasks:
            print(f'Number: {n}. Task Name: "{i["Task Name"]}. Task Description {i["Descripetion"]}": ')
    else:
        print("No tasks yet")

def update_task():
    view_task()
    task_num = input("Your task number you want to edit")
    task_num = int(task_num) - 1
    if len(tasks) > task_num:
        new_task_name = input("Enter your task (Keep Empty if you Don't want to change): ")
        new_task_description = input("Describe your task(Keep Empty if you Don't want to change): ")
        if new_task_name == "" and new_task_description == "":
            tasks[task_num] = {"Task Name":new_task_name}
        if new_task_name:
            tasks[task_num] = {"Descripetion":new_task_description}
        tasks[task_num] = {"Task Name":new_task_name, "Descripetion":new_task_description}
    else:
        print("No tasks yet")

def delete_task():
    view_task()
    task_num = input("Your task number you want to Edit: ")
    task_num = int(task_num) - 1
    if len(tasks) > task_num:
        tasks.pop(task_num)
    else:
        print("No tasks yet")

while True:
    print("Welcome to CLI Task Manager")
    print("Type 1 if you want to Add a Task")
    print("Type 2 if you want to View your tasks")
    print("Type 3 if you want to Update your tasks")
    print("Type 4 if you want to delete your tasks")
    print("Type 5 if you want to Exit the CLI, Note: all your tasks will be deleted")
    choice = input("Type your number: ")
    if choice == '1':
        add_task()
    elif choice == '2':
        view_task()
    elif choice == '3':
        update_task()
    elif choice == '4':
        delete_task()
    elif choice == '5':
        print("Exiting...")
        break
    else:
        print("print a valid op number")
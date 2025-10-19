# List for all the lists
tasks = list()

# Function to add a task
def add_task():
    task_name = input("Enter your task: ")
    task_description = input("Describe your task: ")
    tasks.append({"Task Name":task_name, "Descripetion":task_description})
    view_task()

# Function to View tasks
def view_task():
    if tasks:
        for i in tasks:
            n=1
            print(f'Number: {n}. Task Name: "{i["Task Name"]}. Task Description {i["Descripetion"]}": ')
            n+=n
    else:
        print("No tasks yet")

# Function to Updae tasks
def update_task():
    view_task()
    if tasks:
        task_num = int(input("Your task number you want to edit: ")) - 1
        if 0 <= task_num < len(tasks):
            new_task_name = input("New title name: ")
            new_task_desc = input("New title descreption: ")
            if new_task_name:
                tasks[task_num]["Descripetion"] = new_task_name
            if new_task_name:
                tasks[task_num]["Task Name"] = new_task_desc
        else:
            pass

    else:
        print("No tasks yet")

# Function to Delete tasks
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
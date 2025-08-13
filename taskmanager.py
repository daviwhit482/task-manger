# functions

def addTask():
    task = ''
    while task != 'x':
        task = str(input("Enter task to add (enter 'x' to return to menu): "))
        if task != 'x':
            taskList.append(task)
    Main()

# delete task using pop so when an element above it is removed all elements shift up

def delTask():
    for index, element in enumerate(taskList, start=1):
        print(f"{index}. {element}")
    taskNum = ''
    while taskNum != 'x':
        taskNum = input("Select a task to delete (enter 'x' to return to menu): ")
        if taskNum != 'x':
            num = int(taskNum)
            taskList.pop(num - 1)
    Main()

# allows users to re-write whatever is in that numbered place

def editTask():
    for index, element in enumerate(taskList, start=1):
        print(f"{index}. {element}")
    taskNum = int(input("Select a task to edit: "))
    newTask = str(input("Enter the edited task: "))
    taskList[taskNum - 1] = newTask
    Main()

# view task using enumerate so each task is numbered before it

def viewTask():
    print("Current tasks: ")
    for index, element in enumerate(taskList, start=1):
        print(f"{index}. {element}")
    Main()

# saving to file using write so that it overrides whatever is currently in that file

def saveFile():
    file_name = str(input("Enter the name of the file you want to save to: "))
    with open(file_name, "w") as file:
        for task in taskList:
            file.write(task + "\n")
    Main()

# using try except so that if user enters an invalid file name, program doesn't break

def loadFile():
    file_name = str(input("Enter the name of the file you want to load from: "))
    try:
        with open(file_name, "r") as file:
            for line in file:
                taskList.append(line.strip())
            print("Tasks have been loaded successfully.")
    except FileNotFoundError:
        print("That file doesn't exist.")
    Main()

# main

taskList = []

def Main():
    while True:
        print("Welcome to your Task Manager!")
        print("------------------------------")
        print("1. Add a task")
        print("2. Delete a task")
        print("3. Edit a task")
        print("4. View all tasks")
        print("5. Save tasks to file")
        print("6. Load tasks from file")
        print("7. Exit")

        try:
            choice = int(input("Enter your choice (1-7): "))
        except ValueError:
            print("Please enter a number.")
            continue

        if choice == 1:
            addTask()
        elif choice == 2:
            delTask()
        elif choice == 3:
            editTask()
        elif choice == 4:
            viewTask()
        elif choice == 5:
            saveFile()
        elif choice == 6:
            loadFile()
        elif choice == 7:
            print("Goodbye!")
            quit()
        else:
            False
            print("Invalid choice, try again.")

Main()
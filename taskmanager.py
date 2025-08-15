class TaskManager():
    def __init__(self):
        self.tasks = []

    # add task using user input, if user enters 'x', exits method

    def addTask(self):
        task = ''
        while task != 'x':
            task = str(input("Enter task to add (enter 'x' to return to menu): "))
            if task != 'x':
                self.tasks.append(task)
  
    # delete task using pop so when an element above it is removed all elements shift up

    def delTask(self):
        if not self.tasks:
            print('No tasks to delete.')
            return
        self.viewTask()
        taskNum = ''
        while taskNum != 'x':
            taskNum = input("Select a task to delete (enter 'x' to return to menu): ")
            if taskNum != 'x':
                try:
                    num = int(taskNum)
                    self.tasks.pop(num - 1)
                except (ValueError, IndexError):
                    print("Invalid task number.")
        
    # allows users to re-write whatever is in that numbered place

    def editTask(self):
        if not self.tasks:
            print('No tasks to edit.')
            return
        self.viewTask()
        try:
            taskNum = int(input("Select a task to edit: "))
            newTask = input("Enter the edited task: ")
            self.tasks[taskNum - 1] = newTask
        except (ValueError, IndexError):
            print("Invalid task number.")

    # view task using enumerate so each task is numbered before it

    def viewTask(self):
        if not self.tasks:
            print('No tasks to show.')
            return
        print("Current tasks: ")
        for index, element in enumerate(self.tasks, start=1):
            print(f"{index}. {element}")

    # saving to file using write so that it overrides whatever is currently in that file

    def saveFile(self):
        file_name = str(input("Enter the name of the file you want to save to: "))
        try:
            with open(file_name, "w") as file:
                for task in self.tasks:
                    file.write(task + "\n")
            print("tasks successfully saved to file!")
        except:
            print("Invalid file name.")

    # using try except so that if user enters an invalid file name, program doesn't break

    def loadFile(self):
        self.tasks.clear()
        file_name = str(input("Enter the name of the file you want to load from: "))
        try:
            with open(file_name, "r") as file:
                for line in file:
                    self.tasks.append(line.strip())
                print("Tasks have been loaded successfully.")
        except FileNotFoundError:
            print("That file doesn't exist.")

# main

def Main():

    manager = TaskManager()

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
            manager.addTask()
        elif choice == 2:
            manager.delTask()
        elif choice == 3:
            manager.editTask()
        elif choice == 4:
            manager.viewTask()
        elif choice == 5:
            manager.saveFile()
        elif choice == 6:
            manager.loadFile()
        elif choice == 7:
            print("Goodbye!")
            break
        else:
            False
            print("Invalid choice, try again.")

Main()

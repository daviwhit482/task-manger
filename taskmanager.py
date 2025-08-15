class TaskManager():
    def __init__(self):
        self.tasks = []

    # add task using user input, if user enters 'x', exits method

    def create_task(self):
        task = ''
        while task == '':
            task = str(input("Enter the task description: ")).strip()
        
        priority = ''
        while priority == '':
            priority = str(input("Enter the priority (High/Medium/Low): ")).strip()
        
        due = ''
        while due == '':
            due = str(input("Enter the due date (YYYY-MM-DD): ")).strip()

        status = ''
        while status == '':
            status = str(input("Enter the status (Done/Not Done): ")).strip()

        new_task = Task(task, priority, due, status)
        self.tasks.append(new_task)
        print('Task successfully added!')
  
    # delete task using pop so when an element above it is removed all elements shift up

    def delete_task(self):
        if not self.tasks:
            print("No tasks to delete.")
            return

        while True:
            self.view_task()
            task_num = input("Select a task to delete (enter 'x' to return to menu): ").strip()

            if task_num.lower() == 'x':
                break

            try:
                index = int(task_num) - 1
                if 0 <= index < len(self.tasks):
                    deleted_task = self.tasks.pop(index)
                    print(f"Task '{deleted_task.get_task()}' deleted successfully.")
                else:
                    print("Invalid task number.")
            except ValueError:
                print("Please enter a valid number or 'x' to exit.")
        
    # allows users to re-write whatever is in that indexed place

    def edit_task(self):
        if not self.tasks:
            print('No tasks to edit.')
            return

        self.view_task()
        try:
            task_index = int(input("Select a task to edit: ")) - 1
            if 0 <= task_index < len(self.tasks):
                task = self.tasks[task_index]

                print("Press Enter to keep the current value.")

                new_name = input(f"Task name ({task.task}): ")
                if new_name.strip():
                    task.set_task(new_name)

                new_priority = input(f"Priority ({task.priority}): ")
                if new_priority.strip():
                    task.set_priority(new_priority)

                new_due = input(f"Due date ({task.due}): ")
                if new_due.strip():
                    task.set_due(new_due)

                new_status = input(f"Status ({task.status}): ")
                if new_status.strip():
                    task.set_status(new_status)

                print("Task updated successfully.")

            else:
                print("Invalid task number.")
        except ValueError:
            print("Invalid input. Please enter a number.")


    # view task using enumerate so each task is numbered before it

    def view_task(self):
        if not self.tasks:
            print('No tasks to show.')
            return
        print("Current tasks: ")
        for index, element in enumerate(self.tasks, start=1):
            print(f"{index}. {element.get_task()} | Priority: {element.get_priority()} | Due: {element.get_due()} | Status: {element.get_status()}")

    # saving to file using write so that it overrides whatever is currently in that file

    def save_file(self):
        file_name = str(input("Enter the name of the file you want to save to: "))
        try:
            with open(file_name, "w") as file:
                for task in self.tasks:
                    file.write(f"{task.get_task()},{task.get_priority()},{task.get_due()},{task.get_status()}\n")
            print("Tasks successfully saved to file!")
        except:
            print("Invalid file name.")

    # using try except so that if user enters an invalid file name, program doesn't break

    def load_file(self):
        self.tasks.clear()
        file_name = str(input("Enter the name of the file you want to load from: "))
        try:
            with open(file_name, "r") as file:
                for line in file:
                    parts = line.strip().split(',')
                    if len(parts) == 4:
                        task, priority, due, status = parts
                        self.tasks.append(Task(task, priority, due, status))
                print("Tasks have been loaded successfully!")
        except FileNotFoundError:
            print("That file doesn't exist.")

class Task():

    # initialization
    def __init__(self, pTask, pPriority, pDue, pStatus):
        self.task = pTask
        self.priority = pPriority
        self.due = pDue
        self.status = pStatus
    
    # setter methods
    def set_task(self, task):
        self.task = task
    def set_priority(self, priority):
        self.priority = priority
    def set_due(self, due):
        self.due = due
    def set_status(self, status):
        self.status = status
    
    # getter methods
    def get_task(self):
        return self.task
    def get_priority(self):
        return self.priority
    def get_due(self):
        return self.due
    def get_status(self):
        return self.status

    
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
            manager.create_task()
        elif choice == 2:
            manager.delete_task()
        elif choice == 3:
            manager.edit_task()
        elif choice == 4:
            manager.view_task()
        elif choice == 5:
            manager.save_file()
        elif choice == 6:
            manager.load_file()
        elif choice == 7:
            print("Goodbye!")
            break
        else:
            False
            print("Invalid choice, try again.")

Main()

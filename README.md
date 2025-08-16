# Task Manager CLI

![Python](https://img.shields.io/badge/python-3.x-blue.svg)
![License](https://img.shields.io/badge/license-MIT-green.svg)

A simple command-line task management application in Python that allows you to **add, view, edit, delete, save, and load tasks**. Each task includes a description, priority, due date, and status.

## Features

- Add new tasks with a description, priority (High/Medium/Low), due date, and status (Done/Not Done).  
- Edit existing tasks, keeping current values if Enter is pressed.  
- Delete tasks by selecting the task number.  
- View all tasks with clear formatting showing task details.  
- Save tasks to a CSV-like file for persistent storage.  
- Load tasks from a previously saved file.  

## How to Run

1. Make sure you have **Python 3** installed.  
2. Clone or download the repository.  
3. Run the program from the terminal:
```
python main.py
```
4. Follow the on-screen menu to manage your tasks.

## File Format

Tasks are saved in a comma-separated format txt:
```
Task Description,Priority,Due Date,Status
```

## Planned Improvements

- Add sorting/filtering tasks by priority or due date.
- Add reminders or notifications.
- Create a web application version using Flask.

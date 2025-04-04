# Simple To-Do List App
tasks = []

def add_task():
    task = input("➕ Enter a new task: ")
    tasks.append(task)
    print(f"Task '{task}' added!")

def show_tasks():
    print("\n📋 Your Tasks:")
    for i, task in enumerate(tasks, 1):
        print(f"{i}. {task}")

while True:
    print("\n===== TO-DO LIST =====")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Exit")
    
    choice = input("Choose an option (1-3): ")
    
    if choice == "1":
        add_task()
    elif choice == "2":
        show_tasks()
    elif choice == "3":
        print("Goodbye! 👋")
        break
    else:
        print("Invalid choice. Try again.")
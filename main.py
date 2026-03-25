# Simple CLI-based Task Manager

tasks = []

def show_menu():
    print("\n--- Student Task Manager ---")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Mark Task as Complete")
    print("4. Delete Task")
    print("5. Exit")


def add_task():
    task = input("Enter task: ")
    tasks.append({"task": task, "done": False})
    print("Task added successfully!")


def view_tasks():
    if not tasks:
        print("No tasks available.")
        return

    print("\nYour Tasks:")
    for i, t in enumerate(tasks):
        status = "✔" if t["done"] else "✘"
        print(f"{i + 1}. {t['task']} [{status}]")


def mark_complete():
    view_tasks()
    try:
        num = int(input("Enter task number to mark complete: "))
        tasks[num - 1]["done"] = True
        print("Task marked as complete!")
    except:
        print("Invalid input.")


def delete_task():
    view_tasks()
    try:
        num = int(input("Enter task number to delete: "))
        tasks.pop(num - 1)
        print("Task deleted!")
    except:
        print("Invalid input.")


while True:
    show_menu()
    choice = input("Enter your choice: ")

    if choice == '1':
        add_task()
    elif choice == '2':
        view_tasks()
    elif choice == '3':
        mark_complete()
    elif choice == '4':
        delete_task()
    elif choice == '5':
        print("Goodbye!")
        break
    else:
        print("Invalid choice. Try again.")


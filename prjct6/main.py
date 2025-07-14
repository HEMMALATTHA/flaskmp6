import json
import os

TODO_FILE = 'todos.json'

def load_todos():
    if not os.path.exists(TODO_FILE):
        return []
    with open(TODO_FILE, 'r') as file:
        return json.load(file)

def save_todos(todos):
    with open(TODO_FILE, 'w') as file:
        json.dump(todos, file, indent=4)

def add_task(task):
    todos = load_todos()
    todos.append({"task": task, "done": False})
    save_todos(todos)
    print(f"Added: {task}")

def list_tasks():
    todos = load_todos()
    if not todos:
        print("No tasks yet.")
        return
    print("\nTo-Do List:")
    for i, todo in enumerate(todos, 1):
        status = "✅" if todo["done"] else "❌"
        print(f"{i}. [{status}] {todo['task']}")
    print()

def mark_done(index):
    todos = load_todos()
    if 0 <= index < len(todos):
        todos[index]["done"] = True
        save_todos(todos)
        print(f"Marked as done: {todos[index]['task']}")
    else:
        print("Invalid task number.")

def delete_task(index):
    todos = load_todos()
    if 0 <= index < len(todos):
        removed = todos.pop(index)
        save_todos(todos)
        print(f"Deleted: {removed['task']}")
    else:
        print("Invalid task number.")

def show_menu():
    print("""
=== TODO LIST APP ===
1. View Tasks
2. Add Task
3. Mark Task as Done
4. Delete Task
5. Exit
""")

if __name__ == '__main__':
    while True:
        show_menu()
        choice = input("Choose an option: ")

        if choice == '1':
            list_tasks()
        elif choice == '2':
            task = input("Enter the task: ")
            add_task(task)
        elif choice == '3':
            list_tasks()
            try:
                idx = int(input("Enter task number to mark as done: ")) - 1
                mark_done(idx)
            except ValueError:
                print("Invalid input.")
        elif choice == '4':
            list_tasks()
            try:
                idx = int(input("Enter task number to delete: ")) - 1
                delete_task(idx)
            except ValueError:
                print("Invalid input.")
        elif choice == '5':
            print("Exiting... Bye!")
            break
        else:
            print("Invalid option. Try again.")

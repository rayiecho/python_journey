def add_tasks(tasks, name):
    tasks.append({"name": name, "done": False})

def show_tasks(tasks):
    if len(tasks) == 0:
        print("No tasks yet!")
        return
    for i, task in enumerate(tasks):
        status = ">" if task["done"] else "x"
        print(f"{i + 1}. [{status}] {task['name']}")

def complete_tasks(tasks, number):
    if number < 1 or number > len(tasks):
        print("Invalid task number")
        return
    tasks[number - 1]["done"] = True
    print(f"Task {number} marked as done!")

def remove_tasks(tasks, number):
    if number < 1 or number > len(tasks):
        print("Invalid task number")
        return
    removed = tasks.pop(number - 1)
    print(f"Removed: {removed['name']}")

def main():
    tasks = []
    while True:
        print("\n--- TO-DO LIST ---")
        print("1. Add task")
        print("2. Show tasks")
        print("3. Complete task")
        print("4. Remove task")
        print("5. Quit")
        choice = input("\nChoose an option: ")
        if choice == "1":
            name = input("Task name: ")
            add_tasks(tasks, name)
        elif choice == "2":
            show_tasks(tasks)
        elif choice == "3":
            show_tasks(tasks)
            number = int(input("Task number to complete: "))
            complete_tasks(tasks, number)
        elif choice == "4":
            show_tasks(tasks)
            number = int(input("Task number to remove: "))
            remove_tasks(tasks, number)
        elif choice == "5":
            print("Goodbye!")
            break
        else:
            print("Invalid option, try again")

main()

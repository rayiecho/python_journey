tasks = []
def add_task(task):
    tasks.append(task)
    print(f"added: {task}")

def view_tasks():
    if not tasks:
        print("No task yet")
        return
    for i, task in enumerate(tasks, start = 1):     
        print(f"{i}.{task}")

def remove_task(number):
    if 1<=number<=len(tasks):
        removed = tasks.pop(number - 1)
        print(f"Removed : {removed}")
    else:
        print("Invalid Task number")  

def complete_tasks(tasks, number):
    if number < 1 or number > len(tasks):
        print("Invalid task")
        return
    tasks[number - 1]["Done"] = True
    print(f"task  {number} Marked as done!" )



def main():
 while True:
    print("\n----To Do List---")    
    print("1.Add Task.")
    print("2.View Task")
    print("3.Remove Task.")
    print("4.Complete Task.")
    print("5.Quit")     
    choice = input("Choose an option ")
    if choice == "1":
       task = input("Enter task")
       add_task(task)
    elif choice == "2":
       view_tasks()
    elif choice == "3":
       view_tasks()
       number = int(input("Enter task number to remove "))
       remove_task(number)
    elif choice == "4":
            view_tasks()
            number = int(input("Task number to complete: "))
            complete_tasks(tasks, number)

    elif choice == "5":
      name = input("Enter your name ")
      print(f"Goodbye, {name}, baba, see you again, you earned it my love.")
      break  
    else:
       print("Invalid Choice, kindly try again later!")      

main()

tasks = []

def display_menu():
    print("\nTO-DO List Application")
    print("1. View TO-DO List")
    print("2. Add Task")
    print("3. Update Task")
    print("4. Delete Task")
    print("5. Exit")

def view_tasks():
    if not tasks:
        print("\nYour TO-DO list is empty.")
    else:
        print("\nYour TO-DO List:")
        for idx, task in enumerate(tasks, 1):
            print(f"{idx}. {task}")

def add_task():
    task = input("\nEnter the task: ")
    tasks.append(task)
    print(f"Task '{task}' added to the TO-DO list.")

def delete_task():
    if not tasks:
        print("\nYour TO-DO list is empty.")
        return
    
    view_tasks()
    try:
        task_num = int(input("\nEnter the number of the task to delete: "))
        if 1 <= task_num <= len(tasks):
            removed_task = tasks.pop(task_num - 1)
            print(f"Task '{removed_task}' removed from the TO-DO list.")
        else:
            print("Invalid task number.")
    except ValueError:
        print("Please enter a valid number.")
def update_task():
    if not tasks:
        print("\nYour TO-DO list is empty.")
        return
    
    view_tasks()
    try:
        task_num = int(input("\nEnter the number of the task to update: "))
        if 1 <= task_num <= len(tasks):
            updated_task = input("Enter the updated task: ")
            tasks[task_num - 1] = updated_task
            print(f"Task {task_num} updated to '{updated_task}'.")
        else:
            print("Invalid task number.")
    except ValueError:
        print("Please enter a valid number.")
        
def main():
    while True:
        display_menu()
        choice = input("\nEnter your choice: ")
        if choice == '1':
            view_tasks()
        elif choice == '2':
            add_task()
        elif choice == '3':
            update_task()
        elif choice == '4':
            delete_task()
        elif choice == '5':
            print("Exiting the TO-DO List Application.")
            break
        else:
            print("Invalid choice. Please try again.")
main()

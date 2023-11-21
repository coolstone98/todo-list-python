import os
import time

def display_menu():
    time.sleep(1)
    print()
    print("Press 1 to view you todo list: ")
    print("Press 2 to add a task: ")
    print("Press 3 to complete a task: ")
    print("Press 4 to remove task: ")
    print("Press 5 to exit your todo list: ")
    print()
    
def view_task():
    with open("tasks.txt", "r") as file:
        tasks = file.readlines()
        if tasks:
            for index, task in enumerate(tasks, start=1):
                print(f"{index} - {task.strip()}")
        else:
            print("No tasks currently in todo list")
            
def add_task():
    task = input("Please add your task here: ")
    with open("tasks.txt", "a") as file:
        file.write(task + "\n")
    print(f"Task {task} added successfully")

def complete_task():
    view_task()
    try:
        task_number = int(input("Enter the number of task to complete: "))
        with open("tasks.txt", "r") as file:
            tasks = file.readlines()
            if 1 <= task_number <= len(tasks):
                completed_task = tasks.pop(task_number - 1)
                with open("tasks.txt", "w") as file:
                    file.writelines(tasks)
                print(f"Task {completed_task} successfully marked as complete")
            else:
                print("Task not found")
    except ValueError:
        print("please enter a number")

def remove_task():
    view_task()
    try:
        task_number = int(input("Enter the number of task to remove: "))
        with open("tasks.txt", "r") as file:
            tasks = file.readlines()
            if 1 <= task_number <= len(tasks):
                removed_task = tasks.pop(task_number - 1)
                with open("tasks.txt", "w") as file:
                    file.writelines(tasks)
                print(f"Task {removed_task} successfully removed")
            else:
                print("Task not found")
    except ValueError:
        print("please enter a number")
        
        
def main():
    while True:
        display_menu()
        choice = int(input("Enter an option here: "))
        
        if choice == 1:
            view_task()
        elif choice == 2:
            add_task()
        elif choice == 3:
            complete_task()
        elif choice == 4:
            remove_task()
        elif choice == 5:
            print("Todo list exited. Good Bye")
            break
        else:
            if type(choice) != int:
                print("Please enter a number")
            print("Number entered is not an option")
        
if __name__ == "__main__":
    if not os.path.exists("tasks.txt"):
        with open("tasks.txt", "w"):
            pass
    main()
                
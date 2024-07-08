class Task:
    def __init__(self, description):
        self.description = description
        self.completed = False

    def __str__(self):
        status = "✓" if self.completed else "✗"
        return f"[{status}] {self.description}"

import json
class ToDoList:
    def __init__(self):
        self.tasks = []

    def add_task(self, description):
        task = Task(description)
        self.tasks.append(task)

    def view_tasks(self):
        for i, task in enumerate(self.tasks, 1):
            print(f"{i}. {task}")

    def mark_complete(self, index):
        if 0 <= index < len(self.tasks):
            self.tasks[index].completed = True

    def delete_task(self, index):
        if 0 <= index < len(self.tasks):
            del self.tasks[index]

    
def main():
    todo_list = ToDoList()

    while True:
        print("\nTo-Do List Application")
        print("1. Create a task")
        print("2. track all tasks")
        print("3. Updation of task completion")
        print("4. Delete a task")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            description = input("Enter the task description: ")
            todo_list.add_task(description)
        elif choice == '2':
            
            todo_list.view_tasks()
            
        elif choice == '3':
            
            index = int(input("Enter the task number to mark as complete: ")) - 1
            todo_list.mark_complete(index)
            
        elif choice == '4':
            index = int(input("Enter the task number to delete: ")) - 1
            todo_list.delete_task(index)
        elif choice == '5':
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()

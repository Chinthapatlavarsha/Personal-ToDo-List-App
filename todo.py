import json

class Task:
    def _init_(self, title, description, category):
        self.title = title
        self.description = description
        self.category = category
        self.completed = False

    def mark_completed(self):
        self.completed = True

    def _repr_(self):
        return f"Task(title='{self.title}', description='{self.description}', category='{self.category}', completed={self.completed})"

def save_tasks(tasks):
    with open('tasks.json', 'w') as f:
        json.dump([task._dict_ for task in tasks], f, indent=4)

def load_tasks():
    try:
        with open('tasks.json', 'r') as f:
            task_data = json.load(f)
            return [Task(**data) for data in task_data]
    except FileNotFoundError:
        return []

def main():
    tasks = load_tasks()
    
    while True:
        print("\n=== To-Do List Application ===")
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Mark Task Completed")
        print("4. Delete Task")
        print("5. Exit")
        
        choice = input("Choose an option: ")
        
        if choice == '1':
            title = input("Task Title: ")
            description = input("Task Description: ")
            category = input("Task Category (e.g., Work, Personal): ")
            tasks.append(Task(title, description, category))
            print("Task added successfully.")
        
        elif choice == '2':
            if tasks:
                for idx, task in enumerate(tasks, start=1):
                    status = "Completed" if task.completed else "Pending"
                    print(f"{idx}. {task.title} ({task.category}) - {status}")
                    print(f"   Description: {task.description}")
            else:
                print("No tasks found.")
        
        elif choice == '3':
            for idx, task in enumerate(tasks, start=1):
                status = "Completed" if task.completed else "Pending"
                print(f"{idx}. {task.title} - {status}")
            task_idx = int(input("Enter the task number to mark as completed: ")) - 1
            tasks[task_idx].mark_completed()
            print("Task marked as completed.")
        
        elif choice == '4':
            for idx, task in enumerate(tasks, start=1):
                print(f"{idx}. {task.title}")
            task_idx = int(input("Enter the task number to delete: ")) - 1
            tasks.pop(task_idx)
            print("Task deleted successfully.")
        
        elif choice == '5':
            save_tasks(tasks)
            print("Tasks saved. Exiting...")
            break

        else:
            print("Invalid choice. Please try again.")

# Call the main function directly
main()

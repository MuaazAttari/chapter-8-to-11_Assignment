from datetime import datetime

def log_task(task_name: str):
    """Writes the task with timestamp into tasks.txt"""
    with open("tasks.txt", "a") as file:
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        file.write(f"[{timestamp}] {task_name}\n")
    print("✅ Task logged successfully.\n")

def show_all_tasks():
    """Reads and displays all tasks from tasks.txt"""
    try:
        with open("tasks.txt", "r") as file:
            tasks = file.readlines()
            if not tasks:
                print("🟡 No tasks found.\n")
            else:
                print("📋 All Logged Tasks:")
                for task in tasks:
                    print(task.strip())
    except FileNotFoundError:
        print("⚠️ 'tasks.txt' not found. No tasks logged yet.\n")

# Testing the functions
if __name__ == "__main__":
    while True:
        print("\n--- Task Logger Menu ---")
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Exit")
        
        choice = input("Enter your choice (1/2/3): ")

        if choice == '1':
            task = input("Enter your task: ")
            log_task(task)
        elif choice == '2':
            show_all_tasks()
        elif choice == '3':
            print("👋 Exiting Task Logger.")
            break
        else:
            print("❌ Invalid choice. Try again.")

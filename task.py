from datetime import datetime, timedelta

class TaskManager:
    def __init__(self):
        self.tasks = []

    def add_task(self, task, deadline=None, priority=None):
        task_info = {"task": task, "completed": False, "deadline": deadline, "priority": priority}
        self.tasks.append(task_info)
        print(f"Task '{task}' added successfully!")

    def view_tasks(self):
        if not self.tasks:
            print("No tasks available.")
        else:
            print("Tasks:")
            for idx, task_info in enumerate(self.tasks, start=1):
                status = "Completed" if task_info["completed"] else "Not Completed"
                deadline_info = f" | Deadline: {task_info['deadline']}" if task_info['deadline'] else ""
                priority_info = f" | Priority: {task_info['priority']}" if task_info['priority'] else ""
                print(f"{idx}. {task_info['task']} - {status}{deadline_info}{priority_info}")

    def mark_task_completed(self, task_index):
        if 1 <= task_index <= len(self.tasks):
            self.tasks[task_index - 1]["completed"] = True
            print(f"Task '{self.tasks[task_index - 1]['task']}' marked as completed.")
        else:
            print("Invalid task index.")

    def edit_task(self, task_index):
        if 1 <= task_index <= len(self.tasks):
            new_task = input("Enter the updated task: ")
            self.tasks[task_index - 1]["task"] = new_task
            print(f"Task updated successfully.")
        else:
            print("Invalid task index.")

    def delete_task(self, task_index):
        if 1 <= task_index <= len(self.tasks):
            deleted_task = self.tasks.pop(task_index - 1)
            print(f"Task '{deleted_task['task']}' deleted successfully.")
        else:
            print("Invalid task index.")

def main():
    task_manager = TaskManager()

    while True:
        print("\nTask Manager Menu:")
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Mark Task as Completed")
        print("4. Edit Task")
        print("5. Delete Task")
        print("6. Quit")

        choice = input("Enter your choice (1-6): ")

        if choice == "1":
            task = input("Enter the task: ")
            deadline = input("Enter the deadline (YYYY-MM-DD): ")
            priority = input("Enter the priority (High/Medium/Low): ")
            task_manager.add_task(task, deadline, priority)
        elif choice == "2":
            task_manager.view_tasks()
        elif choice == "3":
            task_manager.view_tasks()
            task_index = int(input("Enter the task index to mark as completed: "))
            task_manager.mark_task_completed(task_index)
        elif choice == "4":
            task_manager.view_tasks()
            task_index = int(input("Enter the task index to edit: "))
            task_manager.edit_task(task_index)
        elif choice == "5":
            task_manager.view_tasks()
            task_index = int(input("Enter the task index to delete: "))
            task_manager.delete_task(task_index)
        elif choice == "6":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 6.")

if __name__ == "__main__":
    main()

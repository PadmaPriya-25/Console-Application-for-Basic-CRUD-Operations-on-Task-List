# Task class to represent each task
class Task:
    def __init__(self, task_id, name, description, due_date):
        self.task_id = task_id
        self.name = name
        self.description = description
        self.due_date = due_date

    def __str__(self):
        return f"ID: {self.task_id}\nName: {self.name}\nDescription: {self.description}\nDue Date: {self.due_date}"


# TaskManager class to manage the tasks
class TaskManager:
    def __init__(self):
        self.tasks = []
        self.task_id_counter = 1

    # Create a new task
    def create_task(self):
        name = input("Enter task name: ")
        description = input("Enter task description: ")
        due_date = input("Enter task due date (YYYY-MM-DD): ")

        task = Task(self.task_id_counter, name, description, due_date)
        self.tasks.append(task)
        self.task_id_counter += 1
        print("Task created successfully!\n")

    # Read and display all tasks
    def read_tasks(self):
        if not self.tasks:
            print("No tasks available.\n")
        else:
            for task in self.tasks:
                print(task)
                print("-" * 30)

    # Update an existing task
    def update_task(self):
        task_id = int(input("Enter the task ID to update: "))
        task = self.find_task_by_id(task_id)

        if task:
            task.name = input(f"Enter new task name (current: {task.name}): ") or task.name
            task.description = input(f"Enter new task description (current: {task.description}): ") or task.description
            task.due_date = input(f"Enter new task due date (current: {task.due_date}): ") or task.due_date
            print("Task updated successfully!\n")
        else:
            print("Task not found!\n")

    # Delete a task
    def delete_task(self):
        task_id = int(input("Enter the task ID to delete: "))
        task = self.find_task_by_id(task_id)

        if task:
            self.tasks.remove(task)
            print("Task deleted successfully!\n")
        else:
            print("Task not found!\n")

    # Helper method to find a task by ID
    def find_task_by_id(self, task_id):
        for task in self.tasks:
            if task.task_id == task_id:
                return task
        return None


# Main menu loop
def main():
    task_manager = TaskManager()

    while True:
        print("Task Manager - Choose an option:")
        print("1. Create Task")
        print("2. Read Tasks")
        print("3. Update Task")
        print("4. Delete Task")
        print("5. Exit")

        choice = input("Enter your choice (1-5): ")

        if choice == "1":
            task_manager.create_task()
        elif choice == "2":
            task_manager.read_tasks()
        elif choice == "3":
            task_manager.update_task()
        elif choice == "4":
            task_manager.delete_task()
        elif choice == "5":
            print("Exiting the program.")
            break
        else:
            print("Invalid choice. Please select a valid option.\n")


if __name__ == "__main__":
    main()

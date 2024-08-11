class TodoStack:
    def __init__(self):
        self.stack = []

    def add_task(self, task):
        self.stack.append(task)
        print(f"Task added: {task}")

    def remove_task(self):
        if self.stack:
            removed_task = self.stack.pop()
            print(f"Task removed: {removed_task}")
        else:
            print("No tasks to remove.")

    def display_tasks(self):
        if not self.stack:
            print("No tasks to display.")
        else:
            print("To-Do List (from most recent to oldest):")
            for i, task in enumerate(reversed(self.stack), 1):
                print(f"{i}. {task}")

def main():
    todo_stack = TodoStack()

    while True:
        print("\n1. Add Task")
        print("2. Remove Task")
        print("3. Display Tasks")
        print("4. Exit")
        choice = input("Choose an option: ")

        if choice == '1':
            task = input("Enter the task: ")
            todo_stack.add_task(task)
        elif choice == '2':
            todo_stack.remove_task()
        elif choice == '3':
            todo_stack.display_tasks()
        elif choice == '4':
            print("Exiting...")
            break
        else:
            print("Invalid option. Please try again.")

if __name__ == "__main__":
    main()

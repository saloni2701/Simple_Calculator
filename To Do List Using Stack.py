class TodoStack:
    def init(self):
        self.stack = []

    def add(self, task):
        """A new task is pushed onto the stack."""
        self.stack.append(task)
        print(f"Task added: {task}")

    def remove(self):
        """The most recent task is poped from the stack."""
        if self.stack:
            removed_task = self.stack.pop()
            print(f"Task removed: {removed_task}")
        else:
            print("No tasks to remove.")

    def display(self):
        """All tasks are displayed in the stack."""
        if not self.stack:
            print("No tasks to display.")
        else:
            print("To-Do List (from most recent to oldest):")
            for i, task in enumerate(reversed(self.stack)):
                print(f"{i + 1}. {task}")

def main():
    todo_list = TodoStack()

    while True:
        print("\n1. Add Task")
        print("2. Remove Task")
        print("3. Display Tasks")
        print("4. Exit")
        choice = input("Choose an option: ")

        if choice == '1':
            task = input("Enter the task: ")
            todo_list.add_task(task)
        elif choice == '2':
            todo_list.remove_task()
        elif choice == '3':
            todo_list.display_tasks()
        elif choice == '4':
            print("Exiting The To Do List...")
            break
        else:
            print("Invalid option. Please try again.")

if __name__ == "__main__":
    main()

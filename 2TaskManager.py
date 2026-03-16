import json
import os
from datetime import datetime

class Task:
  def __init__(self,title,priority,due_date):
    self.title=title
    self.priority=priority
    self.due_date=due_date
    self.created=datetime.now().strftime("%Y-%m-%d %H:%M")
    self.completed=False
    
  def to_dict(self):
    return{
       "title":self.title,
       "priority":self.priority,
       "due_date":self.due_date,
       "created":self.created,
       "completed":self.completed
       
    }
  @staticmethod
  def from_dict(data):
    task=Task(data["title"],data["priority"],data["due_date"])
    task.created=data["created"]
    task.completed=data["completed"]
    return task


"""import json
import os
from datetime import datetime

class Task:
    def __init__(self, title, priority, due_date):
        self.title = title
        self.priority = priority
        self.due_date = due_date
        self.created = datetime.now().strftime("%Y-%m-%d %H:%M")
        self.completed = False

    def to_dict(self):
        return {
            "title": self.title,
            "priority": self.priority,
            "due_date": self.due_date,
            "created": self.created,
            "completed": self.completed
        }

    @staticmethod
    def from_dict(data):
        task = Task(data["title"], data["priority"], data["due_date"])
        task.created = data["created"]
        task.completed = data["completed"]
        return task


class TaskManager:
    FILE = "tasks.json"

    def __init__(self):
        self.tasks = []
        self.load_tasks()

    def add_task(self, title, priority, due_date):
        task = Task(title, priority, due_date)
        self.tasks.append(task)
        self.save_tasks()
        print("Task added successfully!")

    def list_tasks(self):
        if not self.tasks:
            print("No tasks available.")
            return

        sorted_tasks = sorted(self.tasks, key=lambda t: (t.priority, t.due_date))

        for i, task in enumerate(sorted_tasks):
            status = "✔" if task.completed else "✘"
            print(f"{i+1}. [{status}] {task.title}")
            print(f"   Priority: {task.priority}")
            print(f"   Due: {task.due_date}")
            print(f"   Created: {task.created}")

    def complete_task(self, index):
        try:
            self.tasks[index].completed = True
            self.save_tasks()
            print("Task completed!")
        except IndexError:
            print("Invalid task number.")

    def delete_task(self, index):
        try:
            del self.tasks[index]
            self.save_tasks()
            print("Task deleted!")
        except IndexError:
            print("Invalid task number.")

    def save_tasks(self):
        with open(self.FILE, "w") as f:
            json.dump([t.to_dict() for t in self.tasks], f, indent=4)

    def load_tasks(self):
        if os.path.exists(self.FILE):
            with open(self.FILE, "r") as f:
                data = json.load(f)
                self.tasks = [Task.from_dict(d) for d in data]


def menu():
    manager = TaskManager()

    while True:
        print("\n==== TASK MANAGER ====")
        print("1. Add Task")
        print("2. List Tasks")
        print("3. Complete Task")
        print("4. Delete Task")
        print("5. Exit")

        choice = input("Choose option: ")

        if choice == "1":
            title = input("Task title: ")
            priority = int(input("Priority (1=High, 5=Low): "))
            due_date = input("Due date (YYYY-MM-DD): ")
            manager.add_task(title, priority, due_date)

        elif choice == "2":
            manager.list_tasks()

        elif choice == "3":
            manager.list_tasks()
            idx = int(input("Task number to complete: ")) - 1
            manager.complete_task(idx)

        elif choice == "4":
            manager.list_tasks()
            idx = int(input("Task number to delete: ")) - 1
            manager.delete_task(idx)

        elif choice == "5":
            print("Goodbye!")
            break

        else:
            print("Invalid choice.")


if __name__ == "__main__":
    menu()
    """

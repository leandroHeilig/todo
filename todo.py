from datetime import datetime

class Project:
    def __init__(self, name):
        self.name = name
        self.tasks = []

    def add_task(self, task):
        self.tasks.append(Task(task))

    def get_pending_tasks(self):
        return [task for task in self.tasks if not task.completed]
    
    def find_task(self, description):
        for task in self.tasks:
            if task.description == description:
                return task
        return None

    def __str__(self):
        return f"Project: {self.name}, Tasks: {len(self.get_pending_tasks())} pending"
    
class Task:
    def __init__(self, description, due_date=None):
        self.description = description
        self.due_date = due_date
        self.completed = False
        self.created_at = datetime.now()

    def mark_complete(self):
        self.completed = True

    def __str__(self):
        status = "Completed" if self.completed else "Pending"
        due = f", Due: {self.due_date}" if self.due_date else ""
        return f"Task: {self.description}{due}, Status: {status}"

def main():
    project = Project("Sample Project")
    project.add_task("Passar roupa")
    project.add_task("Lavar Louça")

    print(project)

    task = project.find_task("Passar roupa")
    if task:
        print(task)
        task.mark_complete()
        print("After marking complete:")
        print(task)

    print("Pending tasks:")
    for pending_task in project.get_pending_tasks():
        print(pending_task)
    
    go_shopping = Project("Go Shopping")
    go_shopping.add_task("Buy groceries")
    go_shopping.add_task("Buy fruits")

    print(go_shopping)

    for task in go_shopping.get_pending_tasks():
        print(f'-{task}')

    buy_fruits = go_shopping.find_task("Buy fruits")
    if buy_fruits:
        buy_fruits.mark_complete()

    

if __name__ == "__main__":
    main()
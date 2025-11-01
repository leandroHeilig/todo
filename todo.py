from datetime import datetime, timedelta

class Project:
    def __init__(self, name):
        self.name = name
        self.tasks = []
        
    def __interact__(self, other):
        return self.tasks.__interact__(other)

    def add_task(self, task, due_date=None):
        self.tasks.append(Task(task, due_date))

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
        status = []
        if self.completed:
            status.append("(Completed)")
        elif self.due_date:
            if datetime.now() > self.due_date:
                status.append("(Overdue)")
            else: 
                days_left = (self.due_date - datetime.now()).days
                status.append(f"(Due in {days_left} days)")
        return f"{self.description} {' '.join(status)}"
    
class RecurringTask(Task):
    def __init__(self, description, due_date, interval_days=7):
        super().__init__(description, due_date)
        self.interval_days = interval_days
       

    def mark_complete(self):
        super().mark_complete()
        new_due_date = datetime.now() + datetime.timedelta(days=self.interval_days)
        return RecurringTask(self.description, new_due_date, self.interval_days)
        # Logic to create a new task after the interval can be added here

    def mark_complete(self):
        super().mark_complete()
        # Logic to create a new task after the interval can be added here
        
def main():
    project = Project("Sample Project")
    project.add_task("Passar roupa",datetime.now())
    project.add_task("Lavar Louça", datetime(2025, 12, 31))
    project.add_task("Comprar mantimentos", datetime.now()+ timedelta(days=3))
    #project.tasks.append(RecurringTask("Pagar contas", datetime.now(), 7))
    project.tasks.append(RecurringTask("Pagar contas", datetime.now(), 7))

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
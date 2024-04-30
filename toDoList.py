class ToDoList:
    def __init__(self):
        self.tasks = []

    def add_task(self, task, priority):
        # Ensure priority is stored as an integer for easier sorting
        self.tasks.append([task, int(priority)])

    def delete_task(self, task):
        for list_item in self.tasks:
            if list_item[0] == task:
                self.tasks.remove(list_item)
                return
        print("Task not found!")

    def get_tasks(self):
        # Return the tasks sorted by priority (higher priority first)
        return sorted(self.tasks, key=lambda x: x[1], reverse=True)

    def update_priority(self, task, new_priority):
        # Update the priority for a given task
        for list_item in self.tasks:
            if list_item[0] == task:
                list_item[1] = int(new_priority)
                return
        print("Task not found!")

    def clear_tasks(self):
        self.tasks.clear()

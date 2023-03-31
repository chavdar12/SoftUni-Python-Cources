from project.task import Task


class Section:

    def __init__(self, name: str):
        self.name = name
        self.tasks = []

    def add_task(self, new_task: Task):
        for t in self.tasks:
            if t.name == new_task.name:
                return f"Task is already in the section {self.name}"
        # else
        self.tasks.append(new_task)
        return f"Task {new_task.details()} is added to the section"

    def complete_task(self, task_name: str):
        for task in self.tasks:
            if task.name == task_name:
                task.completed = True
                return f"Completed task {task_name}"
            # not returning value will mean not found
        return f"Could not find task with the name {task_name}"

    def clean_section(self):
        tasks_count = 0
        for task in self.tasks:
            if task.completed:
                tasks_count += 1

                self.tasks.remove(task)
        return f"Cleared {tasks_count} tasks."

    def view_section(self):
        result = f"Section {self.name}:"
        for task in self.tasks:
            result += f"\n{task.details()}"
        return result


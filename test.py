class Task:
    def __init__(self, name, description, deadline):
        self.name = name
        self.description = description
        self.deadline = deadline
        self.completed = False

    def complete(self):
        self.completed = True


class Project:
    def __init__(self, name):
        self.name = name
        self.tasks = []

    def add_task(self, task):
        self.tasks.append(task)

    def find_task_by_name(self, task_name):
        for task in self.tasks:
            if task.name == task_name:
                return task
        return None

    def complete_task(self, task_name):
        task = self.find_task_by_name(task_name)
        if task:
            task.complete()
        else:
            print(f"Завдання '{task_name}' не знайдено")

    def display_tasks(self):
        print(f"Завдання для проекту '{self.name}':")
        for task in self.tasks:
            status = 'виконано' if task.completed else 'не виконано'
            print(f"- {task.name} ({task.description}) - Дедлайн: {task.deadline}, Статус: {status}")


project_1 = Project("Проект 1")
task_1 = Task("Завдання 1", "Опис завдання 1", "31.12.2023")
task_2 = Task("Завдання 2", "Опис завдання 2", "15.01.2024")

project_1.add_task(task_1)
project_1.add_task(task_2)

project_1.display_tasks()

project_1.complete_task("Завдання 1")

project_1.display_tasks()

class TaskList:
    def __init__(self):
        self._tasks = []

    def add_task(self, task):
        self._tasks.append(task)

    def remove_task(self, task):
        if task in self._tasks:
            self._tasks.remove(task)

    def add_multiple_task(self, tasks):
        self._tasks.extend(tasks)


    def tasks(self):
        return self._tasks

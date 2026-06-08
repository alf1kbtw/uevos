class Task:

    def __init__(self, task_id: str, description: str, priority: int):
        self.id = task_id
        self.description = description
        self.priority = priority


class TaskQueue:

    def __init__(self):
        self.items = []

    def enqueue(self, task: Task):
        self.items.append(task)

    def dequeue(self):
        if self.is_empty():
            print("Очередь задач пуста")
            return None
        return self.items.pop(0)

    def front(self):
        if self.is_empty():
            print("Очередь задач пуста")
            return None
        return self.items[0]

    def is_empty(self):
        return len(self.items) == 0

    def size(self):
        return len(self.items)

    def find_by_id(self, task_id: str):
        for task in self.items:
            if task.id == task_id:
                return task
        return None


if __name__ == "__main__":
    queue = TaskQueue()

    queue.enqueue(Task("T1", "Проверить отчет по второй лабе", 3))
    queue.enqueue(Task("T2", "Написать код для третьей лабораторной", 5))
    queue.enqueue(Task("T3", "Повторить теорию про FIFO и LIFO", 2))

    print(f"Всего задач в очереди: {queue.size()}")
    first_task = queue.front()
    if first_task:
        print(f"Первая задача на выполнение: [{first_task.id}] {first_task.description}")

    print("\n" + "─" * 60)
    print("ВАРИАТИВНАЯ ЧАСТЬ: Поиск задачи по ID")

    search_id = input("Введите ID задачи для поиска (например, T2): ")
    found = queue.find_by_id(search_id)

    if found:
        print(f"Успешно найдено -> ID: {found.id} | Описание: {found.description} | Приоритет: {found.priority}")
    else:
        print(f"Задача с ID '{search_id}' в очереди не найдена.")

    print("\n" + "─" * 60)
    print("ДЕМОНСТРАЦИЯ РАБОТЫ ОЧЕРЕДИ (FIFO):")

    while not queue.is_empty():
        current_task = queue.dequeue()
        print(f"Выполняется задача: [{current_task.id}] {current_task.description}...")

    print(f"\nОчередь пуста? {queue.is_empty()}")
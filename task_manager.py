import datetime

class Task:
    def __init__(self, title, priority, deadline=None):
        self.title = title
        self.priority = priority  # 1 - Низкий, 2 - Средний, 3 - Критический
        self.created_at = datetime.datetime.now()
        self.deadline = deadline  # Формат: YYYY-MM-DD
        self.is_completed = False

    def complete(self):
        self.is_completed = True

    def __repr__(self):
        status = "✅" if self.is_completed else "⏳"
        return f"[{self.priority}] {self.title} | Дедлайн: {self.deadline} | {status}"
    
tasks_storage = []

tasks_storage.sort(key=lambda x: x.priority, reverse=True)
print("--- Список дел отсортирован по важности ---")

task1 = Task("Выучить что-нибудь", 3, "2026-04-01")
tasks_storage.append(task1)

task2 = Task("Написать README", 2, "2026-03-31")
tasks_storage.append(task2)

task3 = Task("Сделать кофе", 1, "2026-03-30")
tasks_storage.append(task3)

print("--- Текущие задачи ---")
for t in tasks_storage:
    print(t)

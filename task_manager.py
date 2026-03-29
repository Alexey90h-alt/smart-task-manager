import datetime
import json  # Библиотека для работы с форматом JSON
import os    # Библиотека для работы с файловой системой

class Task:
    def __init__(self, title, priority, deadline=None):
        self.title = title
        self.priority = priority  # 1 - Низкий, 2 - Средний, 3 - Критический
        self.created_at = datetime.datetime.now()
        self.deadline = deadline
        self.is_completed = False

    def complete(self):
        self.is_completed = True

    # --- НОВЫЙ МЕТОД: Трансфигурация в словарь ---
    def to_dict(self):
        return {
            "title": self.title,
            "priority": self.priority,
            "deadline": self.deadline,
            "is_completed": self.is_completed
            # Дату создания пока пропустим, для простоты
        }

    def __repr__(self):
        status = "✅" if self.is_completed else "⏳"
        return f"[{self.priority}] {self.title} | Дедлайн: {self.deadline} | {status}"

# --- НОВАЯ ФУНКЦИЯ: Заклинание записи на диск ---
def save_tasks(tasks, filename="tasks.json"):
    # Мы превращаем каждый объект Task в простой словарь
    data = [t.to_dict() for t in tasks]
    with open(filename, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=4)
    print(f"\nЗадачи бережно сохранены в {filename}")

# --- ОСНОВНОЙ КОД ---
tasks_storage = []

# Создаем наши задачи
task1 = Task("Посмотреть урок на Skillbox", 3, "2026-04-01")
task2 = Task("Написать README", 2, "2026-03-31")
task3 = Task("Сделать кофе", 1, "2026-03-30")

tasks_storage.append(task1)
tasks_storage.append(task2)
tasks_storage.append(task3)

# Сортируем
tasks_storage.sort(key=lambda x: x.priority, reverse=True)

print("--- Текущие задачи ---")
for t in tasks_storage:
    print(t)

# --- ПРИМЕНЯЕМ СОХРАНЕНИЕ ---
save_tasks(tasks_storage)
import os

# 1. القالب الخاص بكل مهمة
class Task:
    def __init__(self, title, description, language):
        self.title = title
        self.description = description
        self.language = language
        self.is_completed = False

    def __str__(self):
        status = "[DONE]" if self.is_completed else "[PENDING]"
        return f"{status} | {self.language} | {self.title}"

# 2. المدير المسؤول عن العمليات
class TaskManager:
    def __init__(self, file_name="my_tasks.txt"):
        self.file_name = file_name
        self.tasks = []
        self.load_tasks()

    def add_task(self, title, description, language):
        new_task = Task(title, description, language)
        self.tasks.append(new_task)
        self.save_tasks()

    def save_tasks(self):
        with open(self.file_name, "w", encoding="utf-8") as f:
            for t in self.tasks:
                # التعديل هنا: نستخدم t.is_completed وليس self
                f.write(f"{t.title}|{t.description}|{t.language}|{t.is_completed}\n")

    def load_tasks(self):
        if os.path.exists(self.file_name):
            with open(self.file_name, "r", encoding="utf-8") as f:
                self.tasks = []
                for line in f:
                    data = line.strip().split("|")
                    if len(data) == 4:
                        t = Task(data[0], data[1], data[2])
                        t.is_completed = data[3] == "True"
                        self.tasks.append(t)

    def show_tasks(self):
        print("\n--- Current Tasks List ---")
        if not self.tasks:
            print("No tasks found.")
        for task in self.tasks:
            print(task)

# 3. تشغيل البرنامج
manager = TaskManager()

# إضافة مهمة جديدة
manager.add_task("Start Flutter", "Learn Dart and widgets", "Flutter/Dart")

# عرض المهام
manager.show_tasks()

print("\n✅ Task Manager Updated Successfully!")
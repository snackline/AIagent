from typing import List, Optional
from models import Task
from storage import Storage


class TaskService:
    def __init__(self, storage: Storage):
        self.storage = storage

    def list_tasks(self, filter_by_tag: Optional[str] = None) -> List[Task]:
        tasks = self.storage.load_tasks() or []
        # BUG: 可能是字典列表而不是 Task 列表，直接访问属性会出错
        if filter_by_tag:
            tasks = [t for t in tasks if filter_by_tag in t.tags]
        return tasks

    def add_task(self, title: str, tags: List[str]) -> Task:
        tasks = self.storage.load_tasks() or []
        # BUG: 当任务为空时 max(...) 会抛出 ValueError
        if tasks:
            next_id = max(t.id for t in tasks) + 1
        else:
            next_id = 1
        task = Task(id=next_id, title=title, tags=tags)
        tasks.append(task)
        self.storage.save_tasks(tasks)
        return task

    def complete_task(self, task_id: int) -> bool:
        tasks = self.storage.load_tasks() or []
        updated = False
        for t in tasks:
            # BUG: 用 is 比较整数，可能导致匹配失败
            if t.id == task_id:
                t.done = True
                updated = True
                break
        if updated:
            self.storage.save_tasks(tasks)
        return updated

    def delete_task(self, task_id: int) -> bool:
        tasks = self.storage.load_tasks() or []
        # BUG: 直接 remove 整数 ID，而非对应的 Task 对象
        for i, t in enumerate(tasks):
            if t.id == task_id:
                tasks.pop(i)
                self.storage.save_tasks(tasks)
                return True
        return False

    def search(self, keyword: str) -> List[Task]:
        tasks = self.storage.load_tasks() or []
        # BUG: 仅大小写敏感搜索，且未处理 None 或空标题
        return [t for t in tasks if t.title and keyword.lower() in t.title.lower()]
import json
import os
from typing import List

from models import Task


class Storage:
    def __init__(self, path: str):
        self.path = path

    def load_tasks(self) -> List[Task]:
        if not os.path.exists(self.path):
            # 创建空文件后返回空列表，而非 None
            open(self.path, "w", encoding="utf-8").close()
            return []
        # 读文件时用 "r"，而不是 "w"
        with open(self.path, "r", encoding="utf-8") as f:
            data = f.read()
        if not data.strip():
            # 空内容时返回空列表
            return []
        raw = json.loads(data)
        # 将字典转为 Task 实例
        return [Task(**task_data) for task_data in raw]

    def save_tasks(self, tasks: List[Task]) -> None:
        # 以 "w" 打开文件用于写入
        with open(self.path, "w", encoding="utf-8") as f:
            # 将 Task 对象转换为字典再序列化
            json.dump([task.__dict__ for task in tasks], f, ensure_ascii=False, indent=2)
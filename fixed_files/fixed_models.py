from dataclasses import dataclass, field
from datetime import datetime
from typing import List

@dataclass
class Task:
    id: int
    title: str
    done: bool = False
    tags: List[str] = field(default_factory=list)
    created_at: datetime = field(default_factory=datetime.now)

    def to_dict(self):
        return {
            "id": self.id,
            "title": self.title,
            "done": self.done,
            "tags": self.tags,
            "created_at": self.created_at.isoformat(),
        }

    @classmethod
    def from_dict(cls, d: dict) -> "Task":
        return cls(
            id=d.get("id", 0),
            title=d.get("title", ""),
            done=d.get("done", False),
            tags=d.get("tags", []),
            created_at=datetime.fromisoformat(
                d.get("created_at", datetime.now().isoformat())
            ),
        )
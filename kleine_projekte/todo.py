"""Kleines Projekt 2: Aufgabenliste (Todo List).

A simple in-memory todo list manager.
"""

from dataclasses import dataclass, field
from typing import List


@dataclass
class TodoItem:
    """Represents a single todo item."""

    title: str
    done: bool = False

    def complete(self) -> None:
        """Mark this item as done."""
        self.done = True

    def __str__(self) -> str:
        status = "✓" if self.done else "○"
        return f"[{status}] {self.title}"


class TodoList:
    """A simple in-memory todo list."""

    def __init__(self) -> None:
        self._items: List[TodoItem] = []

    def add(self, title: str) -> TodoItem:
        """Add a new item with *title* and return it."""
        item = TodoItem(title=title)
        self._items.append(item)
        return item

    def complete(self, index: int) -> None:
        """Mark the item at *index* (0-based) as done.

        Raises:
            IndexError: If *index* is out of range.
        """
        self._items[index].complete()

    def remove(self, index: int) -> TodoItem:
        """Remove and return the item at *index* (0-based).

        Raises:
            IndexError: If *index* is out of range.
        """
        return self._items.pop(index)

    def pending(self) -> List[TodoItem]:
        """Return all items that are not yet done."""
        return [item for item in self._items if not item.done]

    def all_items(self) -> List[TodoItem]:
        """Return all items."""
        return list(self._items)

    def __len__(self) -> int:
        return len(self._items)

    def __str__(self) -> str:
        if not self._items:
            return "Keine Aufgaben vorhanden."
        return "\n".join(str(item) for item in self._items)

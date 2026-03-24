"""Tests for the TodoList class."""

import pytest
from kleine_projekte.todo import TodoItem, TodoList


def test_add_item():
    todo = TodoList()
    item = todo.add("Buy milk")
    assert item.title == "Buy milk"
    assert not item.done
    assert len(todo) == 1


def test_complete_item():
    todo = TodoList()
    todo.add("Write tests")
    todo.complete(0)
    assert todo.all_items()[0].done


def test_complete_invalid_index():
    todo = TodoList()
    with pytest.raises(IndexError):
        todo.complete(0)


def test_remove_item():
    todo = TodoList()
    todo.add("Task A")
    todo.add("Task B")
    removed = todo.remove(0)
    assert removed.title == "Task A"
    assert len(todo) == 1


def test_pending_filters_done():
    todo = TodoList()
    todo.add("Task 1")
    todo.add("Task 2")
    todo.complete(0)
    pending = todo.pending()
    assert len(pending) == 1
    assert pending[0].title == "Task 2"


def test_str_empty():
    todo = TodoList()
    assert str(todo) == "Keine Aufgaben vorhanden."


def test_str_with_items():
    todo = TodoList()
    todo.add("Aufgabe 1")
    todo.complete(0)
    todo.add("Aufgabe 2")
    output = str(todo)
    assert "[✓] Aufgabe 1" in output
    assert "[○] Aufgabe 2" in output


def test_todo_item_str():
    item = TodoItem(title="Test")
    assert str(item) == "[○] Test"
    item.complete()
    assert str(item) == "[✓] Test"

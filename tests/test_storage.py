import json
from task_manager.storage import save_tasks, load_tasks
from task_manager.models.tasks import Task

def test_save_and_load_tasks(tmp_path, monkeypatch):

    # Create a temporary file path for testing
    temp_file = tmp_path / "test_tasks.json"

    # Force the storage module to use the temporary file path
    monkeypatch.setattr("task_manager.storage.tasks_file", temp_file)

    tasks = [
        Task(1, "Test 1"),
        Task(2, "Test 2", completed=True)
    ]

    save_tasks(tasks)
    loaded_tasks = load_tasks()

    assert len(loaded_tasks) == 2
    assert loaded_tasks[0].title == "Test 1"
    assert loaded_tasks[1].completed is True

def test_load_tasks_when_file_does_not_exist(tmp_path, monkeypatch):

    temp_file = tmp_path / "nonexistent.json"

    monkeypatch.setattr("task_manager.storage.tasks_file", temp_file)

    tasks = load_tasks()

    assert tasks == []

def test_save_empty_list(tmp_path, monkeypatch):

    temp_file = tmp_path / "empty.json"

    monkeypatch.setattr("task_manager.storage.tasks_file", temp_file)

    save_tasks([])

    loaded_tasks = load_tasks()

    assert loaded_tasks == []
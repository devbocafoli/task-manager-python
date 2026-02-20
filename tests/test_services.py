import pytest
from task_manager.services import add_task, delete_task, list_tasks, toggle_task_status, find_task_by_id, generate_next_id
from task_manager.models.tasks import Task

def test_generate_next_id():

    tasks = []
    assert generate_next_id(tasks) == 1

    tasks.append(Task(1, 'Test 1'))
    assert generate_next_id(tasks) == 2

def test_generate_next_id_existing_ids():

    tasks = [
        Task(1, 'Test 1'),
        Task(4, 'Test 2'),
        Task(5, 'Test 3'),
    ]
    assert generate_next_id(tasks) == 6

def test_find_task_by_id_found():

    tasks = [
        Task(1, 'Test 1'),
        Task(2, 'Test 2', completed=True),
        Task(3, 'Test 3')
    ]

    task = find_task_by_id(tasks, 2)

    assert task is not None
    assert task.id == 2
    assert task.title == 'Test 2'
    assert task.completed is True

def test_find_task_by_id_not_found():

    tasks = [
        Task(1, 'Test 1'),
        Task(2, 'Test 2'),
        Task(3, 'Test 3')
    ]
    task = find_task_by_id(tasks, 4)

    assert task is None

def test_add_task(monkeypatch):

    fake_tasks = []

    # Simulate save_tasks to avoid saving to the actual file.
    def fake_save(tasks):
        pass

    monkeypatch.setattr('task_manager.services.save_tasks', fake_save)

    new_task = add_task(fake_tasks, 'New Task Test')

    assert new_task.id == 1
    assert new_task.title == 'New Task Test'
    assert new_task.completed is False
    assert len(fake_tasks) == 1

def test_delete_task(monkeypatch):

    fake_tasks = [
        Task(1, 'Test 1'),
        Task(2, 'Test 2', completed=True),
        Task(3, 'Test 3')
    ]
    # Simulate load_tasks to return the fake_tasks list.
    def fake_load():
        return fake_tasks
    
    # Simulate save_tasks to avoid saving to the actual file.
    def fake_save(tasks):
        pass

    monkeypatch.setattr('task_manager.services.load_tasks', fake_load)
    monkeypatch.setattr('task_manager.services.save_tasks', fake_save)

    deleted_task = delete_task(2)

    assert deleted_task.id == 2
    assert deleted_task.title == 'Test 2'
    assert deleted_task.completed is True

def test_toggle_task_status(monkeypatch):

    fake_tasks = [
        Task(1, 'Test 1'),
        Task(2, 'Test 2', completed=True),
        Task(3, 'Test 3')
    ]

    # Simulate load_tasks to return the fake_tasks list.
    def fake_load():
        return fake_tasks
    
    # Simulate save_tasks to avoid saving to the actual file.
    def fake_save(tasks):
        pass

    monkeypatch.setattr('task_manager.services.load_tasks', fake_load)
    monkeypatch.setattr('task_manager.services.save_tasks', fake_save)

    toggled_task = toggle_task_status(2)

    assert toggled_task.id == 2
    assert toggled_task.title == 'Test 2'
    assert toggled_task.completed is False

    toggled_task = toggle_task_status(3)

    assert toggled_task.id == 3
    assert toggled_task.title == 'Test 3'
    assert toggled_task.completed is True
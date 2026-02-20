import pytest
from task_manager.models.tasks import Task

def test_task_creation():

    task = Task(id=1, title="Test Task Creation")

    assert task.id == 1
    assert task.title == 'Test Task Creation'
    assert task.completed is False

def test_toggle_status():

    task = Task(id=2, title='Test Task Toggle')

    task.toggle_status()
    assert task.completed is True

    task.toggle_status()
    assert task.completed is False

def test_to_dict():

    task = Task(id=3, title='Test Task to dict', completed=True)

    task_dict = task.to_dict()

    assert task_dict == {
        'id' : 3,
        'title' : 'Test Task to dict',
        'completed' : True
    }

def test_from_dict():

    task_data = {
        'id' : 4,
        'title' : 'Test Task from dict',
        'completed' : True
    }

    task = Task.from_dict(task_data)

    assert task.id == 4
    assert task.title == 'Test Task from dict'
    assert task.completed is True
from time import sleep
from services.storage import load_tasks, save_tasks

def add_task(title):

    """Add a new task to the tasks and return it."""

    if not title.strip():

        raise ValueError('Task title cannot be empty.')

    new_task = {
        'title' : title,
        'completed' : False
    }

    tasks = load_tasks()

    tasks.append(new_task)
    save_tasks(tasks)

    return new_task


def delete_task(index):

    """Deletes a task by its index and returns the removed task."""
    
    tasks = load_tasks()

    if not tasks:
        raise ValueError('No tasks found to delete.')

    if index < 1 or index > len(tasks):
        raise IndexError('Task index does not exist.')

    removed_task = tasks.pop(index - 1)
    save_tasks(tasks)

    return removed_task
            
        
def list_tasks():

    """Return all tasks in the tasks list."""

    return load_tasks()


def toggle_task_status(index):

    """Toggles the completion status of a task and returns the updated task."""

    tasks = load_tasks()

    if not tasks:
        raise ValueError('No tasks found to toggle.')
    
    if index < 1 or index > len(tasks):
        raise IndexError('Task index does not exist.')

    else:

        tasks[index - 1]['completed'] = not tasks[index - 1]['completed']
        save_tasks(tasks)

        return tasks[index - 1]
        


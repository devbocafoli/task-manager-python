from task_manager.storage import load_tasks, save_tasks
from task_manager.models.tasks import Task

def add_task(tasks, title):

    """Add a new task to the tasks and return it."""

    if not title.strip():
        raise ValueError('Task title cannot be empty')
    
    new_id = generate_next_id(tasks)
    new_task = Task(new_id, title)

    tasks.append(new_task)
    save_tasks(tasks)

    return new_task
    

def delete_task(task_id_to_delete):

    """Deletes a task by its task_id and returns them removed task."""
    
    tasks = load_tasks()

    if not tasks:
        raise ValueError('No tasks found to delete')

    task = find_task_by_id(tasks, task_id_to_delete)
    
    if not task:
        raise IndexError('Task ID does not exist')

    tasks.remove(task)
    save_tasks(tasks)

    return task
            
        
def list_tasks():

    """Return all tasks in the tasks list."""

    return load_tasks()


def toggle_task_status(task_id_to_toggle):

    """Toggles the completion status of a task and returns them task."""

    tasks = load_tasks()

    if not tasks:
        raise ValueError('No tasks found to toggle')
    
    task = find_task_by_id(tasks, task_id_to_toggle)

    if not task:
        raise IndexError('Task ID does not exist')

    else:
        task.completed = not task.completed

        save_tasks(tasks)

        return task
        

def generate_next_id(tasks):

    """Generate the next task ID based on the existing tasks."""

    if not tasks:
        return 1
    
    return max(task.id for task in tasks) + 1


def find_task_by_id(tasks, task_id):

    """Find a task by its ID and return it."""

    print('Searching for ID:', task_id)
    for task in tasks:
        print('Checking task ID:', task.id, type(task.id))
        if task.id == task_id:
            return task
        
    return None
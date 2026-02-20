import json
from task_manager.models.tasks import Task
from pathlib import Path

FILE_PATH = Path(__file__).parent.parent.parent
tasks_file = FILE_PATH / "data" / "data.json"

def load_tasks():

    """Load tasks from tasks_file and return them as a list."""
    
    try:
        with open(tasks_file, 'r') as f:

            data = json.load(f)

            return [Task.from_dict(item) for item in data]
        
    except (FileNotFoundError, json.JSONDecodeError):

        return []
    
    
def save_tasks(tasks):

    """Save task in tasks_file."""

    with open(tasks_file, 'w') as f:

        json.dump([task.to_dict() for task in tasks], f, indent=4)

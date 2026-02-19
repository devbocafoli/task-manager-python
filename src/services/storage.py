import json

tasks_file = 'data/data.json'

def load_tasks():

    """Load tasks from tasks_file and return them as a list."""
    
    try:
        with open(tasks_file, 'r') as arq:

            tasks_data = json.load(arq)

            return tasks_data
        
    except (FileNotFoundError, json.JSONDecodeError):

        return []
    
    
def save_tasks(tasks):

    """Save task in tasks_file."""

    with open(tasks_file, 'w') as arq:

        json.dump(tasks, arq, indent=4)

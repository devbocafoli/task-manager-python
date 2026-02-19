

class Task:
    def __init__(self, id: int, title: str, completed: bool = False):
        self.id = id
        self.title = title
        self.completed = completed

    def mark_as_completed(self):

        """Mark the task as completed."""

        self.completed = True

    def to_dict(self):

        """Convert the Task object to a dictionary."""

        return{
            'id' : self.id,
            'title' : self.title,
            'completed' : self.completed
        }


    def from_dict(data : dict):

        """Create a Task object from a dictionary."""

        return Task(
            id = data['id'],
            title = data['title'],
            completed = data['completed']
        )

    def __str__(self):

        """Return a task as a string representation."""

        status = '✔' if self.completed else '✘'

        return f' {self.id} - {self.title} - [{status}]'
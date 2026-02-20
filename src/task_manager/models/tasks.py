

class Task:
    def __init__(self, id: int, title: str, completed: bool = False):
        self.id = id
        self.title = title
        self.completed = completed

    def toggle_status(self):

        """Toggle the completion status of the task."""

        self.completed = not self.completed

    def to_dict(self):

        """Convert the Task object to a dictionary."""

        return{
            'id' : self.id,
            'title' : self.title,
            'completed' : self.completed
        }


    @staticmethod
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
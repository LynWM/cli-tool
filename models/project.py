from datetime import datetime

class Project:
    _all = []
    _id_counter = 1

    def __init__(self, title, description, due_date, owner_name):
        self.title = title
        self.description = description
        self.due_date = due_date
        self._owner_name = owner_name

        self.tasks = []
        self.id = Project._id_counter
        Project._id_counter += 1
        Project._all.append(self)

    # Instance Methods
    @property
    def title(self):
        return self._title
    
    @title.setter
    def title(self, value):
        if not value:
            raise ValueError("Project Title cannot be empty. Please try again")
        self._title = value
    
    @property
    def description(self):
        return self._description
    
    @description.setter
    def description(self, value):
        if not value:
            raise ValueError("Project Description cannot be empty. Please try again")
        self._description = value

    @property
    def due_date(self):
        return self._due_date

    @due_date.setter
    def due_date(self, value):
        try:
            datetime.strptime(value, "%Y-%m-%d")
        except ValueError:
            raise ValueError("Due date must be in the YYYY-MM-DD format. Please try again")
        self._due_date = value

    @property
    def owner_name(self):
        return self._owner_name

    @classmethod
    def all(cls):
        return cls._all
    
    #methods used in main.py
    @classmethod
    def find_by_title(cls, title):
        return next((p for p in cls._all if p.title == title), None)

    @classmethod
    def find_by_owner(cls, owner_name):
        return [p for p in cls._all if p.owner_name == owner_name]

    # converting to dict to be saved by JSON => file_io.py
    def to_dict(self):
        return {
            "id": self.id,
            "title": self._title,
            "description": self._description,
            "due_date": self._due_date,
            "owner_name": self._owner_name,
            "tasks": self.tasks
        }

    def __str__(self):
        return (f"Project #{self.id}: {self._title} | "
                f"Owner: {self._owner_name} | "
                f"Due: {self._due_date} | "
                f"Tasks: {len(self.tasks)}")

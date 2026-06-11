class Task:
    _all = []        
    _id_counter = 1  

    def __init__(self, title, project_title, assigned_to=None):
        self._title = title
        self._project_title = project_title
        self._assigned_to = assigned_to
        self._status = "pending"   
        self.id = Task._id_counter
        Task._id_counter += 1
        Task._all.append(self)

    
    # Instance Methods
    @property
    def title(self):
        return self._title

    @title.setter
    def title(self, value):
        if not value:
            raise ValueError("Title cannot be empty. Please try again")
        self._title = value

    @property
    def status(self):
        return self._status

    @status.setter
    def status(self, value):
        allowed = ["pending", "in-progress", "complete"]
        if value not in allowed:
            raise ValueError(f"Status must be one of: {allowed}")
        self._status = value

    @property
    def assigned_to(self):
        return self._assigned_to

    @assigned_to.setter
    def assigned_to(self, value):
        self._assigned_to = value

    @property
    def project_title(self):
        return self._project_title

    @classmethod
    def all(cls):
        return cls._all

    @classmethod
    def find_by_project(cls, project_title):
        return [t for t in cls._all if t.project_title == project_title]

    @classmethod
    def find_by_id(cls, task_id):
        return next((t for t in cls._all if t.id == task_id), None)

    def complete(self):
        self._status = "complete"

    def to_dict(self):
        return {
            "id": self.id,
            "title": self._title,
            "project_title": self._project_title,
            "assigned_to": self._assigned_to,
            "status": self._status
        }

    def __str__(self):
        assigned = self._assigned_to or "Unassigned"
        return (f"Task #{self.id}: {self._title} \n "
                f"Project: {self._project_title} \n "
                f"Assigned to: {assigned} \n "
                f"Status: {self._status}")
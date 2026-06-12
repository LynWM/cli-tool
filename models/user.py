# Parent class - User
class Person:
    def __init__(self, name, email):
        self.name = name
        self.email = email
    
    # Instance  Methods
    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, value):
        if not value:
            raise ValueError("Name cannot be empty. Please enter a name")
        self._name = value

    @property
    def email(self):
        return self._email
    
    @email.setter
    def email(self, value):
        if "@" not in value or "." not in value.split("@")[-1]:
            raise ValueError("Please enter a valid email address")
        self._email = value

    def __str__(self):
        return f"{self._name} ({self._email})"
    

# Child class
class User(Person):
    _all = []

    def __init__(self, name, email):
        super().__init__(name, email)
        
        
        self.projects = []
        User._all.append(self)

    # Class Methods
    @classmethod
    def all(cls):
        return cls._all
    
    @classmethod
    def find_by_name(cls, name):
        return next((u for u in cls._all if u.name == name), None)
    
    # Instance methods
    def to_dict(self):
        return {
            "name": self._name,
            "email": self._email,
            "projects": self.projects
        }
    
    def __str__(self):
        return f"User: {self._name} | Email: {self._email} | Projects: {len(self.projects)}"
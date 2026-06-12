import unittest
from models.user import User, Person
from models.project import Project
from models.task import Task


class TestPerson(unittest.TestCase):

    #Tests for the Person base class.
    def test_person_attributes(self):
        person = Person("Alex", "alex@email.com")
        self.assertEqual(person.name, "Alex")
        self.assertEqual(person.email, "alex@email.com")

    def test_invalid_email(self):
        person = Person("Alex", "alex@email.com")
        with self.assertRaises(ValueError):
            person.email = "notanemail"

    def test_empty_name(self):
        person = Person("Alex", "alex@email.com")
        with self.assertRaises(ValueError):
            person.name = ""


class TestUser(unittest.TestCase):
    
    #Tests for the User class.
    def setUp(self):
        User._all.clear()

    def test_create_user(self):
        user = User("Alex", "alex@email.com")
        self.assertEqual(user.name, "Alex")
        self.assertEqual(user.email, "alex@email.com")

    def test_user_added_to_all(self):
        user = User("Alex", "alex@email.com")
        self.assertIn(user, User.all())

    def test_find_by_name(self):
        User("Alex", "alex@email.com")
        found = User.find_by_name("Alex")
        self.assertIsNotNone(found)
        self.assertEqual(found.name, "Alex")

    def test_find_by_name_not_found(self):
        result = User.find_by_name("Ghost")
        self.assertIsNone(result)

    def test_user_to_dict(self):
        user = User("Alex", "alex@email.com")
        d = user.to_dict()
        self.assertEqual(d["name"], "Alex")
        self.assertEqual(d["email"], "alex@email.com")
        self.assertIn("projects", d)

    def test_user_inherits_person(self):
        user = User("Alex", "alex@email.com")
        self.assertIsInstance(user, Person)


class TestProject(unittest.TestCase):
    
    #Tests for the Project class.
    def setUp(self):
        Project._all.clear()
        Project._id_counter = 1

    def test_create_project(self):
        project = Project("CLI Tool", "A cool tool", "2025-12-01", "Alex")
        self.assertEqual(project.title, "CLI Tool")
        self.assertEqual(project.owner_name, "Alex")

    def test_invalid_due_date(self):
        project = Project("CLI Tool", "A cool tool", "2025-12-01", "Alex")
        with self.assertRaises(ValueError):
            project.due_date = "tomorrow"

    def test_find_by_title(self):
        Project("CLI Tool", "A cool tool", "2025-12-01", "Alex")
        found = Project.find_by_title("CLI Tool")
        self.assertIsNotNone(found)

    def test_find_by_owner(self):
        Project("CLI Tool", "A cool tool", "2025-12-01", "Alex")
        Project("Another", "Another project", "2025-11-01", "Alex")
        results = Project.find_by_owner("Alex")
        self.assertEqual(len(results), 2)

    def test_project_id_increments(self):
        p1 = Project("CLI Tool", "desc", "2025-12-01", "Alex")
        p2 = Project("Web App", "desc", "2025-12-01", "Alex")
        self.assertNotEqual(p1.id, p2.id)

    def test_project_to_dict(self):
        project = Project("CLI Tool", "A cool tool", "2025-12-01", "Alex")
        d = project.to_dict()
        self.assertIn("title", d)
        self.assertIn("owner_name", d)


class TestTask(unittest.TestCase):
    
    #Tests for the Task class.
    def setUp(self):
        Task._all.clear()
        Task._id_counter = 1

    def test_create_task(self):
        task = Task("Implement login", "CLI Tool", "Alex")
        self.assertEqual(task.title, "Implement login")
        self.assertEqual(task.status, "pending")

    def test_default_status(self):
        task = Task("Implement login", "CLI Tool")
        self.assertEqual(task.status, "pending")

    def test_complete_task(self):
        task = Task("Implement login", "CLI Tool")
        task.complete()
        self.assertEqual(task.status, "complete")

    def test_invalid_status(self):
        task = Task("Implement login", "CLI Tool")
        with self.assertRaises(ValueError):
            task.status = "done"

    def test_optional_assigned_to(self):
        task = Task("Implement login", "CLI Tool")
        self.assertIsNone(task.assigned_to)

    def test_find_by_project(self):
        Task("Implement login", "CLI Tool")
        Task("Write tests", "CLI Tool")
        results = Task.find_by_project("CLI Tool")
        self.assertEqual(len(results), 2)

    def test_find_by_id(self):
        task = Task("Implement login", "CLI Tool")
        found = Task.find_by_id(task.id)
        self.assertEqual(found.title, "Implement login")

    def test_task_to_dict(self):
        task = Task("Implement login", "CLI Tool", "Alex")
        d = task.to_dict()
        self.assertIn("title", d)
        self.assertIn("status", d)
        self.assertIn("assigned_to", d)


if __name__ == "__main__":
    unittest.main()



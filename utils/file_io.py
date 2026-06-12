import json
import os

tool_data = "data/data.json"


def load_data():
    if not os.path.exists(tool_data):
        return {"users": [], "projects": [], "tasks": []}
    
    try:
        with open(tool_data, "r") as f:
            return json.load(f)
        
    except (json.JSONDecodeError, ValueError):
        print("There's a problem with the data file. Kindly refresh and try again.")
        return {"users": [], "projects": [], "tasks": []}


def save_data(data):
    try:
        with open(tool_data, "w") as f:
            json.dump(data, f, indent=2)
    except IOError as e:
        print(f"Error saving data: {e}")

# passing classes as parameters instead of imports - avoid circular imports
def load_all(UserClass, ProjectClass, TaskClass):
    
    data = load_data()

    # clearing to avoid duplicates
    UserClass._all.clear()
    ProjectClass._all.clear()
    ProjectClass._id_counter = 1
    TaskClass._all.clear()
    TaskClass._id_counter = 1

    # rebuilding users
    for u in data["users"]:
        user = UserClass(u["name"], u["email"])
        user.projects = u.get("projects", [])

    # rebuilding projects
    for p in data["projects"]:
        project = ProjectClass(
            p["title"],
            p["description"],
            p["due_date"],
            p["owner_name"]
        )
        project.tasks = p.get("tasks", [])
        project.id = p["id"]
        if p["id"] >= ProjectClass._id_counter:
            ProjectClass._id_counter = p["id"] + 1

    # rebuilding tasks
    for t in data["tasks"]:
        task = TaskClass(
            t["title"],
            t["project_title"],
            t.get("assigned_to")
        )
        task._status = t.get("status", "pending")
        task.id = t["id"]
        if t["id"] >= TaskClass._id_counter:
            TaskClass._id_counter = t["id"] + 1


def save_all(UserClass, ProjectClass, TaskClass):
   
    data = {
        "users": [u.to_dict() for u in UserClass.all()],
        "projects": [p.to_dict() for p in ProjectClass.all()],
        "tasks": [t.to_dict() for t in TaskClass.all()]
    }
    save_data(data)
import argparse
from rich.console import Console
from rich.table import Table
from models.user import User
from models.project import Project
from models.task import Task
from utils.file_io import load_all, save_all

console = Console()

# Adding user
def add_user(args):
    load_all(User, Project, Task)
    existing = User.find_by_name(args.name)
    if existing:
        console.print(f"[red]User '{args.name}' already exists.[/red]")
        return
    
    user = User(args.name, args.email)
    save_all(User, Project, Task)
    console.print(f"[green]User '{args.name}' created successfully![/green]")

# Listing users
def list_users(args):
    load_all(User, Project, Task)
    users = User.all()
    if not users:
        console.print("[yellow]No users found.[/yellow]")
        return
    
    # returning a table with users
    table = Table(title="Users", show_lines=True)
    table.add_column("Name", style="cyan")
    table.add_column("Email", style="magenta")
    table.add_column("Projects", style="green")
    for user in users:
        table.add_row(user.name, user.email, str(len(user.projects)))
    console.print(table)

# adding projects
def add_project(args):
    load_all(User, Project, Task)
    user = User.find_by_name(args.user)
    if not user:
        console.print(f"[red]User '{args.user}' not found.[/red]")
        return
    existing = Project.find_by_title(args.title)
    if existing:
        console.print(f"[red]Project '{args.title}' already exists.[/red]")
        return
    project = Project(args.title, args.description, args.due_date, args.user)
    user.projects.append(args.title)
    save_all(User, Project, Task)
    console.print(f"[green] Project '{args.title}' added to '{args.user}'![/green]")

# Listing projects
def list_projects(args):
    load_all(User, Project, Task)
    if args.user:
        projects = Project.find_by_owner(args.user)
        title = f"Projects for {args.user}"
    else:
        projects = Project.all()
        title = "All Projects"
    if not projects:
        console.print("[yellow]No projects found.[/yellow]")
        return
    table = Table(title=title, show_lines=True)
    table.add_column("ID", style="cyan")
    table.add_column("Title", style="magenta")
    table.add_column("Description", style="white")
    table.add_column("Due Date", style="yellow")
    table.add_column("Owner", style="green")
    table.add_column("Tasks", style="blue")
    for project in projects:
        table.add_row(
            str(project.id),
            project.title,
            project.description,
            project.due_date,
            project.owner_name,
            str(len(project.tasks))
        )
    console.print(table)

# adding tasks
def add_task(args):
    load_all(User, Project, Task)
    project = Project.find_by_title(args.project)
    if not project:
        console.print(f"[red]Project '{args.project}' not found.[/red]")
        return
    task = Task(args.title, args.project, args.assigned_to)
    project.tasks.append(args.title)
    save_all(User, Project, Task)
    console.print(f"[green] Task '{args.title}' added to '{args.project}'![/green]")

# listing tasks
def list_tasks(args):
    load_all(User, Project, Task)
    if args.project:
        tasks = Task.find_by_project(args.project)
        title = f"Tasks for {args.project}"
    else:
        tasks = Task.all()
        title = "All Tasks"
    if not tasks:
        console.print("[yellow]No tasks found.[/yellow]")
        return
    table = Table(title=title, show_lines=True)
    table.add_column("ID", style="cyan")
    table.add_column("Title", style="magenta")
    table.add_column("Project", style="white")
    table.add_column("Assigned To", style="yellow")
    table.add_column("Status", style="green")
    for task in tasks:
        table.add_row(
            str(task.id),
            task.title,
            task.project_title,
            task.assigned_to or "Unassigned",
            task.status
        )
    console.print(table)

# marking task as completed/not completed
def complete_task(args):
    load_all(User, Project, Task)
    task = Task.find_by_id(args.id)
    if not task:
        console.print(f"[red]Task with ID {args.id} not found.[/red]")
        return
    task.complete()
    save_all(User, Project, Task)
    console.print(f"[green]Task '{task.title}' marked as complete![/green]")


# argparse and subparsers(subcommands)
def main():
    parser = argparse.ArgumentParser(
        description="CLI Project Management Tool"
    )
    subparsers = parser.add_subparsers(dest="command")
    subparsers.required = True

    # add-user
    p_add_user = subparsers.add_parser("add-user", help="Add a new user")
    p_add_user.add_argument("--name", required=True, help="User's name")
    p_add_user.add_argument("--email", required=True, help="User's email")
    p_add_user.set_defaults(func=add_user)

    # list-users
    p_list_users = subparsers.add_parser("list-users", help="List all users")
    p_list_users.set_defaults(func=list_users)

    # add-project
    p_add_project = subparsers.add_parser("add-project", help="Add a project")
    p_add_project.add_argument("--user", required=True, help="Owner's name")
    p_add_project.add_argument("--title", required=True, help="Project title")
    p_add_project.add_argument("--description", required=True, help="Project description")
    p_add_project.add_argument("--due-date", dest="due_date", required=True, help="Due date YYYY-MM-DD")
    p_add_project.set_defaults(func=add_project)

    # list-projects
    p_list_projects = subparsers.add_parser("list-projects", help="List projects")
    p_list_projects.add_argument("--user", help="Filter by user")
    p_list_projects.set_defaults(func=list_projects)

    # add-task
    p_add_task = subparsers.add_parser("add-task", help="Add a task")
    p_add_task.add_argument("--project", required=True, help="Project title")
    p_add_task.add_argument("--title", required=True, help="Task title")
    p_add_task.add_argument("--assigned-to", dest="assigned_to", help="Assign to a user")
    p_add_task.set_defaults(func=add_task)

    # list-tasks
    p_list_tasks = subparsers.add_parser("list-tasks", help="List tasks")
    p_list_tasks.add_argument("--project", help="Filter by project")
    p_list_tasks.set_defaults(func=list_tasks)

    # complete-task
    p_complete_task = subparsers.add_parser("complete-task", help="Mark task complete")
    p_complete_task.add_argument("--id", required=True, type=int, help="Task ID")
    p_complete_task.set_defaults(func=complete_task)

    args = parser.parse_args()
    args.func(args)


if __name__ == "__main__":
    main()
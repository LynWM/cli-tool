# Python Project Management CLI Tool

This is a simple CLI Tool used to add and manage users and tasks.

## Setup Instructions

### Fork and Clone the Repository

1. Go to the provided GitHub repository link.
2. Fork the repository to your GitHub account.
3. Clone the forked repository to your local machine using:

```bash
git clone <repo-url>
cd cli-tool
```

### Install Python and pip

To be able to use and interact with this project, ensure both Python and pip are installed:

```bash
python --version
pip --version
```

If not, install Python version 3.10+ and pip.
[Python Resource](https://www.python.org/downloads/)

### Project Terminal

Open the project in your preferred IDE(eg VS Code) and in the terminal:

1. Install dependencies
 ```bash
 pipenv install
 ```

2. Activate the virtual environment.
 This will allow you to interact with the CLI tool and run commands.
 ```bash
 pipenv shell
 ```

## Running Commands

### General Help
```bash
 python main.py --help
```
This code gives you a basic rundown on all commands you can use while interacting with this CLI
Tool in the terminal.

General help for a specific command
```bash
 python main.py add-task --help
```

All commands are written **python main.py** 

The terminal will also provide help in how arguments should be arranged and structured when running commands.

### Sample Commands 

1. Adding new user
 ```bash
 python main.py add-user --name "John" --email "johndoe@gmail.com"
 ```
This command adds user **John** and his email **johndoe@gmail.com** to the data.json file

2. Adding a project
 ```bash
 python main.py add-project --user "John" --title "JS Calculator" --description "A simple calculator for basic computations" --due-date "2026-06-24"
 ```
This command adds the project by John and stores it in the data.json file

3. Adding a task
```bash
python main.py add-task --project "JS Calculator" --title "Work on addition" --assigned-to "John"
```

#### Note:
**Arguments, especially the ones that contain multiple words such as description should be enclosed with "" so that it can be treated as one argument**

## Current Features
- Add and list users.
- Add and list projects.
- Add and list tasks under projects.
- Mark tasks as complete

## To be added
- Modifying and Deleting Users.
- Removing or Updating cureent projects and tasks.
- Reassigning projects from one user to another.

## SideNotes
- Incorporated the [Rich Python Library](https://pypi.org/project/rich/) package for formating output in well structured tables and beautiful text.

 
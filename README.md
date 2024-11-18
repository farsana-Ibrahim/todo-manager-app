Todo Management Project

Overview
This project is a Todo Management Application that allows users to manage projects and associated todos with a user-friendly interface. Key features include creating, updating, marking, deleting todos, exporting project details as Markdown files, and authentication functionalities (signup, login, logout).

FEATURES:
1.Authentication
User registration (signup).
User login and logout.

2.Projects
Create a new project.
View a list of all projects.
View detailed information about a specific project.
Update the project title.
Export project details and todos as a Markdown file.

3.Todos
Add, edit, delete, and view todos under a project.
Mark todos as complete or pending.
Track completed todos and pending todos for each project.

4.Responsive UI
User-friendly interface built with Bootstrap for responsiveness and aesthetic design.

INSTALLATION

1.Create a virtual environment and install dependencies:
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
pip install -r requirements.txt

2.Configure the database:
Run migrations:
python manage.py migrate

Create a superuser for admin access:
python manage.py createsuperuser

Start the development server:
python manage.py runserver
Open the application in your browser:

PROJECT STRUCTURE
Key Files and Directories
urls.py: Contains all the routes for the application.
views.py: Handles the business logic for authentication, project, and todo management.
Templates:
registration: For authentication-related pages like login and signup.
projects: Contains HTML files for project and todo management.
Models:
Project: Represents a project.
Todo: Represents a todo item under a project.
Templates
project_list.html: Displays all projects.
project_detail.html: Displays detailed project information and todos.
project_form.html: Form for adding/editing projects and todos.
Technologies Used
Backend: Django (Python)
Frontend: HTML, CSS (Bootstrap)
Database: SQLite (default in Django, configurable for PostgreSQL or MySQL)
Markdown Export: Generates .md files for project summaries.
Usage

Authentication
Sign up for a new account or log in if you already have one.
Logout from the application using the "Logout" button.

Manage Projects
Add new projects using the "Create Project" button.
View details of a project and manage todos.

Manage Todos
Add todos to a project, mark them as complete/pending, edit, or delete them.

Export Project Details
Export project details and todos as a Markdown file using the "Export as Markdown" button.
Example Markdown Export

# Project Title

Summary: 2/5 todos completed.

## Pending
- [ ] Todo 1
- [ ] Todo 2
- [ ] Todo 3

## Completed
- [x] Todo 4
- [x] Todo 5

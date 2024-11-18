import os
from django.shortcuts import render, redirect, get_object_or_404
from django.conf import settings
from .models import Project, Todo
from .forms import ProjectForm, TodoForm
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.contrib.auth import logout
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages


def signup_view(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Account created successfully! Please log in.")
            return redirect("login")  # Redirect to login page
    else:
        form = UserCreationForm()
    return render(request, "registration/signup.html", {"form": form})

# View to list all projects
@login_required
def list_projects(request):
    projects = Project.objects.filter(user=request.user)
    return render(request, 'projects/project_list.html', {'projects': projects})

# View to create a new project
@login_required
def create_project(request):
    if request.method == 'POST':
        form = ProjectForm(request.POST)
        if form.is_valid():
            project = form.save(commit=False)
            project.user = request.user
            project.save()
            return redirect('list_projects')
    else:
        form = ProjectForm()
    return render(request, 'projects/project_form.html', {'form': form})

# View to manage todos within a project
# views.py

@login_required
def project_detail(request, project_id):
    project = get_object_or_404(Project, id=project_id, user=request.user)
    todos = project.todos.all()  # Fetch all todos for the project
    completed_todos = todos.filter(completed=True).count()  # Count completed todos
    total_todos = todos.count()  # Count total todos

    if request.method == 'POST':
        # Handle project title update
        if 'update_project' in request.POST:
            project.title = request.POST['title']
            project.save()
            return redirect('project_detail', project_id=project.id)
        
        # Handle todo creation
        form = TodoForm(request.POST)
        if form.is_valid():
            todo = form.save(commit=False)
            todo.project = project
            todo.save()
            return redirect('project_detail', project_id=project.id)
    else:
        form = TodoForm()

    # Include the summary in the context
    context = {
        'project': project,
        'todos': todos,
        'form': form,
        'completed_todos': completed_todos,
        'total_todos': total_todos,
    }
    return render(request, 'projects/project_detail.html', context)



# Export project summary as Markdown
@login_required
def export_project_markdown(request, project_id):
    project = get_object_or_404(Project, id=project_id, user=request.user)
    pending_todos = project.todos.filter(completed=False)
    completed_todos = project.todos.filter(completed=True)

    # Generate Markdown content
    markdown_content = f"# {project.title}\n\n"
    markdown_content += f"Summary: {completed_todos.count()}/{project.todos.count()} todos completed.\n\n"
    markdown_content += "## Pending\n"
    for todo in pending_todos:
        markdown_content += f"- [ ] {todo.title}\n"
    markdown_content += "\n## Completed\n"
    for todo in completed_todos:
        markdown_content += f"- [x] {todo.title}\n"

    # Save as .md file in MEDIA_ROOT
    file_name = f"{project.title.replace(' ', '_')}.md"
    file_path = os.path.join(settings.MEDIA_ROOT, file_name)
    with open(file_path, "w") as file:
        file.write(markdown_content)

    # Serve the file as a download
    with open(file_path, "r") as file:
        response = HttpResponse(file.read(), content_type="text/markdown")
        response['Content-Disposition'] = f'attachment; filename="{file_name}"'
        return response
    
    
# views.py

@login_required
def update_todo(request, todo_id):
    todo = get_object_or_404(Todo, id=todo_id, project__user=request.user)
    if request.method == 'POST':
        form = TodoForm(request.POST, instance=todo)
        if form.is_valid():
            form.save()
            return redirect('project_detail', project_id=todo.project.id)
    else:
        form = TodoForm(instance=todo)
    
    return render(request, 'projects/project_form.html', {'form': form})

# views.py

@login_required
def delete_todo(request, todo_id):
    todo = get_object_or_404(Todo, id=todo_id, project__user=request.user)
    project_id = todo.project.id
    todo.delete()
    return redirect('project_detail', project_id=project_id)

# views.py

@login_required
def mark_complete(request, todo_id):
    todo = get_object_or_404(Todo, id=todo_id, project__user=request.user)
    todo.completed = True
    todo.save()
    return redirect('project_detail', project_id=todo.project.id)

@login_required
def mark_pending(request, todo_id):
    todo = get_object_or_404(Todo, id=todo_id, project__user=request.user)
    todo.completed = False
    todo.save()
    return redirect('project_detail', project_id=todo.project.id)

def logout_view(request):
    logout(request)
    return redirect('login')  # Redirect to the login page after logout


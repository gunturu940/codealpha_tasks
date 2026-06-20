from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Project, Task, Comment

def register_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('dashboard')
    else:
        form = UserCreationForm()
    return render(request, 'tasks/register.html', {'form': form})

def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('dashboard')
    else:
        form = AuthenticationForm()
    return render(request, 'tasks/login.html', {'form': form})

def logout_view(request):
    logout(request)
    return redirect('login')

@login_required
def dashboard(request):
    projects = Project.objects.filter(members=request.user) | Project.objects.filter(created_by=request.user)
    projects = projects.distinct()
    return render(request, 'tasks/dashboard.html', {'projects': projects})

@login_required
def create_project(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        description = request.POST.get('description')
        project = Project.objects.create(title=title, description=description, created_by=request.user)
        project.members.add(request.user)
        return redirect('project_detail', pk=project.pk)
    return render(request, 'tasks/create_project.html')

@login_required
def project_detail(request, pk):
    project = get_object_or_404(Project, pk=pk)
    todo_tasks = project.tasks.filter(status='todo')
    inprogress_tasks = project.tasks.filter(status='inprogress')
    done_tasks = project.tasks.filter(status='done')
    return render(request, 'tasks/project_detail.html', {
        'project': project,
        'todo_tasks': todo_tasks,
        'inprogress_tasks': inprogress_tasks,
        'done_tasks': done_tasks,
    })

@login_required
def edit_project(request, pk):
    project = get_object_or_404(Project, pk=pk)
    if request.method == 'POST':
        project.title = request.POST.get('title')
        project.description = request.POST.get('description')
        project.save()
        return redirect('project_detail', pk=project.pk)
    return render(request, 'tasks/edit_project.html', {'project': project})

@login_required
def delete_project(request, pk):
    project = get_object_or_404(Project, pk=pk)
    if request.method == 'POST':
        project.delete()
        return redirect('dashboard')
    return render(request, 'tasks/delete_project.html', {'project': project})

@login_required
def create_task(request, pk):
    project = get_object_or_404(Project, pk=pk)
    if request.method == 'POST':
        title = request.POST.get('title')
        description = request.POST.get('description')
        priority = request.POST.get('priority')
        deadline = request.POST.get('deadline')
        assigned_to_id = request.POST.get('assigned_to')
        from django.contrib.auth.models import User
        assigned_to = User.objects.get(pk=assigned_to_id) if assigned_to_id else None
        Task.objects.create(
            project=project, title=title, description=description,
            priority=priority, deadline=deadline or None, assigned_to=assigned_to
        )
        return redirect('project_detail', pk=project.pk)
    members = project.members.all()
    return render(request, 'tasks/create_task.html', {'project': project, 'members': members})

@login_required
def task_detail(request, pk):
    task = get_object_or_404(Task, pk=pk)
    comments = task.comments.all().order_by('created_at')
    if request.method == 'POST':
        content = request.POST.get('content')
        if content:
            Comment.objects.create(task=task, author=request.user, content=content)
        return redirect('task_detail', pk=task.pk)
    return render(request, 'tasks/task_detail.html', {'task': task, 'comments': comments})

@login_required
def edit_task(request, pk):
    task = get_object_or_404(Task, pk=pk)
    if request.method == 'POST':
        task.title = request.POST.get('title')
        task.description = request.POST.get('description')
        task.priority = request.POST.get('priority')
        task.deadline = request.POST.get('deadline') or None
        task.save()
        return redirect('task_detail', pk=task.pk)
    return render(request, 'tasks/edit_task.html', {'task': task})

@login_required
def update_task_status(request, pk):
    task = get_object_or_404(Task, pk=pk)
    if request.method == 'POST':
        task.status = request.POST.get('status')
        task.save()
    return redirect('project_detail', pk=task.project.pk)

from django.shortcuts import render, redirect
from .forms import TaskForm
from .models import Task

# Display all tasks on the home page
def task_list(request):
    tasks = Task.objects.all().order_by("-created_at")
    return render(request, "tasks/task_list.html", {"tasks": tasks})

# Handle adding a new task
def add_task(request):
    if request.method == "POST":
        form = TaskForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect("task_list")
    else:
        form = TaskForm()

    return render(request, "tasks/task_form.html", {"form": form})

# Mark a task as completed
def complete_task(request, task_id):
    task = Task.objects.get(id=task_id)
    task.completed = True
    task.save()

    return redirect("task_list")
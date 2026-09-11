from django.shortcuts import render, redirect
from .forms import TaskForm
from .models import Task


def task_list(request):
    tasks = Task.objects.all().order_by("-created_at")
    return render(request, "tasks/task_list.html", {"tasks": tasks})


def add_task(request):
    if request.method == "POST":
        form = TaskForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect("task_list")
    else:
        form = TaskForm()

    return render(request, "tasks/task_form.html", {"form": form})
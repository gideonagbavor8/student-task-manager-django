# Overview

The Student Task Manager is a Django web application that helps students organize and track their tasks. Users can add tasks with a title and description, view saved tasks, see when each task was created, and mark unfinished tasks as completed.

To run the application locally, make sure Python and Django are installed. Open PowerShell in the project folder and run:

```powershell
python manage.py runserver
```

Then open the following address in a web browser:

```text
http://127.0.0.1:8000/
```

The purpose of this software is to strengthen my skills in developing web applications with Python and Django. The project gave me practical experience with Django models, forms, views, URL routing, templates, user input, and database operations using SQLite.

[Software Demo Video](https://vimeo.com/1226081100)

# Web Pages

The application has two main web pages.

The first page is the Student Task Manager task list. It dynamically retrieves tasks from the SQLite database and displays each task's title, description, completion status, and creation date. For unfinished tasks, the page also provides a Complete Task option.

The second page is the Add New Task page. Users enter a task title and description through a Django form. When the form is submitted, Django validates and saves the task to the SQLite database, then redirects the user back to the task list.

The pages are connected through Django URL routing. Users can move from the task list to the Add New Task page and return to the task list after creating a task.

# Development Environment

I developed this application using:

* Visual Studio Code
* Windows PowerShell
* Python 3.13
* Django 6.0.3
* SQLite
* Git and GitHub

The application was written in Python using the Django web framework. Django's models, forms, views, URL routing, and template system were used to build the application. SQLite was used as the database for storing task information.

# Useful Websites

* [Django Documentation](https://docs.djangoproject.com/)
* [Python Documentation](https://docs.python.org/3/)
* [MDN Web Docs](https://developer.mozilla.org/)

# Future Work

* Add the ability to edit existing tasks.
* Add the ability to delete tasks.
* Add filtering so users can view pending or completed tasks separately.
* Improve the visual design and responsiveness of the application.

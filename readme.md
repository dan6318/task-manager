Task manager

A simple Django-based task manager application with support for task creation, filtering, and scheduled reminders using Celery and Redis. The entire application is containerised using Docker and managed via docker-compose.

Features:

Create, view, and filter tasks

Mark tasks as completed

Track due dates and priority levels

Automatic polling every minute to send reminder notifications for tasks due in 2 hours, 30 minutes, or overdue

Uses Redis as the message broker and Celery for background task execution

Requirements

Docker (Docker desktop can be installed from https://www.docker.com/products/docker-desktop/)
Version of docker used for development was 4.39.0
Ensure the machine has been restarted for CLI changes to take effect.

All other dependencies (Python, Redis, Celery etc) are handled within the containers pulling from requirements.txt

Setup

Through the command line, navigate to this repo, and cd into the directory "backend/". From here, run the following commands in order:

docker-compose build
docker-compose up
docker-compose exec web python manage.py migrate
docker-compose exec web python manage.py createsuperuser

With the final command, you will be asked to define a username and password.
The email address can be left blank.

This should set up the task-manager container, and this will contain the following services:

redis-1
web-1
beat-1
celery-1

How to use:

First, you need to sign into the superuser account created earlier. This can be done by going to http://127.0.0.1:8000/admin/
After that, the full application can be accessed at http://127.0.0.1:8000/tasks/
Click "Create new task" to create a task, which will serve a form to fill out.
After a task is created, it can be marked as complete or deleted.
Tasks can also be marked as incomplete.
There are 4 buttons at the top to determine filtering, including:
All,
Incomplete,
Complete,
Overdue.
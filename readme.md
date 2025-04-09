# Task Manager

A simple Django-based task manager application with support for task creation, filtering, and scheduled reminders using Celery and Redis. The entire application is containerised using Docker and managed via docker-compose.

## Features

- Create, view, and filter tasks  
- Mark tasks as completed  
- Track due dates and priority levels  
- Automatic polling every minute to send reminder notifications for tasks due in 2 hours, 30 minutes, or overdue  
- Uses Redis as the message broker and Celery for background task execution  

## Requirements

- Docker (Docker Desktop can be installed from https://www.docker.com/products/docker-desktop/)  
- Version of Docker used for development was **4.39.0**  
- Ensure the machine has been restarted for CLI changes to take effect.

All other dependencies (Python, Redis, Celery etc) are handled within the containers pulling from `requirements.txt`.

## Setup

From the command line, navigate to this repo and `cd` into the `backend/` directory. Then, run the following commands in order:

```bash
docker-compose build
docker-compose up
docker-compose exec web python manage.py migrate
docker-compose exec web python manage.py createsuperuser
```

With the final command, you will be asked to define a username and password.  
The email address can be left blank.

This will bring up the task manager container, which includes the following services:

- `redis-1`
- `web-1`
- `beat-1`
- `celery-1`

## How to use

1. Sign into the superuser account created earlier by visiting:  
   http://127.0.0.1:8000/admin/

2. Access the full application at:  
   http://127.0.0.1:8000/tasks/

3. Click **Create new task** to open a form for adding a new task.

4. Once a task is created, it can be:
   - Marked as complete
   - Marked as incomplete
   - Deleted

5. Filter views are available via buttons at the top:
   - All
   - Incomplete
   - Complete
   - Overdue

from celery import shared_task
from django.utils import timezone
from django.db.models import Q
import datetime
from .models import Task

@shared_task
def send_task_reminder(task_uuid, deadline):
    if deadline.get("value"):
        print(f"Reminder: Task {task_uuid} is due in {deadline.get('value')} {deadline.get('scale')}")
    else:
        print(f"Reminder: Task {task_uuid} is due now!")

@shared_task
def check_upcoming_tasks():
    print("Checking upcoming tasks")
    now = timezone.localtime()
    now_utc = now.astimezone(datetime.timezone.utc)
    task_list = Task.objects.filter(
        completed=False, 
        due_date__lte=now_utc+datetime.timedelta(hours=2), 
        due_date__gt=now_utc+datetime.timedelta(minutes=30), 
        notification_tracking__2h=False
        )
    for task in task_list:
        send_task_reminder.delay(task.uuid, {"value": 2, "scale": "hours"})
        task.notification_tracking["2h"] = True
        task.save(update_fields=["notification_tracking"])
    task_list = Task.objects.filter(
        completed=False, 
        due_date__lte=now_utc+datetime.timedelta(minutes=30), 
        due_date__gt=now_utc, 
        notification_tracking__30m=False
        )
    for task in task_list:
        send_task_reminder.delay(task.uuid, {"value": 30, "scale": "minutes"})
        task.notification_tracking["30m"] = True
        task.save(update_fields=["notification_tracking"])
    task_list = Task.objects.filter(
        completed=False, 
        due_date__lte=now_utc,  
        notification_tracking__0m=False
        ) 
    for task in task_list:
        send_task_reminder.delay(task.uuid, {})
        task.notification_tracking["0m"] = True
        task.save(update_fields=["notification_tracking"])


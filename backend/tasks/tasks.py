from celery import shared_task
import logging

@shared_task
def send_task_reminder(task_uuid):
    logging.info(f"Reminder: Task {task_uuid} is due soon!")
    return f"Reminder sent for task {task_uuid}"

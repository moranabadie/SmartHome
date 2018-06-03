from celery.schedules import crontab
from celery.task.base import periodic_task

from Threads.WaikUp import waik_up_process


@periodic_task(run_every=(crontab(minute='*/1')), name="some_task", ignore_result=True)
def some_task():
    # do something
    waik_up_process()
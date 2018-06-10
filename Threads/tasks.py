import datetime

from celery.schedules import crontab
from celery.task.base import periodic_task

from Threads.WaikUp import waik_up_process
from ViewManager.models import Last


@periodic_task(run_every=(crontab(minute='*/1')), name="some_task", ignore_result=True)
def some_task():
    # do something
    print("Check for date")
    n = Last.objects.first()
    if n == None:
        n = Last()
        n.save()
    n.date = datetime.datetime.now()
    n.save()
    waik_up_process()
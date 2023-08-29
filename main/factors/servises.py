import json
from datetime import timedelta

from django.utils.datetime_safe import datetime
from django_celery_beat.models import IntervalSchedule, PeriodicTask


def set_schedule(*args, **kwargs):
    """переодичность"""
    schedule, create = IntervalSchedule.objects.get_or_create(
        every=10,
        period=IntervalSchedule.SECONDS
    )
    """информация"""
    PeriodicTask.objects.create(
        interval=schedule,
        name="Import contacts",
        task="proj.tasks.import_contacts",
        args=json.dumps(["arg1", "arg2"]),
        kwargs=json.dumps({
            "be_careful": True,
        }),
        expires=datetime.utcnow() + timedelta(seconds=30)
    )

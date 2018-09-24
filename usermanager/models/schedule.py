from django.db import models
from django.core.exceptions import ValidationError
from django.conf import settings
from django.utils import timezone

class ScheduleManager(models.Model):
    pass
    
class Schedule(models.Model):
    DAY_CHOICES = (
        (0, 'Monday'),
        (1, 'Tuesday'),
        (2, 'Wednesday'),
        (3, 'Thursday'),
        (4, 'Friday')
    )
    day_of_week = models.SmallIntegerField(choices=DAY_CHOICES)
    time_start = models.TimeField()
    time_end = models.TimeField()

    objects = ScheduleManager()

    def __str__(self):
        return super().__str__()
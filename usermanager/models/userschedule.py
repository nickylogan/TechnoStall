from django.db import models
from django.core.exceptions import ValidationError
from django.conf import settings
from django.utils import timezone
from . import Schedule

class UserScheduleManager(models.Model):
    pass
    
class UserSchedule(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    schedule = models.ForeignKey(Schedule, on_delete=models.CASCADE)

    objects = UserScheduleManager()

    def __str__(self):
        return super().__str__()
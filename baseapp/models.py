from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

class TSUserManager(models.Manager):
  pass
  
class TSUser(models.Model):
  INFORMATICS = 'TIF'
  INFORMATION_SYSTEMS = 'SI'
  MAJOR_CHOICES = (
    (INFORMATICS, 'Informatics'),
    (INFORMATION_SYSTEMS, 'Information Systems')
  )

  STALLKEEPER = 'SL'
  STALLADMIN = 'SA'
  ROLE_CHOICES = (
    (STALLKEEPER, 'Stallkeeper'),
    (STALLADMIN, 'Stall Admin')
  )

  user = models.OneToOneField(User, on_delete=models.CASCADE)
  major = models.CharField(max_length=3, choices=MAJOR_CHOICES)
  active = models.BooleanField(default=True)
  role = models.CharField(max_length=2, choices=ROLE_CHOICES)

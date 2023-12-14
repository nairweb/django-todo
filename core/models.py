from django.db import models
from django.contrib.auth.models import User
class todo(models.Model):
    task=models.CharField(max_length=50)


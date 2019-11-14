from django.db import models
from django.contrib.auth.models import  User
# Create your models here.

class PersonDetails(models.Model):
    name = models.CharField(max_length=20)
    age = models.PositiveIntegerField()
    auth_link = models.ForeignKey(User)

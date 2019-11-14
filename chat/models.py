from django.db import models

# Create your models here.
from Person.models import PersonDetails


class ChatInstance(models.Model):
    person1 = models.ForeignKey(PersonDetails)
    person2 = models.ForeignKey(PersonDetails)
    created_at = models.DateTimeField(auto_now_add=True)

class ChatMessage(models.Model):
    instance = models.ForeignKey(ChatInstance,on_delete=models.PROTECT,)
    sender = models.ForeignKey
    message = models.TextField()
    timestamp = models.DateTimeField(auto_now=True)

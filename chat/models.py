from django.db import models

# Create your models here.
from Person.models import PersonDetails


class ChatInstance(models.Model):
    person1 = models.ForeignKey(PersonDetails, on_delete=models.PROTECT, related_name='person1')
    person2 = models.ForeignKey(PersonDetails, on_delete=models.PROTECT, related_name='person2')
    created_at = models.DateTimeField(auto_now_add=True)


class ChatMessage(models.Model):
    instance = models.ForeignKey(ChatInstance, on_delete=models.CASCADE, )
    sender = models.ForeignKey(PersonDetails, on_delete=models.PROTECT)
    message = models.TextField()
    timestamp = models.DateTimeField(auto_now=True)

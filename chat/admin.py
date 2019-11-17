from django.contrib import admin

# Register your models here.
from chat.models import ChatInstance, ChatMessage

admin.site.register(ChatInstance)
admin.site.register(ChatMessage)

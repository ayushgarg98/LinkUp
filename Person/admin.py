from django.contrib import admin

# Register your models here.
from Person.models import PersonDetails

admin.site.register(PersonDetails)
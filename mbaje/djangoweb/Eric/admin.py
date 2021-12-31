from django.contrib import admin

# Register your models here.
from .models import Sender
from .models import Message

admin.site.register(Sender)
admin.site.register(Message)
from django.contrib import admin

# Register your models here.

# Make model editable by admin website
from .models import Question
admin.site.register(Question)

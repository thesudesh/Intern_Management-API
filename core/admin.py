from django.contrib import admin
from .models import UserProfile, Task, Attendance

admin.site.register(UserProfile)
admin.site.register(Task)
admin.site.register(Attendance)

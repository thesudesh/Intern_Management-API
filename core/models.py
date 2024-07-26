from django.contrib.auth.models import AbstractUser, Group, Permission
from django.db import models

class UserProfile(AbstractUser):
    ROLE_CHOICES = [
        ('Supervisor', 'Supervisor'),
        ('Intern', 'Intern'),
    ]
    role = models.CharField(max_length=20, choices=ROLE_CHOICES)
    
    groups = models.ManyToManyField(
        Group,
        related_name='user_profiles',  # Add related_name to avoid conflict
        blank=True,
    )
    user_permissions = models.ManyToManyField(
        Permission,
        related_name='user_profiles',  # Add related_name to avoid conflict
        blank=True,
    )

class Task(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    assigned_to = models.ForeignKey(UserProfile, related_name='tasks', on_delete=models.CASCADE)
    completed = models.BooleanField(default=False)

class Attendance(models.Model):
    user = models.ForeignKey(UserProfile, related_name='attendances', on_delete=models.CASCADE)
    date = models.DateField(auto_now_add=True)
    check_in_time = models.TimeField(auto_now_add=True)
    check_out_time = models.TimeField(null=True, blank=True)

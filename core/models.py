from django.contrib.auth.models import AbstractUser, Group, Permission
from django.db import models
from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.translation import gettext_lazy as _
from .constant import ROLE_CHOICES, INTERN
from .managers import CustomUserManager
from django.contrib.auth.validators import UnicodeUsernameValidator


# class UserProfile(AbstractUser):
#     ROLE_CHOICES = [
#         ('Supervisor', 'Supervisor'),
#         ('Intern', 'Intern'),
#     ]
#     role = models.CharField(max_length=20, choices=ROLE_CHOICES)
    
#     groups = models.ManyToManyField(
#         Group,
#         related_name='user_profiles',  
#         blank=True,
#     )
#     user_permissions = models.ManyToManyField(
#         Permission,
#         related_name='user_profiles', 
#         blank=True,
#     )




class UserProfile(AbstractUser):
    username_validator = UnicodeUsernameValidator()

    username = models.CharField(
        _("username"),
        max_length=150,
        unique=True,
        help_text=_(
            "Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only."
        ),
        validators=[username_validator],
        error_messages={
            "unique": _("A user with that username already exists."),
        },
    )
    email = models.EmailField(_("email address"), unique=True)
    role = models.CharField(max_length=20, choices=ROLE_CHOICES, default = INTERN)
    
 
    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["username"]

    objects = CustomUserManager()

    def __str__(self):
        return self.email

class Task(models.Model):
    title = models.CharField(max_length=255, blank = False, null=False )
    description = models.TextField()
    assigned_to = models.ForeignKey(UserProfile, related_name='tasks', on_delete=models.CASCADE)
    completed = models.BooleanField(default=False)

class Attendance(models.Model):
    user = models.ForeignKey(UserProfile, related_name='attendances', on_delete=models.CASCADE)
    check_in_time = models.DateTimeField(auto_now_add=True)
    check_out_time = models.DateTimeField(null=True, blank=True)


from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

#abstract user model
class User(AbstractUser):
    roles = [
        ('1', 'Admin'),
        ('2', 'User'),
        ('3', 'Manager'),
    ]

    email = models.EmailField(unique=True, null=True)
    phone_number = models.CharField(max_length=10, null=True, blank=True)
    role = models.CharField(max_length=50, choices=roles, default=2)

    #email 
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    groups = models.ManyToManyField(
        'auth.Group',
        verbose_name='groups',
        blank=True,
        help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.',
        related_name='customuser_set',  # Use a custom related name for the related set of groups
        related_query_name='customuser',  # Use a custom related name for the related query)
    )

    user_permissions = models.ManyToManyField(
        'auth.Permission',
        verbose_name='user permissions',
        blank=True,
        help_text='Specific permissions for this user.',
        related_name='customuser_set',  # Use a custom related name for the related set of permissions
        related_query_name='customuser',  # Use a custom related name for the related query
    )

    def __str__(self):
        return self.email
    
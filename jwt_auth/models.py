from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    email = models.CharField(max_length=50, unique=True)
    username = models.CharField(max_length=50, blank=True, unique=True) #

    # add a str/repr here
    def __str__(self):
        return f'{self.email}'

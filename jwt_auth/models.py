from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    email = models.CharField(max_length=50, unique=True)
    username = models.CharField(max_length=50, blank=True, unique=True) #

    # see what happens if you uncomment the line below and try to change the USERNAME_FIELD that way,
    # instead of having to inherit from AbstractBaseUser
    # read the bear notes on how migrations work for users (start from ' Day 3 - user authentication (Thursday)')

    # USERNAME_FIELD = 'email'

    # add a str/repr here
    def __str__(self):
        return f'{self.email}'

# read (in particular) the section on 'specifying a custom user model', ALSO READ substituting a custom user model
# https://docs.djangoproject.com/en/4.0/topics/auth/customizing/

# read the bear notes on how migrations work for users

# see the other models file too
"""
class MyUser(AbstractBaseUser):
    identifier = models.CharField(max_length=40, unique=True)
    ...
    USERNAME_FIELD = 'identifier'
"""

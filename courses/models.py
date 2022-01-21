from django.db import models

class Course(models.Model):
    '''Course Model'''
    # these fields are examples and can be removed
    # name = models.CharField(max_length=30, unique=True)
    # number = models.PositiveIntegerField(unique=True)
    # is_starter = models.BooleanField(default=False)
    # generation = models.PositiveIntegerField()
    # pokedex_entry =  models.TextField(max_length=300)
    # image = models.CharField(max_length=300)

    name = models.CharField(max_length=100, unique=True)
    length = models.PositiveIntegerField()
    # see the relationships recording for how to make relationships between models
    # prerequisite
    # review =
    # syllabus =

    def __str__(self):
        return f'{self.name}'

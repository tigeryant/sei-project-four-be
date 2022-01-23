from django.db import models

class Course(models.Model):
    '''Course Model'''
    # these fields are examples and can be removed
    # name = models.CharField(max_length=30, unique=True)
    # number = models.PositiveIntegerField(unique=True)
    # is_starter = models.BooleanField(default=False)
    # generation = models.PositiveIntegerField()
    # pokedex_entry =  models.TextField(max_length=300)

    name = models.CharField(max_length=100, unique=True)
    length = models.PositiveIntegerField()
    # NEW FIELDS
    # prerequisite - FK that links to itself (many to many)
    # reviews - FK, one to many that links to the review
    # syllabus - FK, one to many that links to the weekly syllabus, maybe this should be on the WeeklySyllabus model

    # ADD AN IMAGE FIELD
    # ADD AN INSTRUCTOR FIELD
    image = models.CharField(max_length=300)
    instructor = models.CharField(max_length=100)

    def __str__(self):
        return f'{self.name}'

class Review(models.Model):
    ''' Review Model '''
    content = models.TextField(max_length=300)
    rating = models.PositiveIntegerField()
    # created_at = models.DateTimeField(auto_now_add=True)
    course = models.ForeignKey(
        Course,
        related_name='reviews',
        on_delete=models.CASCADE
    )
    owner = models.ForeignKey(
        'jwt_auth.User',
        related_name='reviews_posted',
        on_delete=models.CASCADE
    )

    def __str__(self):
        return f'Review {self.id} of Course {self.course}'

## new models:

# WEEKLYSYLLABUS
# syllabus id
# content

# SKILL GAINED
# skill id


## USER (this will be in jwt_auth, not here)
# User id
# email
# password

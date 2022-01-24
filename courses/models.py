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
    image = models.CharField(max_length=300)
    length = models.PositiveIntegerField()
    overview = models.TextField(max_length=300)
    prerequisites = models.ManyToManyField('self')
    instructor_name = models.CharField(max_length=100)
    instructor_image = models.CharField(max_length=300)
    instructor_bio = models.TextField(max_length=300)

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

class WeeklySyllabus(models.Model):
    ''' Weekly Syllabus Model'''
    content=models.TextField(max_length=300)
    description = models.TextField(max_length=300)
    week = models.PositiveIntegerField()
    course = models.ForeignKey(
        Course,
        related_name='weekly_syllabuses',
        on_delete=models.CASCADE
    )

    def __str__(self):
        return f'Syllabus for week {self.week} of course {self.course}'

class Skill(models.Model):
    ''' Skill Model '''

    name = models.CharField(max_length=100)
    course = models.ManyToManyField(
        Course,
        related_name='skills'
    )

    def __str__(self):
        return f'Skill: {self.name}'


    # course = models.ForeignKey(
    #     Course,
    #     related_name='skills',
    #     on_delete=models.DO_NOTHING # test this. if it doesn't work
    #     # on_delete=models.CASCADE
    # )


## USER (this will be in jwt_auth, not here)
# User id
# email
# password

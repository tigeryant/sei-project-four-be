from django.contrib import admin
from .models import Course, Review, WeeklySyllabus, Skill

admin.site.register(Course)
admin.site.register(Review)
admin.site.register(WeeklySyllabus)
admin.site.register(Skill)

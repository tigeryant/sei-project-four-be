from rest_framework import serializers
from .models import Course

class CourseSerializer(serializers.ModelSerializer):
    ''' Serilaizer for outgoing course response '''

    class Meta:
        model = Course
        fields = '__all__'
from rest_framework import serializers
from .models import Course, Review

class ReviewSerializer(serializers.ModelSerializer):
    ''' Serializer for Reviews'''

    class Meta:
        model = Review
        fields = '__all__'

class CourseSerializer(serializers.ModelSerializer):
    ''' Serilaizer for outgoing course response '''
    reviews = ReviewSerializer(many=True, read_only=True)

    class Meta:
        model = Course
        fields = '__all__'
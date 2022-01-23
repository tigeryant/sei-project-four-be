from rest_framework import serializers
from django.contrib.auth import get_user_model

from .models import Course, Review
User = get_user_model()

class NestedUserSerializer(serializers.ModelSerializer):
    ''' Serializer for users '''
    class Meta:
        model = User
        fields = ('id', 'username', 'email') # change this to just id and email later on

class ReviewSerializer(serializers.ModelSerializer):
    ''' Serializer for reviews '''

    class Meta:
        model = Review
        fields = '__all__'

class NestedReviewSerializer(serializers.ModelSerializer):
    ''' Serializer for nested reviews '''
    owner = NestedUserSerializer()

    class Meta:
        model = Review
        fields = '__all__'

class CourseSerializer(serializers.ModelSerializer):
    ''' Serilaizer for outgoing course response '''
    reviews = ReviewSerializer(many=True, read_only=True)

    class Meta:
        model = Course
        fields = '__all__'
from rest_framework import serializers
from django.contrib.auth import get_user_model

from .models import Course, Review, WeeklySyllabus, Skill
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
        fields = '__all__' # returning the course is unnecessary

class NestedReviewSerializer(serializers.ModelSerializer):
    ''' Serializer for nested reviews '''
    owner = NestedUserSerializer()

    class Meta:
        model = Review
        fields = '__all__'

class WeeklySyllabusSerializer(serializers.ModelSerializer):
    ''' Serializer for weekly syllabuses'''

    class Meta:
        model = WeeklySyllabus
        # fields = '__all__'
        # this was '__all__' before, change back if needed
        fields = ('week', 'content', 'description')

# add a skill serializer here


class SkillSerializer(serializers.ModelSerializer):
    ''' Serializer for skills'''

    class Meta:
        model = Skill
        fields = '__all__'


class CourseSerializer(serializers.ModelSerializer):
    ''' Serilaizer for outgoing course response '''
    reviews = ReviewSerializer(many=True, read_only=True)
    weekly_syllabuses = WeeklySyllabusSerializer(many=True, read_only=True)
    skills = SkillSerializer(many=True, read_only=True)

    class Meta:
        model = Course
        fields = '__all__'
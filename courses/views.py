from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from .models import Course
from .serializers import CourseSerializer

class CourseListView(APIView):

    def get(self, _request):
        courses = Course.objects.all() # take note of this error
        serialized_course = CourseSerializer(courses, many=True)
        return Response(serialized_course.data, status=status.HTTP_200_OK)

class CourseDetailView(APIView):

    def get(self, _request, pk):
        course = Course.objects.get(pk=pk)
        serialized_course = CourseSerializer(course)
        return Response(serialized_course.data, status=status.HTTP_200_OK)
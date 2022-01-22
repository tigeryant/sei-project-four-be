# from rest_framework.views import APIView
# from rest_framework.response import Response
# from rest_framework import status

# from .models import Course
# from .serializers import CourseSerializer

# class CourseListView(APIView):

#     def get(self, _request):
#         courses = Course.objects.all()
#         serialized_course = CourseSerializer(courses, many=True)
#         return Response(serialized_course.data, status=status.HTTP_200_OK)

# class CourseDetailView(APIView):

#     def get(self, _request, pk):
#         course = Course.objects.get(pk=pk)
#         serialized_course = CourseSerializer(course)
#         return Response(serialized_course.data, status=status.HTTP_200_OK)

########################

# from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView

# from .models import Course
# from .serializers import CourseSerializer

# class CourseListView(ListCreateAPIView):
#     queryset = Course.objects.all()
#     serializer_class = CourseSerializer

# class CourseDetailView(RetrieveUpdateDestroyAPIView):
#     queryset = Course.objects.all()
#     serializer_class = CourseSerializer

###########################

from rest_framework.generics import (
    ListCreateAPIView,
    RetrieveUpdateDestroyAPIView,
    CreateAPIView,
    DestroyAPIView,
)
from rest_framework.permissions import IsAuthenticatedOrReadOnly

from .models import Course, Review
from .serializers import CourseSerializer, ReviewSerializer

class CourseListView(ListCreateAPIView):
    ''' View for /course endpoint GET/POST '''

    queryset = Course.objects.all()
    serializer_class = CourseSerializer
    permission_classes = (IsAuthenticatedOrReadOnly, )

class CourseDetailView(RetrieveUpdateDestroyAPIView):
    ''' View for /course/id endpoint GET/PUT/PATCH/DELETE'''

    queryset = Course.objects.all()
    serializer_class = CourseSerializer
    permission_classes = (IsAuthenticatedOrReadOnly, )

class ReviewListView(CreateAPIView):
    ''' View for /course/id/reviews POST'''

    queryset = Review.objects.all()
    serializer_class = ReviewSerializer
    permission_classes = (IsAuthenticatedOrReadOnly, )

class ReviewDetailView(DestroyAPIView):
    ''' View for /course/id/reviews/reviewId DELETE'''

    queryset = Review.objects.all()
    serializer_class = ReviewSerializer
    permission_classes = (IsAuthenticatedOrReadOnly, )
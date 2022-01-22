from django.urls import path
from .views import (
    CourseListView,
    CourseDetailView,
    ReviewListView,
    ReviewDetailView
)

urlpatterns = [
    path('', CourseListView.as_view()),
    path('<int:pk>/', CourseDetailView.as_view()),
    path('<int:pk>/reviews/', ReviewListView.as_view()),
    path('<int:course_pk>/reviews/<int:pk>/', ReviewDetailView.as_view())
]
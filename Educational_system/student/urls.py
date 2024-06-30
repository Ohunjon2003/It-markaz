from django.urls import path
from .views import (StudentDashboardView,StudentGroupView,StudentLessonView,HomeworkView,HomeDetailView)



app_name = 'student'

urlpatterns = [
    path('dashboard/',StudentDashboardView.as_view(),name='dashboard'),
    path('gruhlarim/',StudentGroupView.as_view(),name='gruhlarim'),
    path('lessons/<int:group_id>/',StudentLessonView.as_view(),name='lessons'),
    path('homework/<int:lesson_id>/',HomeworkView.as_view(),name='homework'),
    path('homework-detail/<int:lesson_id>/',HomeDetailView.as_view(),name='homework_detail'),
]
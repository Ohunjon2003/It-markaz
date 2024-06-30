from django.urls import path
from .views import (TeacherDashboardView,TeacherGroupView,TeacherGroupLessonView,TeacherHomeworksView,
                    TeacherStudentsView,TeacherCreateLesson)


app_name = 'teachers'

urlpatterns = [
    path('dashboard/',TeacherDashboardView.as_view(),name='dashboard'),
    path('gruhlarim/',TeacherGroupView.as_view(),name='gruhlarim'),
    path('gruh/<int:group_id>/',TeacherGroupLessonView.as_view(),name='gruh'),
    path('homework/<int:group_id>/',TeacherHomeworksView.as_view(),name='homework'),
    path('student/<int:group_id>/',TeacherStudentsView.as_view(),name='student'),
    path('create_lesson/<int:group_id>/',TeacherCreateLesson.as_view(),name='create_lesson'),
]
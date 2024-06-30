from django.urls import path
from .views import (LoginView,RegisterView,ProfileView,EditProfileView,LogoutView,GroupsView,StudentsListView,
                    EditStudents,DeleteStudentView,StudentByGroupView,ResetPasswordView)


app_name = 'system'

urlpatterns = [

    path('login/',LoginView.as_view(),name='login'),
    path('logout/',LogoutView.as_view(),name='logout'),
    path('register/',RegisterView.as_view(),name='register'),
    path('profile/',ProfileView.as_view(),name='profile'),
    path('edit-profile/',EditProfileView.as_view(),name='edit_profile'),
    path('groups/',GroupsView.as_view(),name='groups'),
    path('students/',StudentsListView.as_view(),name='students'),
    path('student-by-group/<int:id>/',StudentByGroupView.as_view(),name='student_by_group'),
    path('edit-student/<int:id>/',EditStudents.as_view(),name='edit_student'),
    path('delete-student/<int:id>/',DeleteStudentView.as_view(),name='delete_student'),
    path('reset-password/',ResetPasswordView.as_view(),name='reset_password'),

]
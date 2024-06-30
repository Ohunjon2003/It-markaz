from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse

from system.permissions import TeacherRequiredMixin
# Create your views here.
from django.views import View
from system.models import Teacher,Group
from student.models import Lesson
from .forms import CreateLessonForm
class TeacherDashboardView(TeacherRequiredMixin,View):
    def get(self,request):
        return render(request,'student/dashboard.html')

class TeacherGroupView(TeacherRequiredMixin,View):
    def get(self,request):
        teacher = get_object_or_404(Teacher,user=request.user)
        groups = teacher.groups.all()
        return render(request,'teachers/gruhlarim.html',{'groups':groups})


class TeacherGroupLessonView(TeacherRequiredMixin,View):
    def get(self,request,group_id):
        group = get_object_or_404(Group,id=group_id)
        lessons = group.lessons.all()
        return render(request,'teachers/gruh.html',{'group':group,'lessons':lessons})



class TeacherHomeworksView(TeacherRequiredMixin,View):
    def get(self,request,group_id):
        group = get_object_or_404(Group,id=group_id)
        lessons = group.homeworks.all()
        return render(request,'teachers/gruh.html',{'group':group,'lessons':lessons})


class TeacherStudentsView(TeacherRequiredMixin,View):
    def get(self,request,group_id):
        group = get_object_or_404(Group,id=group_id)
        students = group.students.all()
        return render(request,'teachers/student.html',{'group':group,'students':students})


class TeacherCreateLesson(TeacherRequiredMixin,View):
    def get(self,request,group_id):
        form = CreateLessonForm()
        return render(request,'teachers/create_lesson.html',{'form':form})

    def post(self,request,group_id):
        group = get_object_or_404(Group,id=group_id)
        form = CreateLessonForm(request.POST)
        if form.is_valid():
            lesson = Lesson()
            lesson.group = group
            lesson.title = form.cleaned_data['title']
            lesson.save()
            url = reverse('teachers:gruh',args=[group_id])
            return redirect(url)
        form = CreateLessonForm()
        return render(request,'teachers/create_lesson.html',{'form':form})

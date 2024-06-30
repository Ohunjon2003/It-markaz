from django.shortcuts import render, get_object_or_404, redirect
from system.permissions import StudentRequiredMixin
from django.views import View
from system.models import Student,Group
from .models import Lesson,Homework
from .forms import HomeworkForm
class StudentDashboardView(StudentRequiredMixin,View):
    def get(self,request):
        return render(request,'student/dashboard.html')

class StudentGroupView(StudentRequiredMixin,View):
    def get(self,request):
        student = Student.objects.get(user=request.user)
        return render(request,'student/guruhlarim.html',{'student':student})


class StudentLessonView(StudentRequiredMixin,View):
    def get(self,request,group_id):
        group = get_object_or_404(Group,id=group_id)
        lessons = group.lessons.all()
        return render(request,'student/lessons.html',{'lessons':lessons})



class HomeworkView(StudentRequiredMixin,View):
    def get(self,request,lesson_id):
        form = HomeworkForm()
        return render(request,'student/homework.html',{'form':form})

    def post(self,request,lesson_id):
        lesson = get_object_or_404(Lesson,id=lesson_id)
        student = get_object_or_404(Student,user=request.user)

        form = HomeworkForm(request.POST,request.FILES)


        if form.is_valid():
            homework = Homework()

            homework.lesson = lesson
            homework.student = student
            homework.description = form.cleaned_data['description']
            homework.homework_file = form.cleaned_data['homework_file']
            homework.save()


            lesson.homework_status = True
            lesson.save()
            return redirect('student:dashboard')



class HomeDetailView(StudentRequiredMixin,View):
    def get(self,request,lesson_id):
        student = get_object_or_404(Student,user=request.user)
        lesson = get_object_or_404(Lesson,id=lesson_id)
        homework = Homework.objects.filter(lesson=lesson,student=student).first()
        return render(request,'student/homework_detail.html',{'homework':homework})



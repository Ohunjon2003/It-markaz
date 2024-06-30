from django.contrib.auth import login, authenticate, logout
from django.shortcuts import render, redirect, get_object_or_404
from django.views import View
from django.contrib.auth.mixins import LoginRequiredMixin
from .permissions import AdminRequiredMixin
from .forms import LoginForm, RegisterForm, ProfileEditForm, StudentEditForm,ResetPasswordForm
from .models import User, Student, Group,Teacher
from django.db.models import Q

class LoginView(View):
    def get(self, request):
        form = LoginForm()
        return render(request, 'system/login.html', context={'form': form})

    def post(self, request):
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('system:profile')
        return render(request, 'system/login.html', context={'form': form})

class RegisterView(AdminRequiredMixin, View):
    def get(self, request):
        form = RegisterForm()
        return render(request, 'system/register.html', context={'form': form})

    def post(self, request):
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            if user.user_role == 'student':
                new_student = Student(user=user)
                new_student.save()
            elif user.user_role == 'teacher':
                new_teacher = Teacher(user=user)
                new_teacher.save()
            return redirect('/')
        return render(request, 'system/register.html', context={'form': form})

class ProfileView(LoginRequiredMixin, View):
    login_url = '/login/'

    def get(self, request):
        return render(request, 'system/profile.html', context={'user': request.user})

class EditProfileView(LoginRequiredMixin, View):
    def get(self, request):
        form = ProfileEditForm(instance=request.user)
        return render(request, 'system/edit_profile.html', {'form': form})

    def post(self, request):
        form = ProfileEditForm(request.POST, request.FILES, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect('system:profile')
        return render(request, 'system/edit_profile.html', {'form': form})

class LogoutView(View):
    def get(self, request):
        logout(request)
        return redirect('/')

class GroupsView(View):
    def get(self, request):
        groups = Group.objects.all()
        return render(request, 'system/groups.html', {'groups': groups})

class StudentsListView(AdminRequiredMixin, View):
    def get(self, request):
        if request.GET != {}:
            students = Student.objects.filter(Q(user__username__icontains = request.GET['search']) | Q(group__name__icontains= request.GET['search'])
                                              | Q(user__first_name__icontains= request.GET['search']) | Q(user__last_name__icontains= request.GET['search']))
        else:
            students = Student.objects.all()
        return render(request, 'system/students.html', {'students': students})

class StudentByGroupView(AdminRequiredMixin,View):
    def get(self,request,id):
        group = get_object_or_404(Group,id=id)
        students = group.students.all()
        return render(request, 'system/students.html', {'students': students})


class EditStudents(AdminRequiredMixin, View):
    def get(self, request, id):
        student = get_object_or_404(Student, id=id)
        form = StudentEditForm(instance=student)
        return render(request, 'system/edit_student.html', {'form': form})

    def post(self, request, id):
        student = get_object_or_404(Student, id=id)
        form = StudentEditForm(request.POST, instance=student)
        if form.is_valid():
            form.save()
            return redirect('system:students')
        return render(request, 'system/edit_student.html', {'form': form})


class DeleteStudentView(AdminRequiredMixin,View):
    def get(self,request,id):
        student = get_object_or_404(Student,id=id)
        user = User.objects.get(username=student.user.username)
        student.delete()
        user.delete()
        return redirect('system:students')

class ResetPasswordView(LoginRequiredMixin,View):
    def get(self,request):
        form = ResetPasswordForm()
        return render(request,'system/reset_password.html',{'form':form})


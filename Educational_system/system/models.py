from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.


class User(AbstractUser):
    USER_ROLE_CHOICES = [
        ('student', "Student"),
        ('teacher', "Teacher"),
        ('admin', "Admin")
    ]
    image = models.ImageField(upload_to='profile_pics/',blank=True,null=True,default='profile_pics/default.jpg')
    phone_number = models.CharField(max_length=13,null=True,blank=True)
    address = models.CharField(max_length=200,null=True,blank=True)
    user_role = models.CharField(max_length=200,choices=USER_ROLE_CHOICES,default="student")

class Teacher(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    date_of_birth = models.DateField(null=True,blank=True)
    def __str__(self):
        return self.user.username

class Group(models.Model):
    name = models.CharField(max_length=100,unique=True)
    data_created = models.DateTimeField(auto_now_add=True)
    end_data = models.DateTimeField(blank=True,null=True)
    teacher = models.ForeignKey(Teacher,on_delete=models.CASCADE,related_name='groups',null=True,blank=True)

    def __str__(self):
        return self.name


class Student(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    date_of_birth = models.DateField(blank=True,null=True)
    group = models.ForeignKey(Group,on_delete=models.CASCADE,related_name='students',null=True,blank=True)

    def __str__(self):
        return self.user.first_name

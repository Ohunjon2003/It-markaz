from django.db import models
from system.models import Group,Student



class Lesson(models.Model):
    group = models.ForeignKey(Group,on_delete=models.CASCADE,related_name='lessons')
    title = models.CharField(max_length=150)
    date = models.DateField(auto_now_add=True)
    update = models.DateTimeField(auto_now=True)
    homework_status = models.BooleanField(default=False)

    class Meta:
        unique_together = ['group','title']

    def __str__(self):
        return self.title


class Homework(models.Model):
    lesson = models.OneToOneField(Lesson,on_delete=models.CASCADE,related_name='homework')
    group = models.ForeignKey(Group,on_delete=models.CASCADE,null=True,blank=True,related_name='homeworks')
    student = models.ForeignKey(Student,on_delete=models.CASCADE,related_name='students')
    description = models.TextField(null=True,blank=True)
    homework_file = models.FileField(upload_to='homeworks/',blank=True,null=True)
    data = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ['student','lesson']

    def __str__(self):
        return f"{self.student.user.first_name}ning {self.lesson.title}  uchun uy vazifasi"
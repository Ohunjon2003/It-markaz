from django import forms
from student.models import Lesson


class CreateLessonForm(forms.Form):
    title = forms.CharField(widget=forms.TextInput({"class":"form-control"}))


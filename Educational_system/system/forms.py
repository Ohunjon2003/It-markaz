from django import forms
from django.contrib.auth.models import User
from .models import User, Student

class LoginForm(forms.Form):
    username = forms.CharField(max_length=100, min_length=4, widget=forms.TextInput({'class': 'form-control'}))
    password = forms.CharField(widget=forms.TextInput({'class': 'form-control width', 'type': 'password'}))

class RegisterForm(forms.ModelForm):
    USER_ROLE_CHOICES = [
        ('student', "Student"),
        ('teacher', "Teacher"),
        ('admin', "Admin")
    ]

    password = forms.CharField(max_length=100, min_length=6, widget=forms.PasswordInput({'class': 'form-control'}))
    confirm_password = forms.CharField(max_length=100, min_length=6, widget=forms.PasswordInput({'class': 'form-control'}))

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'password', 'confirm_password', 'user_role')

    def clean_confirm_password(self):
        password = self.cleaned_data.get('password')
        confirm_password = self.cleaned_data.get('confirm_password')
        if password != confirm_password:
            raise forms.ValidationError("Passwords do not match")
        return confirm_password

    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data['password'])
        if commit:
            user.save()
        return user

class ProfileEditForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'address', 'image', 'phone_number', 'email')

class StudentEditForm(forms.ModelForm):
    date_of_birth = forms.DateField(widget=forms.DateInput({"class":"form-control"}))


    class Meta:
        model = Student
        fields = ('date_of_birth', 'group')

class ResetPasswordForm(forms.Form):
    old_password = forms.CharField(widget=forms.PasswordInput({'class': 'form-control',"placeholder":"old_password"}))
    new_password = forms.CharField(widget=forms.PasswordInput({'class': 'form-control',"placeholder":"new_password"}))
    confirm_password = forms.CharField(widget=forms.PasswordInput({'class': 'form-control',"placeholder":"confirm_password"}))

    def clean_confirm_password(self):
        new_password = self.cleaned_data['new_password']
        confirm_password = self.cleaned_data['confirm_password']

        if new_password != confirm_password:
            raise forms.ValidationError("Passwords don't match")
        return confirm_password
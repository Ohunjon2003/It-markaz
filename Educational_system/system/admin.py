from django.contrib import admin

# Register your models here.
from .models import User,Student,Group,Teacher


admin.site.register(User)
admin.site.register(Student)
admin.site.register(Group)
admin.site.register(Teacher)

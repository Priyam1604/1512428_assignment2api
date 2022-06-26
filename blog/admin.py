from django.contrib import admin

# Register your models here.

from blog.models import *
admin.site.register(Class)
admin.site.register(Student)
admin.site.register(Lecturer)
admin.site.register(Semester)
admin.site.register(Course)
admin.site.register(StudentEnrollment)
from django.contrib import admin
from lab_apps.models import Student, Course, Project

# Register your models here.
admin.site.register(Student)


class StudentAdmin(admin.ModelAdmin):
    list_display = ('student_name', 'student_usn', 'student_sem')
    ordering = ('student_name',)
    search_fields = ('student_name',)


admin.site.register(Course)
admin.site.register(Project)

# students/admin.py
from django.contrib import admin
from .models import Student, ClassRoom

@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ('name', 'age', 'email', 'classroom', 'joined_date')
    search_fields = ('name', 'email')
    list_filter = ('classroom',)

@admin.register(ClassRoom)
class ClassRoomAdmin(admin.ModelAdmin):
    list_display = ('name', 'grade')

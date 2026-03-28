from django.contrib import admin
from .models import Student, Course, Club, Profile

# Register your models here.

class CourseInline(admin.TabularInline):
    model = Course
    extra = 2

class StudentAdmin(admin.ModelAdmin):
    list_display = ('name', 'age', 'email', 'scholorship')
    inlines = [CourseInline]

class ClubAdmin(admin.ModelAdmin):
    list_display = ('name', 'type')
    filter_horizontal = ('students',)

class ProfileAdmin(admin.ModelAdmin):
    list_display = ('student', 'bio')



admin.site.register(Student, StudentAdmin)
admin.site.register(Club, ClubAdmin)
admin.site.register(Profile, ProfileAdmin)
# admin.site.register(Course, CourseInline)


from django.contrib import admin

# Register your models here.
from .models import CourseRegistration

@admin.register(CourseRegistration)
class CourseRegistrationAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'phone', 'academic_documents')
    search_fields = ('name', 'email', 'phone')
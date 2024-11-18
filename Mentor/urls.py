"""
URL configuration for Mentor project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

from courses import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('courses/', views.courses, name='courses'),
    # path('courses.html/', views.courses, name='courses'),
    path('register/', views.register_course, name='register_course'),
    path('registrations/', views.view_registrations, name='view_registrations'),
path('edit/<int:registration_id>/', views.edit_registration, name='edit_registration'),
    path('delete/<int:registration_id>/', views.delete_registration, name='delete_registration'),
]

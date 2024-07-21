"""
URL configuration for fd_lab project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from lab_apps.views import Home, current_datetime, four_hours_ahead, four_hours_before, showlist, home, about, contact, reg, add_project, StudentDetailView, StudentListView, construct_csv_from_model

urlpatterns = [
    path('', Home),
    path('admin/', admin.site.urls),
    path('cdt/', current_datetime),
    path('fha/', four_hours_ahead),
    path('fhb/', four_hours_before),
    path('showlist/', showlist),
    path('home/', home),
    path('about/', about),
    path('contact/', contact),
    path('reg/', reg),
    path('add_project/', add_project),
    path('student_list/', StudentListView.as_view()),
    path('student_detail/<int:pk>/', StudentDetailView.as_view()),
    path('csv/', construct_csv_from_model),
]

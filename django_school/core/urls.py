"""
URL configuration for core project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from school.views import welcoming,json_res, available_courses,totality_student_course,all_students,specdial_course,course_by_teacher,total

urlpatterns = [
    path('admin/', admin.site.urls),
    path('welcome/',welcoming),
    path('json_response/',json_res),
    path('courses/',available_courses ),
    path('total_student_course/' , totality_student_course),
    path('students/',all_students),
    path('courses/<int:course_id>/',specdial_course),
    path('courses/teacher/<int:teacher_id>/',course_by_teacher),
    path('total/' , total)
]

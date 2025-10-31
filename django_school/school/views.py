from django.shortcuts import render
from django.http import HttpResponse
import json
from .models import Student, Course, Teacher


# Create your views here.
def welcoming(request):
    html = """    <html>
        <body style="background-color:#f0f0f0; text-align:center; margin-top:100px;">
            <h1 style="color:blue;">“Welcome to the School
                Management System!</h1>
            <p style="font-size:18px;">this program manages a system to work with school system</p>
        </body>
    </html>"""
    return HttpResponse(html)


def json_res(request):
    info = {
        "name": "ramin",
        "last_name": "mohammadi",
        "age": 22,
        "eamil": "ramindesu@gmail.com",
    }
    json_response = json.dumps(info, indent=4)
    return HttpResponse(json_response)


def available_courses(request):
    all_courses = """Python,
        java,
        cpp,
        js,"""
    return HttpResponse(all_courses)


def totality_student_course(request):
    all_students = Student.objects.all()
    all_courses = Course.objects.all()
    info = {
        "number of students": len(all_students),
        "number of courses": len(all_courses),
    }
    json_info = json.dumps(info)
    return HttpResponse(json_info)


def all_students(request):
    all_students_list = Student.objects.all()
    name = [f"{s.first_name} {s.last_name} " for s in all_students_list]
    return HttpResponse(name)


def specdial_course(request, course_id):
    course = Course.objects.get(id=course_id)
    response = f"Course Name: {course.title}\nDescription: {course.description}"
    return HttpResponse(response)


def course_by_teacher(request, teacher_id):
    teacher = Teacher.objects.get(id=teacher_id)
    courses = Course.objects.filter(teacher=teacher)
    response = f"courses by {teacher.full_name}"
    for course in courses:
        response += f"\nTitle: {course.title}\nDescription: {course.description}\n"
    return HttpResponse(response)

def total(request):
    all_students = Student.objects.all()
    all_courses = Course.objects.all()
    all_teachers = Teacher.objects.all()
    info = {
        "number of students": len(all_students),
        "number of courses": len(all_courses),
        "number of teacher" : len(all_teachers)
    }
    json_info = json.dumps(info)
    return HttpResponse(json_info)


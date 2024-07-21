from django.views import generic
from lab_apps.models import ProjectReg
from lab_apps.models import Course, Student
from django.db import models
from django.shortcuts import render
from django.http import HttpResponse
import datetime


def Home(request):
    return render(request, 'home.html')


def current_datetime(request):
    now = datetime.datetime.now()
    html = "<html><body><h1>It is now %s </h1></body></html>" % now
    return HttpResponse(html)


def four_hours_ahead(request):
    dt = datetime.datetime.now() + datetime.timedelta(hours=4)
    html = "<html><body><h1> After four hours, It will be %s </h1></body></html>" % (
        dt,)
    return HttpResponse(html)


def four_hours_before(request):
    dt = datetime.datetime.now() + datetime.timedelta(hours=-4)
    html = "<html><body><h1> Before 4 hours, It will be %s </h1></body></html>" % (
        dt,)
    return HttpResponse(html)


def showlist(request):
    students = ["Tony", "Mony", "Sony", "Bob"]
    fruits = ["mango", "apple", "banana", "jackfuits"]
    return render(request, "showlist.html", {"fruits": fruits, "students": students})


def home(request):
    return render(request, "home_.html")


def about(request):
    return render(request, "about.html")


def contact(request):
    return render(request, 'contact.html')


def reg(request):
    if request.method == "POST":
        sid = request.POST.get("sname")
        cid = request.POST.get("cname")
        student = Student.objects.get(id=sid)
        course = Course.objects.get(id=cid)
        res = student.enrollment.filter(id=cid)
        if res:
            return HttpResponse("<h1>Student already enrolled</h1>")
        student.enrollment.add(course)
        return HttpResponse("<h1>Student enrolled successfully</h1>")
    else:
        students = Student.objects.all()
        courses = Course.objects.all()
        return render(request, "reg.html", {"students": students, "courses": courses})


def add_project(request):
    if request.method == "POST":
        form = ProjectReg(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponse("<h1>Record inserted successfully</h1>")
        else:
            return HttpResponse("<h1>Record not inserted</h1>")
    else:
        form = ProjectReg()
        return render(request, "add_project.html", {"form": form})


class StudentListView(generic.ListView):
    model = Student
    template_name = "student_list.html"


class StudentDetailView(generic.DetailView):
    model = Student
    template_name = "student_detail.html"

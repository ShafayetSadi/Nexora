from django.shortcuts import render

from classroom.models import Classroom


def home(request):
    classrooms = Classroom.objects.all()
    return render(request, 'home/home.html', {'classrooms': classrooms})

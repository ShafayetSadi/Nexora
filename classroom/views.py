from django.shortcuts import render

# Create your views here.
def classroom(request):
    return render(request,'classroom/classroom.html')
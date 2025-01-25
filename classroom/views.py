from django.shortcuts import render
from django.shortcuts import redirect

from .forms import ClassroomForm


def classroom(request):
    return render(request, 'classroom/classroom.html')


def create_classroom(request):
    if request.method == 'POST':
        form = ClassroomForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('classroom')
    else:
        form = ClassroomForm()
    return render(request, 'classroom/create_classroom.html', {'form': form})

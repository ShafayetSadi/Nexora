from django.shortcuts import render, get_object_or_404
from django.shortcuts import redirect

from .forms import ClassroomForm
from .models import Classroom


def create_classroom(request):
    if request.method == 'POST':
        form = ClassroomForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('classroom')
    else:
        form = ClassroomForm()
    return render(request, 'classroom/create_classroom.html', {'form': form})


def classroom_detail(request, slug):
    classroom = get_object_or_404(Classroom, slug=slug)
    return render(request, 'classroom/classroom_detail.html', {
        'classroom': classroom
    })

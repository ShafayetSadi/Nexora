from django.shortcuts import render
from .forms import UserRegistrationForm


def register_done(request):
    if request.method == 'POST':
        user_form = UserRegistrationForm(request.POST)
        if user_form.is_valid():
            new_user = user_form.save(commit=False)
            new_user.set_password(
                user_form.cleaned_data['password']
            )
            new_user.save()
            return render(request, 'users/register_done.html', {'new_user': new_user})
    else:
        user_form = UserRegistrationForm()
    return render(request, 'users/register.html', {'user_form': user_form})


def profile(request):
    user = request.user
    return render(request, 'users/profile.html', {'user': user})

def register(request):
    return render(request,'users/register.html')


def login(request):
    return render(request,'registration/login.html')
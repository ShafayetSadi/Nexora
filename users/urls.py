from django.urls import path, include

from .views import register, profile ,login,register_done

urlpatterns = [
    path('', include('django.contrib.auth.urls')),
    path('register_done/', register_done, name='register_done'),
    path('profile/', profile, name='profile'),
    path('login/',login,name='user_login'),
    path('register/',register,name='user_register'),
]

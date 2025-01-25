from django.urls import path
from . import views

urlpatterns = [
    path('classroom', views.classroom, name='classroom'),
    path('create_classroom', views.create_classroom, name='create_classroom'),
]

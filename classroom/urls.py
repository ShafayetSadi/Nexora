from django.urls import path
from . import views

urlpatterns = [
    path('create_classroom/', views.create_classroom, name='create_classroom'),
    path('<str:slug>/', views.classroom_detail, name='classroom_detail'),
]


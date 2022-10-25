from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('email/', views.email, name='email'),
    path('edu/', views.edu, name='edu'),
    path('course/', views.course, name='course'),
    path('last', views.last, name='last'),
]
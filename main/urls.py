from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('trenery/', views.trenery, name='trenery'),
    path('schedule/', views.schedule, name='schedule'),
    path('contact/', views.contact, name='contact'),
    path('price/', views.price, name='price'),
    path('training/', views.contact, name='training_create'),
]
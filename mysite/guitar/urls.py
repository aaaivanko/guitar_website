from django.urls import path
from . import views

app_name = 'guitar'

urlpatterns = [
    path('', views.home, name='home'),
    path('home/', views.home, name='home'),
    path('songs/', views.songs, name='songs'),
    path('chords/', views.chords, name='chords'),
    path('contact/', views.contact, name='contact')
]
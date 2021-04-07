from django.shortcuts import render
from .models import Chord


def home(request):
    return render(request, 'guitar/home.html')


def songs(request):
    return render(request, 'guitar/songs.html')


def chords(request):
    context = {
        'title': 'GUITAR CHORDS',
        'chords': Chord.objects.all()
    }
    return render(request, 'guitar/chords.html', context)


def contact(request):
    return render(request, 'guitar/contact.html')

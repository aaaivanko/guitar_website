from django.shortcuts import render


def home(request):
    return render(request, 'guitar/home.html')


def songs(request):
    return render(request, 'guitar/songs.html')


def chords(request):
    return render(request, 'guitar/chords.html')


def contact(request):
    return render(request, 'guitar/contact.html')

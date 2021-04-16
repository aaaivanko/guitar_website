from django.shortcuts import render, redirect
from .models import Chord
from .forms import Contact
from django.core.mail import send_mail
from django.contrib import messages

from datetime import datetime
import calendar
from calendar import HTMLCalendar


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
    if request.method == 'POST':
        form = Contact(request.POST)
        if form.is_valid():
            subject = form.cleaned_data['subject']
            message = form.cleaned_data['message']
            sender = form.cleaned_data['sender']
            recipient = ['ivan.chvartatskyy@gmail.com']

            send_mail(subject, message, sender, recipient)
            messages.success(request, f'You have been sent you form to {recipient[0]} mail successfully!!!')
            return redirect('guitar:home')
    else:
        form = Contact()

    context = {
        'title': 'CONTACT PAGE',
        'form': form
    }

    return render(request, 'guitar/contact.html', context)

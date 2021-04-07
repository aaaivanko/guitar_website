from django.shortcuts import render, redirect
from .forms import RegisterForm


def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = RegisterForm()
    context = {
        'title': 'REGISTER PAGE',
        'form': form
    }
    return render(request, 'user/register.html', context)


def profile(request):
    return render(request, 'user/profile.html')

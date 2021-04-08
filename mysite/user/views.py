from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
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


@login_required
def profile(request):
    return render(request, 'user/profile.html')

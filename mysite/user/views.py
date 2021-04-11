from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import RegisterForm, UploadUserProfile, UploadUserPhoto
from django.contrib import messages


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
    if request.method == 'POST':
        u_form = UploadUserProfile(request.POST, instance=request.user)
        p_form = UploadUserPhoto(request.POST, request.FILES, instance=request.user.profile)
        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            messages.success(request, f'Your account has been updated!')
            return redirect('user:profile')
    else:
        u_form = UploadUserProfile(instance=request.user)
        p_form = UploadUserPhoto(instance=request.user.profile)

    context = {
        'title': 'PROFILE PAGE',
        'u_form': u_form,
        'p_form': p_form
    }
    return render(request, 'user/profile.html', context)

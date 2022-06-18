from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import CustomUserCreationForm

from django.contrib.auth.models import User
from .models import Profile


def profiles(request):
    profiles = Profile.objects.all()
    context = {'profiles': profiles}
    return render(request, 'users/profiles.html', context)


def profile(request, pk):
    profile = Profile.objects.get(uuid=pk)

    top_skills = profile.skill_set.exclude(description="")
    other_skills = profile.skill_set.filter(description="")

    context = {'profile': profile, 'top_skills': top_skills,
               'other_skills': other_skills}
    return render(request, 'users/profile.html', context)


def registerUser(request):
    page = 'register'
    form = CustomUserCreationForm()

    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.username = user.username.lower()
            user.save()

            messages.success(request, "You've been registered!")

            login(request, user)
            return redirect('profiles')
        else:
            messages.error(
                request, 'During registration, an error has occurred.')

    context = {'page': page, 'form': form}
    return render(request, 'users/login_register_form.html', context)


def loginUser(request):
    page = 'login'

    if request.user.is_authenticated:
        return redirect('profiles')

    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        try:
            user = User.objects.get(username=username)

            user = authenticate(request, username=username, password=password)

            if user is not None:
                login(request, user)
                messages.success(request, "You've been logged in!")
                return redirect('profiles')
            else:
                messages.error(
                    request, "Your password is incorrect.")
        except:
            messages.error(request, 'This user does not exist.')

    context = {'page': page}
    return render(request, 'users/login_register_form.html', context)


@login_required
def logoutUser(request):
    logout(request)
    messages.info(request, "You've been logged out.")
    return redirect('login')

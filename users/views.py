from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages

from .forms import (
    CustomUserCreationForm,
    ProfileForm,
    SkillForm,
)

from django.contrib.auth.models import User
from .models import Profile, Skill


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
    form = CustomUserCreationForm()

    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.username = user.username.lower()
            user.save()

            messages.success(request, "You've been registered!")

            login(request, user)
            return redirect('edit-account')
        else:
            messages.error(
                request, 'During registration, an error has occurred.')

    context = {'form': form}
    return render(request, 'users/register.html', context)


def loginUser(request):
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

    context = {}
    return render(request, 'users/login.html', context)


@login_required(login_url='login')
def logoutUser(request):
    logout(request)
    messages.info(request, "You've been logged out.")
    return redirect('login')


@login_required(login_url='login')
def viewAccount(request):
    profile = request.user.profile

    top_skills = profile.skill_set.exclude(description="")
    other_skills = profile.skill_set.filter(description="")

    context = {'profile': profile, 'top_skills': top_skills,
               'other_skills': other_skills}
    return render(request, 'users/account.html', context)


@login_required(login_url='login')
def editAccount(request):
    profile = request.user.profile
    form = ProfileForm(instance=profile)

    if request.method == 'POST':
        form = ProfileForm(request.POST, request.FILES, instance=profile)
        if form.is_valid:
            form.save()
            return redirect('account')

    context = {'form': form}
    return render(request, 'users/account_form.html', context)


@login_required(login_url='login')
def createSkill(request):
    profile = request.user.profile
    form = SkillForm()

    if request.method == 'POST':
        form = SkillForm(request.POST)
        if form.is_valid:
            skill = form.save(commit=False)
            skill.owner = profile
            skill.save()
            return redirect('account')

    context = {'form': form}
    return render(request, 'users/skill_form.html', context)


@login_required(login_url='login')
def updateSkill(request, pk):
    profile = request.user.profile
    skill = profile.skill_set.get(uuid=pk)
    form = SkillForm(instance=skill)

    if request.method == 'POST':
        form = SkillForm(request.POST, instance=skill)
        if form.is_valid:
            form.save()
            return redirect('account')

    context = {'form': form}
    return render(request, 'users/skill_form.html', context)


@login_required(login_url='login')
def deleteSkill(request, pk):
    profile = request.user.profile
    skill = profile.skill_set.get(uuid=pk)

    if request.method == 'POST':
        skill.delete()
        return redirect('account')

    context = {'object': skill}
    return render(request, 'delete_template.html', context)

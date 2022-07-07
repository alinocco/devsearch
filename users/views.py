from cmath import log
from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages

from .forms import (
    CustomUserCreationForm,
    ProfileForm,
    SkillForm,
    MessageForm,
)

from django.contrib.auth.models import User
from .models import Message, Profile

from .utils import searchProfiles, paginateProfiles


def profiles(request):
    profiles, search_query = searchProfiles(request)

    custom_range, profiles = paginateProfiles(
        request, profiles, results_per_page=6, pages_around=3)

    context = {'profiles': profiles, 'query': search_query,
               'custom_range': custom_range}
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
            user.username = user.username
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
                return redirect(request.GET['next'] if 'next' in request.GET else 'account')
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

            messages.success(request, "Your skill was created successfully!")
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

            messages.success(request, "Your skill was updated successfully!")
            return redirect('account')

    context = {'form': form}
    return render(request, 'users/skill_form.html', context)


@login_required(login_url='login')
def deleteSkill(request, pk):
    profile = request.user.profile
    skill = profile.skill_set.get(uuid=pk)

    if request.method == 'POST':
        skill.delete()

        messages.success(request, "Your skill was deleted successfully!")
        return redirect('account')

    context = {'object': skill}
    return render(request, 'delete_template.html', context)


@login_required(login_url='login')
def inbox(request):
    profile = request.user.profile
    inbox = profile.inbox_messages.all()
    unread_count = inbox.filter(is_read=False).count()

    context = {'inbox': inbox, 'unread_count': unread_count}
    return render(request, 'users/inbox.html', context)


@login_required(login_url='login')
def message(request, pk):
    profile = request.user.profile
    message = profile.inbox_messages.get(uuid=pk)

    if message.is_read == False:
        message.is_read = True
        message.save()

    context = {'message': message}
    return render(request, 'users/message.html', context)


def createMessage(request, pk):
    recipient = Profile.objects.get(uuid=pk)
    form = MessageForm()

    try:
        sender = request.user.profile
    except:
        sender = None

    if request.method == 'POST':
        form = MessageForm(request.POST)
        if form.is_valid:
            message = form.save(commit=False)

            message.sender = sender
            message.recipient = recipient

            if sender:
                message.name = sender.name
                message.email = sender.email

            message.save()
            messages.success(request, "Your message was sent successfully!")
            return redirect('profile', pk=recipient.uuid)

    context = {'recipient': recipient, 'form': form}
    return render(request, 'users/message_form.html', context)

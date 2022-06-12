import uuid

from django.shortcuts import render
from django.http import HttpResponse
from .models import Project
from .forms import ProjectForm


def projects(request):
    projects = Project.objects.all()
    context = {'projects': projects}

    return render(request, 'projects/projects.html', context)


def project(request, pk):
    project = Project.objects.get(uuid=pk)
    context = {'project': project}

    return render(request, 'projects/project.html', context)


def createProject(request):
    form = ProjectForm()
    context = {'form': form}

    return render(request, 'projects/project-form.html', context)

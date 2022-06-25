from django.db.models import Q
from .models import Project, Tag

from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage


def searchProjects(request):
    search_query = ''

    if request.GET.get('query'):
        search_query = request.GET.get('query')

    tags = Tag.objects.filter(name__icontains=search_query)

    projects = Project.objects.distinct().filter(
        Q(title__icontains=search_query) |
        Q(description__icontains=search_query) |
        Q(owner__name__icontains=search_query) |
        Q(tags__in=tags)
    )

    return projects, search_query


def paginateProjects(request, projects, results_per_page, pages_around):
    page = request.GET.get('page')
    paginator = Paginator(projects, results_per_page)

    try:
        projects = paginator.page(page)
    except PageNotAnInteger:
        page = 1
        projects = paginator.page(page)
    except EmptyPage:
        page = paginator.num_pages
        projects = paginator.page(page)

    left_border = int(page) - pages_around

    if left_border < 1:
        left_border = 1

    right_border = int(page) + pages_around + 1

    if right_border > paginator.num_pages:
        right_border = paginator.num_pages + 1

    custom_range = range(left_border, right_border)

    return custom_range, projects

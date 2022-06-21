from django.db.models import Q
from .models import Profile, Skill

from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage


def searchProfiles(request):
    search_query = ''

    if request.GET.get('query'):
        search_query = request.GET.get('query')

    skills = Skill.objects.filter(name__icontains=search_query)

    profiles = Profile.objects.distinct().filter(
        Q(name__icontains=search_query) |
        Q(short_description__icontains=search_query) |
        Q(skill__in=skills)
    )

    return profiles, search_query


def paginateProfiles(request, profiles, results_per_page, pages_around):
    page = request.GET.get('page')
    paginator = Paginator(profiles, results_per_page)

    try:
        profiles = paginator.page(page)
    except PageNotAnInteger:
        page = 1
        profiles = paginator.page(page)
    except EmptyPage:
        page = paginator.num_pages
        profiles = paginator.page(page)

    left_border = int(page) - pages_around

    if left_border < 1:
        left_border = 1

    right_border = int(page) + pages_around + 1

    if right_border > paginator.num_pages:
        right_border = paginator.num_pages + 1

    custom_range = range(left_border, right_border)

    return custom_range, profiles

from .models import Profile, Skill
from django.db.models import Q
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage


def paginateProfiles(request, profiles, results):

    page = request.GET.get('page')
    paginator = Paginator(profiles, results)
    try:
        profiles = paginator.page(page)
    except PageNotAnInteger:
        page = 1
        profiles = paginator.page(page)
    except EmptyPage:
        page = paginator.num_pages
        profiles = paginator.page(page)


    neighbors = 1
    start_index = max(1, int(page) - neighbors)
    end_index = min(paginator.num_pages, int(page) + neighbors)
    if end_index < start_index + 2 * neighbors:
        end_index = start_index + 2*neighbors
    elif start_index > end_index - 2*neighbors:
        start_index = end_index - 2*neighbors
    if start_index < 1:
        end_index -= start_index
        start_index = 1
    elif end_index > paginator.num_pages:
        start_index -= (end_index-paginator.num_pages)
        end_index = paginator.num_pages
    
        

    custome_range = range(start_index, end_index+1)

    return custome_range, profiles


def searchProfiles(request):
    search_query = ''
    if request.GET.get('search_query'):
        search_query = request.GET.get('search_query')

    skills = Skill.objects.filter(name__icontains=search_query)
    #print(skills)
    profiles = Profile.objects.distinct().filter(
        Q(name__icontains = search_query) | 
        Q(short_intro__icontains = search_query) |
        Q(skill__in = skills))
    return profiles, search_query
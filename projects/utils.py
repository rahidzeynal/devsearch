from .models import Project
from django.db.models import Q
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage


def paginateProjects(request, projects, results):

    page = request.GET.get('page')
    paginator = Paginator(projects, results)
    try:
        projects = paginator.page(page)
    except PageNotAnInteger:
        page = 1
        projects = paginator.page(page)
    except EmptyPage:
        page = paginator.num_pages
        projects = paginator.page(page)


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

    return custome_range, projects


def searchProject(request):
    search_query = ''
    if request.GET.get('search_query'):
        search_query = request.GET.get('search_query')
    
    # tags = Tag.objects.filter(name_icontains=search_query)

    projects = Project.objects.distinct().filter(
        Q(title__icontains=search_query) |
        Q(description__icontains=search_query) |
        Q(owner__name__icontains=search_query) |
        Q(tags__name__icontains=search_query)
        )
    return projects, search_query
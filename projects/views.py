from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Project, Tag
from django.db.models import Q
from .forms import ProjectForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .utils import searchProject, paginateProjects



def projects(request):
    projects, search_query = searchProject(request)
    custome_range, projects = paginateProjects(request, projects, 4)
    context = {'projects':projects, 'search_query':search_query, 'custome_range':custome_range}
    return render(request,'projects/projects.html', context=context)

def project(request, pk):
    projectObj = Project.objects.get(id = pk)
    tags = projectObj.tags.all()
    context = {'project':projectObj, 'tags':tags}
    return render(request, 'projects/single-project.html', context=context)

@login_required(login_url="login")
def createProject(request):
    profile = request.user.profile

    form = ProjectForm()

    if request.method == 'POST':
        form = ProjectForm(request.POST, request.FILES)
        if form.is_valid():
            project = form.save(commit=False)
            project.owner = profile
            project.save()
            messages.success(request, 'Project was created successfully!')
            return redirect('account')
    context = {'form':form}
    return render(request, 'projects/project_form.html', context=context)

@login_required(login_url="login")
def updateProject(request, pk):
    profile = request.user.profile
    project = profile.project_set.get(id=pk)
    form = ProjectForm(instance=project)

    if request.method == 'POST':
        form = ProjectForm(request.POST, request.FILES, instance=project)
        if form.is_valid():
            form.save()
            messages.success(request, 'Project was updated successfully!')
            return redirect('account')
    context = {'form':form}
    return render(request, 'projects/project_form.html', context=context)

@login_required(login_url="login")
def deleteProject(request, pk):
    profile = request.user.profile
    project = profile.project_set.get(id=pk)
    if request.method == 'POST':
        project.delete()
        messages.success(request, 'Project was deleted successfully!')
        return redirect('account')
    context = {'object':project}
    return render(request, 'delete_template.html', context=context)
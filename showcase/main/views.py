from django.shortcuts import render
from .models import CityModel, TypeModel, MarkModel, ProjectModel


def main(request):
    access_level = 1
    projects = ProjectModel.objects.all()
    projects_list = []
    for project in projects:
        if (project.AccessLevel<=access_level):
            projects_list.append(project)

    return render(request, "main/main.html", {'content': 'Проектики', 'title': 'main', 'projects': projects_list})


def authorization(request):
    return render(request, "authorization/authorization.html")


def search(request):
    return render(request, "search/search.html")


def project_page(request):
    project = ProjectModel.objects.get(id=2)
    access_level = 0

    if (project.AccessLevel>access_level):
        return render(request, "default.html", {'content': 'Нет доступа', 'title': 'Project'})
    else:
        return render(request, "project/project.html", {'content': 'Проектик', 'title': 'Project', 'project': project})


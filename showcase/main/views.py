from django.http import HttpResponse
from django.shortcuts import render
from .models import CityModel, TypeModel, MarkModel, ProjectModel


def main(request):
    a = ProjectModel.objects.all()
    return render(request, "main/main.html", {'content': 'Проектики', 'title': 'main', 'projects': a})


def authorization(request):
    return render(request, "authorization/authorization.html")


def search(request):
    return render(request, "search/search.html")



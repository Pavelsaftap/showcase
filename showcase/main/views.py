from django.http import HttpResponse
from django.shortcuts import render
from .models import CityModel, TypeModel, MarkModel, ProjectModel


def main(request):
    a = ProjectModel.objects.all()
    return render(request, "main/main.html", {'content': 'Проектики', 'title': 'main', 'projects': a})


def authorization(request):
    return HttpResponse('Authorization')


def search(request):
    return HttpResponse("Search")



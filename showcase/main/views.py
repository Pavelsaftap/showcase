from django.shortcuts import render
from .models import CityModel, TypeModel, MarkModel, ProjectModel
from django.urls import reverse_lazy
from django.views.generic import CreateView
from .forms import RegisterUserForm, LoginUserForm
from django.shortcuts import redirect
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth import logout, login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import LoginView
from random import shuffle


def check_access(request, projects, check_main=0):
    access_level = 1
    projects_list = []

    for project in projects:
        if (project.AccessLevel > access_level or (project.ShowMainPage == 0 and check_main == 1)):
            continue

        sum = 0
        count = 0
        for mark in project.Marks.all():
            sum += mark.Score
            count += 1
        project.AverageMark = sum // count
        project.save()

        projects_list.append(project)

    return projects_list


def main(request):
    projects = ProjectModel.objects.all()
    projects_list = check_access(request, projects, 1)

    return render(request, "main/main.html", {'content': 'Проектики', 'title': 'main', 'projects': projects_list})


def parse_search(params):
    params += ';'
    params_parse_list = params.split(';')
    sortby = params_parse_list[0]
    reverse = 0
    try:
        if sortby[-1] == '$':
            sortby = sortby[:-1]
            reverse = 1
        sortby = int(sortby)
    except:
        sortby = 0
    return [[sortby, reverse]]


def get_sort(projects_list, search_ask):
    if search_ask[0][0] == 0:
        shuffle(projects_list)
    elif search_ask[0][0] == 1:
        projects_list.sort(key=lambda x: x.AverageMark, reverse=True)
    elif search_ask[0][0] == 2:
        projects_list.sort(key=lambda x: x.Name)
    elif search_ask[0][0] == 3:
        projects_list.sort(key=lambda x: x.AccessLevel, reverse=True)

    if search_ask[0][1] == 1:
        projects_list.reverse()
    return projects_list


def search(request, params=''):
    sort_list = [{'link': 'http://127.0.0.1:8000/search/params=0', 'val': 'Random'},
                 {'link': 'http://127.0.0.1:8000/search/params=1', 'val': 'AvgMark'},
                 {'link': 'http://127.0.0.1:8000/search/params=2', 'val': 'Name'},
                 {'link': 'http://127.0.0.1:8000/search/params=3', 'val': 'AccessLevel'}]

    if (params.count(';') > 1 or params == ''):
        projects = ProjectModel.objects.all()
        projects_list = check_access(request, projects, 1)
        return render(request, "search/search.html",
                      {'content': params, 'title': 'search', 'sort_list': sort_list, 'projects': projects_list})

    search_ask = parse_search(params)

    projects = ProjectModel.objects.all()
    projects_list = check_access(request, projects)
    projects_list = get_sort(projects_list, search_ask)

    return render(request, "search/search.html",
                  {'content': params, 'title': 'search', 'sort_list': sort_list, 'projects': projects_list})


def project_page(request, project_id):
    result = 0
    try:
        project = ProjectModel.objects.get(id=project_id)

        access_level = 1
        if (project.AccessLevel > access_level):
            result = 1
        sum = 0
        count = 0
        for mark in project.Marks.all():
            sum += mark.Score
            count += 1
        project.AverageMark = sum // count
        project.save()
    except:
        result = 2

    if (result == 0):
        return render(request, "project/project.html", {'title': 'Project', "access": result, 'project': project})
    else:
        return render(request, "project/project.html", {'title': 'Project', "access": result})


class RegisterUser(CreateView):
    form_class = RegisterUserForm
    template_name = 'main/register.html'
    success_url = reverse_lazy('login')


class LoginUser(LoginView):
    form_class = LoginUserForm
    template_name = 'main/login.html'

    def get_success_url(self):
        return reverse_lazy('index')


def logout_user(request):
    logout(request)
    return redirect('login')

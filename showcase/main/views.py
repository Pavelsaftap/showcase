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


def main(request):
    access_level = 1
    projects = ProjectModel.objects.all()

    projects_list = []
    for project in projects:
        if (project.AccessLevel>access_level or project.ShowMainPage==0):
            continue

        sum = 0
        count = 0
        for mark in project.Marks.all():
            sum += mark.Score
            count += 1
        project.AverageMark = sum // count
        project.save()

        projects_list.append(project)

    return render(request, "main/main.html", {'content': 'Проектики', 'title': 'main', 'projects': projects_list})


def search(request):
    return render(request, "search/search.html")


def project_page(request, project_id):
    result = 0
    try:
        project = ProjectModel.objects.get(id=project_id)
        access_level = 0
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

    if (result==0):
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

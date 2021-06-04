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

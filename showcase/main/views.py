from django.http import HttpResponse
from django.shortcuts import render
from .models import CityModel, TypeModel, MarkModel, ProjectModel
from django.urls import reverse_lazy
from django.views.generic import CreateView
from .forms import RegisterUserForm, LoginUserForm
from django.shortcuts import redirect
from django.contrib.auth import logout, login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import LoginView


def main(request):
    a = ProjectModel.objects.all()
    return render(request, "main/main.html", {'content': 'Проектики', 'title': 'main', 'projects': a})


def authorization(request):
    return HttpResponse('Authorization')


def search(request):
    return HttpResponse("Search")


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

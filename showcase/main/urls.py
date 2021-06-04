from django.urls import path

from . import views

urlpatterns = [
    path('', views.main, name='main'),
    path('authorization', views.authorization, name='authorization'),
    path('search', views.search, name='search'),
    path('project', views.project_page, name='project'),


]
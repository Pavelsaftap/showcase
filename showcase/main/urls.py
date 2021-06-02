from django.urls import path

from . import views

urlpatterns = [
    path('', views.main, name='index'),
    path('authorization', views.authorization, name='authorization'),
    path('search', views.search, name='search'),


]
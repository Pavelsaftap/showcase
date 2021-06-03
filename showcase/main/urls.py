from django.urls import path

from . import views

urlpatterns = [
    path('', views.main, name='index'),
    path('authorization', views.authorization, name='authorization'),
    path('search', views.search, name='search'),
    path('login/', views.LoginUser.as_view(), name='login'),
    path('logout/', views.logout_user, name='logout'),
    path('register/', views.RegisterUser.as_view(), name='register'),


]
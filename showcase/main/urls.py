from django.urls import path
from . import views

urlpatterns = [
    path('', views.main, name='index'),
    # path('search/', views.search, name='search'),
    # path('search/params=<str:params>', views.search, name='search_params'),
    path('search/', views.SearchResultsView.as_view(), name='search_results'),
    path('project/id=<int:project_id>', views.project_page, name='project'),
    path('login/', views.LoginUser.as_view(), name='login'),
    path('logout/', views.logout_user, name='logout'),
    path('register/', views.RegisterUser.as_view(), name='register'),

]

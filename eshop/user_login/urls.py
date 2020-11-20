from django.urls import path, include
from .import views

urlpatterns = [
    path('', views.user_loging, name='home-deshboard'), #url for home deshboard
    path('logout/', views.user_logout, name='user-logout'), #user logout url
    

]
"""
URL configuration for onlineemployee project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from onlineschool import views

urlpatterns = [
    path('home/',views.Home.as_view(),name="home"),
    path('studentA/', views.StudentView.as_view(), name="studentA"),
    # path('studentAll/', views.listAll, name="studentAll"),
    path('remove/<int:sid>',views.remove,name='remove'),

    path('login/', views.LoginView.as_view(), name='login'),
    path('logout/', views.Logout, name='logout'),
    # relationship
    path('ide/', views.IdeCreateView.as_view(), name='ide'),
    path('per/', views.PersonCreateView.as_view(), name='per'),

    path('enrolladd/', views.EnrollView.as_view(), name='enrolladd'),
    path('enrollall/', views.EnrollView.listAll, name='enrollall'),

]

"""assignment URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from api.views import *
urlpatterns = [
    path('admin/', admin.site.urls),
    path("incomplete/",IncompleteReminder.as_view(),name="Incomplete Reminders"),
    path("complete/",CompleteReminder.as_view(),name="Complete Reminders"),
    path("post/reminder/",PostReminder.as_view(),name="Post Reminders"),
    path("update/reminder/",UpdateReminder.as_view(),name="Update Reminders"),
    path("delete/reminder<int:pk>",DeleteReminder.as_view(),name="Delete Reminder"),
]

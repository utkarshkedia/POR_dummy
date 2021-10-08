from django.contrib import admin
from django.urls import path
from userGrouping import views
from mail_api import views as mail_view

urlpatterns = [
    path('', views.home),
    path('mail/',mail_view.track_modifications)
    ]
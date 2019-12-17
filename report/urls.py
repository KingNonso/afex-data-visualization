from django.urls import path, include
from report.dash_apps.finished_apps import simpleexample, examplegraph

from . import views

app_name = 'report'


urlpatterns = [
    path('', views.home, name='dashboard'),
    path('1/', views.grafiti, name='grafiti'),
]

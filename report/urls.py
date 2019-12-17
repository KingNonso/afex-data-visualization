from django.urls import path
from report.dash_apps.finished_apps import simpleexample, examplegraph, datagram, datagram2, dropdown, callback, \
    callback2, interactive

from . import views

app_name = 'report'


urlpatterns = [
    path('', views.home, name='dashboard'),
    path('1/', views.grafiti, name='grafiti'),
    path('2/', views.datagram, name='datagram'),
    path('3/', views.datagram2, name='datagram2'),
    path('4/', views.dropdown, name='dropdown'),
    path('5/', views.callback, name='callback'),  # similar to 3
    path('6/', views.callback2, name='callback2'),
    path('7/', views.interactive, name='interactive'),
]

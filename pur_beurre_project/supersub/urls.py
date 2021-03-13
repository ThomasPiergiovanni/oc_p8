from django.urls import path

from . import views

app_name = 'supersub'

urlpatterns = [
    path('', views.index, name='index'),
]

from django.urls import path

from . import views

app_name = 'supersub'

urlpatterns = [
    path('', views.index, name='index'),
    path('aliment/', views.aliment, name='aliment'),
    path('create_account/', views.create_account, name='create_account'),
    path('login/', views.login, name='login'),
    path('registered_aliments/', views.registered_aliments, name='registered_aliments'),
    path('results/', views.results, name='results'),
]

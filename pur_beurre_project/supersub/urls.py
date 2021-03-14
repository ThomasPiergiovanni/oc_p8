from django.urls import path

from . import views

app_name = 'supersub'

urlpatterns = [
    path('', views.index, name='index'),
    path('results/', views.results, name='results'),
    path('account/', views.account, name='account'),
    path('aliment/', views.aliment, name='aliment'),
    path('create_account/', views.create_account, name='create_account'),
]

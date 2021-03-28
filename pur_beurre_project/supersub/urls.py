from django.urls import path

from . import views

app_name = 'supersub'

urlpatterns = [
    path('', views.index, name='index'),
    path('aliment/', views.aliment, name='aliment'),
    path('registered_aliments/', views.registered_aliments, name='registered_aliments'),
    path('results/', views.results, name='results'),
    path('test_results/', views.test_results, name='test_results'),
]

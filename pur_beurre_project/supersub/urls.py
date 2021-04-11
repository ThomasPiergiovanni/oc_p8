from django.urls import path

from . import views

app_name = 'supersub'

urlpatterns = [
    path('', views.index, name='index'),
    path('aliment/<int:id_product>', views.aliment, name='aliment'),
    path('registered_aliments/', views.registered_aliments, name='registered_aliments'),
    path('results/', views.results, name='results'),
    path('register_product/<int:id_product>,/<int:id_user>', views.register_product, name='register_product'),
]

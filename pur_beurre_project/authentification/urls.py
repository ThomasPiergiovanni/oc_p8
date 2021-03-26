from django.urls import path

from . import views

app_name = 'authentification'

urlpatterns = [
    path('create_account/', views.create_account, name='create_account'),
    path('login/', views.login, name='login'),
    path('account/', views.account, name='account'),
]
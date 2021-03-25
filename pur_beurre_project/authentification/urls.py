from django.urls import path

from . import views

app_name = 'authentification'

urlpatterns = [
    path('account/', views.account, name='account'),
]
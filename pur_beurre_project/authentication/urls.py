from django.urls import path

from . import views

app_name = 'authentication'

urlpatterns = [
    path('sign_up/', views.sign_up, name='sign_up'),
    path('sign_in/', views.sign_in, name='sign_in'),
    path('account/', views.account, name='account'),
    # path('test_account_creation/', views.test_account_creation, name='test_account_creation'),
]
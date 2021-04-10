from django.urls import path

from . import views

app_name = 'authentication'

urlpatterns = [
    path('signin/', views.signin, name='signin'),
    path('login/', views.login, name='login'),
    path('account/', views.account, name='account'),
    # path('test_account_creation/', views.test_account_creation, name='test_account_creation'),
]
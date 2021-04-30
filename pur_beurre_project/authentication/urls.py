from django.urls import path

from . import views
from .views import AccountView

app_name = 'authentication'

urlpatterns = [
    path('sign_up/', views.sign_up, name='sign_up'),
    path('sign_in/', views.sign_in, name='sign_in'),
    path('sign_out/', views.sign_out, name='sign_out'),

    path('account/', AccountView.as_view(), name='account'),
    # path('account/', views.account, name='account'),
]
from django.urls import path

from . import views
from .views import AccountView, SignUpView

app_name = 'authentication'

urlpatterns = [
    path('sign_up/', SignUpView.as_view(), name='sign_up'),
    path('sign_in/', views.sign_in, name='sign_in'),
    path('sign_out/', views.sign_out, name='sign_out'),

    path('account/', AccountView.as_view(), name='account'),
]
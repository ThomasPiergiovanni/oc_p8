from django.urls import path

from . import views
from .views import AccountView, SignUpView, SignInView, SignOutView

app_name = 'authentication'

urlpatterns = [
    path('sign_up/', SignUpView.as_view(), name='sign_up'),
    path('sign_in/', SignInView.as_view(), name='sign_in'),
    path('sign_out/', SignOutView.as_view(), name='sign_out'),
    path('account/', AccountView.as_view(), name='account'),
]
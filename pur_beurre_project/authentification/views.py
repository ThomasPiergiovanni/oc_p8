from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse

from authentification.user_session_manager import UserSessionManager
from authentification.models import User

# Create your views here.

def account(request):
    user_session = UserSessionManager()
    if user_session.active:
        return render(request, 'authentification/account.html')
    else:
        return login(request)

# def create_account(request):
#     context ={
#         'message': "Connection",
#         'button_message': "Créer"
#     }
#     return render(request, 'authentification/create_account.html', context)

def create_account(request):

    if request.method == 'POST':
        try:
            email = request.POST['create_account_email']
            existing_user = User.objects.get(email__iexact=email)
            context ={
                'error_message': " est déja utilisé. Choissisez un autre nom.",
                'email': existing_user.email
            }
            return render(request, 'authentification/create_account.html', context)
        except:
            email = request.POST['create_account_email']
            password = request.POST['create_account_password']
            first_name = request.POST['create_account_first_name']
            user = User(
                first_name=first_name,
                email=email,
                password=password
            )
            print(user.first_name)
            user.save()
            context = {
                'error_message': " n'est pas utilisé",
                'email': email,
            }
            return render(request, 'authentification/create_account.html', context)
    else:
        return render(request, 'authentification/create_account.html') 


    #     email = request.POST['create_account_email']
    #     user_exist = User.objects.get(email__iexact=email)
    #     if user_exist:
    #         context ={
    #             'error_message': " est déja utilisé. Choissisez un autre nom.",
    #             'email': user_exist.email
    #         }
    #         return render(request, 'authentification/create_account.html', context)


    #         # user = User(
    #         #     first_name=first_name,
    #         #     email=email,
    #         #     password=password
    #         # )
    #         # print(user.first_name)
    #         # user.save()
    #         # return render(request, 'supersub/index.html')
    #         # return HttpResponseRedirect(reverse('supersub:index'))

    #         context = {
    #             'error_message': " n'est pas utilisé",
    #             'email': email,
    #         }
    #         return render(request, 'authentification/create_account.html', context)
    # except:
    #     if request.method == 'POST':
    #         email = request.POST['create_account_email']
    #         password = request.POST['create_account_password']
    #         first_name = request.POST['create_account_first_name']
    #         user = User(
    #             first_name=first_name,
    #             email=email,
    #             password=password
    #         )
    #         print(user.first_name)
    #         user.save()
    #         context = {
    #             'error_message': " n'est pas utilisé",
    #             'email': email,
    #         }
    #         return render(request, 'authentification/create_account.html', context)
    #     else:
    #         return render(request, 'authentification/create_account.html')

# def create_account(request):
#     try:
#         first_name = request.POST['create_account_first_name']
#         email = request.POST['create_account_email']
#         password = request.POST['create_account_password']
#         user_exist = User.objects.get(email__iexact=email)
#         if user_exist:
#             context ={
#                 'error_message': " est déja utilisé. Choissisez un autre nom.",
#                 'email': user_exist.email
#             }
#             return render(request, 'authentification/create_account.html', context)
#         else:
#             print("bug")
#             # user = User(
#             #     first_name=first_name,
#             #     email=email,
#             #     password=password
#             # )
#             # print(user.first_name)
#             # user.save()
#             # return render(request, 'supersub/index.html')
#             # return HttpResponseRedirect(reverse('supersub:index'))
#     except:
#         return render(request, 'authentification/create_account.html')

def login(request):
    context ={
        'message': "Se connecter",
        'button_message': "Se connecter"
    }
    return render(request, 'authentification/login.html', context)



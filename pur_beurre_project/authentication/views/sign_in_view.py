from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect

from authentication.forms.sign_in_form import SignInForm
from supersub.views.custom_view import CustomView


class SignInView(CustomView):
    """
    """
    def __init__(self):
        """
        """
        super().__init__()
        self.data['redirect'] = 'supersub:index'
        self.data['render'] = 'authentication/sign_in.html'

    def get(self, request):
        """
        """
        form = SignInForm()
        self.data['ctxt']['form'] = form
        return render(request, self.data['render'], self.data['ctxt'])
    
    def post(self, request):
        """
        """
        logout(request)
        form = SignInForm(data=request.POST)
        if form.is_valid():
            email = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(email=email, password=password)
            if user is not None:
                login(request, user)
                return redirect(self.data['redirect'])
        else:
            self.data['ctxt']['form'] = form
            return render(request, self.data['render'], self.data['ctxt'])
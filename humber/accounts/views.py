from django.shortcuts import render
from django.contrib.auth import authenticate, login
from django.contrib.auth import logout
from django.views import View
from applications.models import Agent
from accounts.forms import UserLoginForm
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse

class LoginView(View):
    login_form = UserLoginForm
    template_name = 'accounts/login.html'

    #display blank form
    def get(self, request):
        form = self.login_form(None)
        return render(request, self.template_name, {'form':form})
    #process form data
    def post(self, request):
        form = self.login_form(request.POST)
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                return HttpResponseRedirect(reverse('applications:home'))
            else:
                return HttpResponse("Your account has been disabled")
        else:
            return HttpResponse("Invalid login")

class LogoutView(View):
    template_name = 'accounts/logout.html'

    def post(self, request):
        logout(request)
        return render(request, self.template_name)







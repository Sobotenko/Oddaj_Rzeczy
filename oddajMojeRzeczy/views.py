from django.shortcuts import render
from django.template.response import TemplateResponse
from django.views import View

# Create your views here.
class LandingPageView(View):
    def get(self, request):
        return TemplateResponse(request, "index.html")

class AddDonationView(View):
    def get(self, request):
        return TemplateResponse(request, "form-confirmation.html")

class LoginView(View):
    def get(self, request):
        return TemplateResponse(request, "login.html")

class RegisterView(View):
    def get(self, request):
        return TemplateResponse(request, "register.html")

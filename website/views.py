from django.shortcuts import render
from .models import *
from django.views import View

# Create your views here.


class HomeView(View):
    def get(self, request):
        return render(request, 'index.html')
    
class ServiceView(View):
    def get(self, request):
        return render(request, 'services.html')
    
class AboutView(View):
    def get(self, request):
        return render(request, 'about.html')


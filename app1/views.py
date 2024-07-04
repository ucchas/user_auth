from django.shortcuts import render
from django.urls import reverse,reverse_lazy

# Create your views here.
from django.views.generic import CreateView
from app1.forms import *

class Signup(CreateView):
    form_class = UserCreateForm
    template_name = 'signup.html'
    success_url = reverse_lazy('index')

def index(request):
    return render(request,'index.html')

def greet(request):
    return render(request,'greet.html',{'user':request.user})
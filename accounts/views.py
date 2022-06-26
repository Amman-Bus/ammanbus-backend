from email import message
from django.shortcuts import render, redirect
from django.contrib.auth import login, logout,authenticate, get_user_model
from django.contrib.auth.forms import AuthenticationForm
from django.contrib import messages
from django.views.generic import CreateView
from .models import User
from .forms import PassengerSignUpForm, DriverSignUpForm

# Create your views here.
User = get_user_model()

def home(request):
    return render(request, 'home.html')

def register(request):
    return render(request, 'register.html')

class passenger_register(CreateView):
    model = User  
    form_class = PassengerSignUpForm
    template_name= 'passenger_register.html'

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect('/accounts/home')

class driver_register(CreateView):
    model = User  
    form_class = DriverSignUpForm
    template_name= 'driver_register.html'

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect('/accounts/home')

def login_user(request):
    if request.method=='POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None :
                login(request,user)
                return redirect('/accounts/home')
            else:
                messages.error(request,"Invalid username or password")
        else:
            messages.error(request,"Invalid username or password")
    return render(request, 'login.html',context={'form':AuthenticationForm()})

def logout_user(request):
    logout(request)
    return redirect('/accounts/home')
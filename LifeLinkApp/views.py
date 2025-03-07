from django.contrib import messages
from django.shortcuts import render,redirect
from .forms import RegisterForm,CustomLoginForm
from django.contrib.auth import login



def index(request):
    return render(request, 'index.html')

def login_page(request):
    if request.method == 'POST':
        form = CustomLoginForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('homepage')  # Redirect to the home page after successful login
    else:
        form = CustomLoginForm()

    return render(request, 'login.html',{'form':form})


def signup(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Registration successful! Please log in.")
            return redirect('login')
    else:
        form = RegisterForm()

    return render(request, 'signup.html', {'form': form})


def blood_donation(request):
    return render(request, 'blood_donation.html')



# Create your views here.

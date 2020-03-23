from django.contrib.auth import logout, login
from django.shortcuts import render, redirect
from django.contrib.auth.forms import  AuthenticationForm
from . forms import UserCreationForm
# Create your views here.
def signupV(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect("/")
    else:
        form = UserCreationForm()
    return render(request, 'signup.html', {'form': form})


def loginV(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        print(form)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect("/")
    else:
        form = AuthenticationForm()
    return render(request, 'login.html', {'form': form})


def logoutV(request):
    if request.method == "POST" or "GET":
        logout(request)
        print("logging out")
        return redirect('/')


def profile(request):

    return render(request,"profile.html")

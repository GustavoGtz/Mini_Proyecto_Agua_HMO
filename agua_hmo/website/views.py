from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm


# Create your views here.

def home(request):
    return render(request, 'home.html', {})


def manage_users(request):
    return render(request, 'manage_users.html', {})


def manage_payment_concept(request):
    return render(request, 'manage_payment_concept.html', {})


def createUser(request):
    form = UserCreationForm()
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    return render(request, 'user_form.html', {"form": form})

#
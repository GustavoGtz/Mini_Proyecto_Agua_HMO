from django.shortcuts import render, redirect
from .forms import UserForm


# Create your views here.

def home(request):
    return render(request, 'home.html', {})


def manage_users(request):
    return render(request, 'manage_users.html', {})


def manage_payment_concept(request):
    return render(request, 'manage_payment_concept.html', {})


def createUser(request):
    form = UserForm()
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')

    context = {'form': form}
    return render(request, 'manage_users.html', {})

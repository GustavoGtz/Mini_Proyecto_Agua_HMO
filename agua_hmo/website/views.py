from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from .models import Users


# Create your views here.

def home(request):
    return render(request, 'home.html', {})

def manage_users(request):
    return render(request, 'manage_users.html', {})

def manage_payment_concept(request):
    if request.method == 'POST':
        user_meter_number = int(request.POST.get('meter_number', 0))
        searched_user = Users.objects.filter(meter_number=user_meter_number)
        if searched_user.exists():
            return render(request, 'user_manage_payment_concept.html', {'user' : searched_user.first})
        else:
            return render(request, 'manage_payment_concept.html', {'error': True})
    return render(request, 'manage_payment_concept.html', {'error': False})

def createUser(request):
    form = UserCreationForm()
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    return render(request, 'user_form.html', {"form": form})





from django.shortcuts import render

# Create your views here.

def home(request):
    return render(request, 'home.html', {})

def manage_users(request):
    return render(request, 'manage_users.html', {})

def manage_payment_concept(request):
    return render(request, 'manage_payment_concept.html', {})


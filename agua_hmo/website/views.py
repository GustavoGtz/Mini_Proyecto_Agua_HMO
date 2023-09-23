from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from .models import Users, Debts, Concepts
from .forms import UserForm
import json



# Create your views here.

def home(request):
    return render(request, 'home.html', {})

def manage_users(request):
    return render(request, 'manage_users.html', {})

def manage_payment_concept(request):
    if request.method == 'POST':
        action = request.POST.get('action')
        if action == 'find_user':
            user_meter_number = int(request.POST.get('meter_number', 0))
            searched_user = Users.objects.filter(meter_number=user_meter_number)
            if searched_user.exists():
                return render(request, 'user_manage_payment_concept.html', {'user' : searched_user.first, 'debts' : Debts.objects.filter(meter_number=user_meter_number)})
            else:
                return render(request, 'manage_payment_concept.html', {'error': True})
        if action == 'create_ticket':
            print("@AAAAAAAAFRawfaw")
            print(request.POST.get('meter_number'))
            user_meter_number = int(request.POST.get('meter_number', 0))
            ticket_year = int(request.POST.get('year', 0))
            ticket_month = int(request.POST.get('month', 0))

            concep_info = Concepts.objects.filter(year=ticket_year)
            debt_info = Debts.objects.filter(meter_number=user_meter_number, year=ticket_year, month=ticket_month)

            water_cons = concep_info.consumption_per_cubic * debt_info.water_usage_m3
            drainage = concep_info.drainage_fee
            sanitation = concep_info.sanitation
            red_cross = concep_info.red_cross
            firefighters = concep_info.firefighters
            total_month = debt_info.total_month
            previous_debt = debt_info.previous_debt
            total = water_cons + drainage + sanitation + red_cross + firefighters + total_month + previous_debt


            return render(request, 'ticket.html', {'user' : Users.objects.filter(meter_number=user_meter_number).first,
                                                   'ticket' : Debts.objects.filter(meter_number=user_meter_number, year=ticket_year, month=ticket_month).first,
                                                   'concepts' : Concepts.objects.filter(year=ticket_year)})

        
    return render(request, 'manage_payment_concept.html', {'error': False})

def create_user(request):
    form = UserForm()
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    context = {'form': form}
    return render(request, 'user_form.html', context)

def delete_user(request):
    if request.method == 'POST':
        user_meter_number = int(request.POST.get('meter_number', 0))
        searched_user = Users.objects.filter(meter_number=user_meter_number)
        if searched_user.exists():
            searched_user.delete()
            #return render(request, 'delete.html', {})
    return render(request, 'manage_payment_concept.html', {'error': False})

def update_user(request):
    if request.method == 'POST':
        user_meter_number = int(request.POST.get('meter_number', 0))
        searched_user = Users.objects.filter(meter_number=user_meter_number)
        if searched_user.exists():
            user_user_name = request.POST.get('user_name', 0)
            user_contract_type = request.POST.get('contract_type', 0)
            user_home_direction = request.POST.get('home_direction', 0)
            searched_user.update(user_name=user_user_name)
            searched_user.update(contract_type=user_contract_type)
            searched_user.update(home_direction=user_home_direction)
            return redirect('home')
        else:
            return render(request, 'update_user.html', {'error' : True})

    return render(request, 'update_user.html', {'error' : False})

def show_user(request):
    if request.method == 'POST':
        user_meter_number = int(request.POST.get('meter_number', 0))
        searched_user = Users.objects.filter(meter_number=user_meter_number)
        if searched_user.exists():
            return render(request, 'user_info.html', {'user' : searched_user.first})
        else:
            return render(request, 'manage_payment_concept.html', {'error': True})
    return render(request, 'manage_payment_concept.html', {'error': False})







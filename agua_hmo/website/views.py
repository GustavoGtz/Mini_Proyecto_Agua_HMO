from django.shortcuts import render, redirect
from .models import Users, Debts, Concepts
from .forms import UserForm
from django.utils import timezone
from django.contrib import messages
import random



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
            user_meter_number = int(request.POST.get('meter_number', 0))
            ticket_year = int(request.POST.get('year', 0))
            ticket_month = int(request.POST.get('month', 0))

            concep_info = Concepts.objects.get(year=ticket_year)
            debt_info = Debts.objects.get(meter_number=user_meter_number, year=ticket_year, month=ticket_month)

            water_cost = concep_info.consumption_per_cubic * debt_info.water_usage_m3
            drainage_cost = concep_info.drainage_fee * water_cost
            sanitation_cost = concep_info.sanitation * water_cost
            red_cross_cost = concep_info.red_cross * water_cost
            firefighters_cost = concep_info.firefighters * water_cost
            total_month = water_cost + drainage_cost + sanitation_cost + red_cross_cost + firefighters_cost
            previous_debt = debt_info.previous_debt
            total = total_month + previous_debt

            return render(request, 'ticket.html', {'user' : Users.objects.filter(meter_number=user_meter_number).first,
                                                   'ticket' : Debts.objects.filter(meter_number=user_meter_number, year=ticket_year, month=ticket_month).first,
                                                   'water_cons' : water_cost,
                                                   'drainage' : drainage_cost,
                                                   'sanitation' : sanitation_cost,
                                                   'red_cross' : red_cross_cost,
                                                   'firefighters' : firefighters_cost,
                                                   'total_month' : total_month,
                                                   'previous_debt' : previous_debt,
                                                   'total' : total
                                                   })
        
        if action == 'create_debt':
            user_meter_number = int(request.POST.get('meter_number', 0))
            searched_user = Users.objects.filter(meter_number=user_meter_number)
            user_meter_number = int(request.POST.get('meter_number', 0))
            user_history_of_debts = Debts.objects.filter(meter_number=user_meter_number)
            if user_history_of_debts.exists():
                user_last_debt = user_history_of_debts.latest('id')
                random_water_usage = random.uniform(1, 10)
                # Function to calculate the next year/month of the new debt
                def calculate_next_debt_date(year, month):
                    new_month = month + 1
                    if(new_month >= 13) : 
                        return(year+1, 1)
                    else:
                        return(year, new_month)
                new_debt_date = calculate_next_debt_date(user_last_debt.year, user_last_debt.month)
                concep_info = Concepts.objects.get(year=new_debt_date[0])
                water_cost = concep_info.consumption_per_cubic * random_water_usage
                total_month_full = (water_cost +
                                         concep_info.drainage_fee * water_cost + 
                                         concep_info.sanitation * water_cost +
                                         concep_info.red_cross * water_cost +
                                         concep_info.firefighters * water_cost +
                                         user_last_debt.total_month)
                # Generar pagina para cargar nuevo adeudeo.
                new_debt = Debts(meter_number = user_meter_number,
                                 year = new_debt_date[0],
                                 month = new_debt_date[1],
                                 cut = 20,
                                 water_usage_m3 = round(random_water_usage, 3),
                                 previous_debt = user_last_debt.total_month,
                                 total_month = total_month_full)
                new_debt.save()
                return render(request, 'user_manage_payment_concept.html', {'user' : searched_user.first, 'debts' : Debts.objects.filter(meter_number=user_meter_number)})
            else:
                current_date = timezone.now().date()
                current_year = current_date.year
                current_month = current_date.month

                concep_info = Concepts.objects.get(year=current_year)
                random_water_usage = random.uniform(1, 10)
                water_cost = concep_info.consumption_per_cubic * random_water_usage
                
                total_month_full = (water_cost +
                                         concep_info.drainage_fee * water_cost + 
                                         concep_info.sanitation * water_cost +
                                         concep_info.red_cross * water_cost +
                                         concep_info.firefighters * water_cost)
                                        
                # Generar pagina para cargar un nuevo adeudo inicial.
                new_debt = Debts(meter_number = user_meter_number,
                                 year = current_year,
                                 month = current_month,
                                 cut = 20,
                                 water_usage_m3 = round(random_water_usage, 3),
                                 previous_debt = 0,
                                 total_month = total_month_full)
                new_debt.save()
                return render(request, 'user_manage_payment_concept.html', {'user' : searched_user.first, 'debts' : Debts.objects.filter(meter_number=user_meter_number)})

                
            
    return render(request, 'manage_payment_concept.html', {'error': False})

def create_user(request):
    form = UserForm()
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
        else:
            messages.error(request, 'Numero de medidor ya existe.')
    context = {'form': form}
    return render(request, 'user_form.html', context)

def delete_user(request):
    if request.method == 'POST':
        user_meter_number = int(request.POST.get('meter_number', 0))
        searched_user = Users.objects.filter(meter_number=user_meter_number)
        if searched_user.exists():
            searched_user.delete()
            return redirect('home')
        else:
            messages.error(request, 'Numero de medidor no existe.')
    return render(request, 'delete.html', {'error': False})

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







from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .forms import SignUpForm, AddDriverForm, AddCarForm, AddVlForm, AddFCardForm, AddTripForm
from .models import Driver, Car, VL, FCard, Trip
from django.http import HttpResponse
import csv
import calendar
from calendar import HTMLCalendar
from datetime import datetime



'''
return render(request, 'home.html', {'cars':cars})
------------------------------------^^^^^^^^^^^^^^^
------------------------------------"context dictionary" passed to home.html

'''

def home(request, year=datetime.now().year, month=datetime.now().strftime('%B')):
	# Check to see if logging in
	if request.method == 'POST':
		username = request.POST['username']
		password = request.POST['password']
		# Authenticate
		user = authenticate(request, username=username, password=password)
		if user is not None:
			login(request, user)
			messages.success(request, "You Have Been Logged In!")
			return redirect('home')
		else:
			messages.success(request, "There Was An Error Logging In, Please Try Again...")
			return redirect('home')
	else:
		cars = Car.objects.all()
		drivers = Driver.objects.all()
		vls = VL.objects.all()
		fcards = FCard.objects.all()
  
		month = month.capitalize()
		# Convert month from name to number
		month_number = list(calendar.month_name).index(month)
		month_number = int(month_number)

		# create a calendar
		cal = HTMLCalendar().formatmonth(
			year, 
			month_number)
		# Get current year
		now = datetime.now()
		current_year = now.year

		# Get current time
		time = now.strftime('%H:%M ')
  
		due_car_list = Car.objects.filter(
			reg_due__year = year,
			reg_due__month = month_number
		)
 
		due_stairs_list = Car.objects.filter(
			stairs_due__year = year,
			stairs_due__month = month_number
		)

		due_lift_list = Car.objects.filter(
			lift_due__year = year,
			lift_due__month = month_number
		)
  
		due_tires_list = Car.objects.filter(
			tires_due__year = year,
			tires_due__month = month_number
		)

		due_fcards_list = FCard.objects.filter(
			exp_date__year = year,
			exp_date__month = month_number
		)
  
		return render(request, 
			'home.html', {'cars':cars ,'drivers':drivers ,'vls':vls, 'fcards':fcards,
			"year": year,
			"month": month,
			"month_number": month_number,
			"cal": cal,
			"current_year": current_year,
			"time":time,
			'due_car_list':due_car_list,
			'due_stairs_list':due_stairs_list,
			'due_lift_list':due_lift_list,
			'due_tires_list':due_tires_list,
		'due_fcards_list':due_fcards_list,
			})


def logout_user(request):
	logout(request)
	messages.success(request, "You Have Been Logged Out...")
	return redirect('home')


def register_user(request):
	if request.method == 'POST':
		form = SignUpForm(request.POST)
		if form.is_valid():
			form.save()
			# Authenticate and login
			username = form.cleaned_data['username']
			password = form.cleaned_data['password1']
			user = authenticate(username=username, password=password)
			login(request, user)
			messages.success(request, "You Have Successfully Registered! Welcome!")
			return redirect('home')
	else:
		form = SignUpForm()
		return render(request, 'register.html', {'form':form})

	return render(request, 'register.html', {'form':form})

def drivers(request):
	if request.user.is_authenticated:
		# Look Up Records
		drivers = Driver.objects.all()
		return render(request, 'drivers.html', {'drivers':drivers})
	else:
		messages.success(request, "You Must Be Logged In To View That Page...")
		return redirect('home')

def driver_record(request, pk):
	if request.user.is_authenticated:
		# Look Up Records
		driver_record = Driver.objects.get(id=pk)
		trips = Trip.objects.filter(driver=driver_record.id).order_by('-id')
		return render(request, 'driver.html', {'driver_record':driver_record ,'trips':trips})
	else:
		messages.success(request, "You Must Be Logged In To View That Page...")
		return redirect('home')


def delete_driver(request, pk):
	if request.user.is_authenticated:
		delete_it = Driver.objects.get(id=pk)
		delete_it.delete()
		messages.success(request, "Driver Deleted Successfully...")
		return redirect('drivers')
	else:
		messages.success(request, "You Must Be Logged In To Do That...")
		return redirect('home')


def add_driver(request):
	form = AddDriverForm(request.POST or None)
	if request.user.is_authenticated:
		if request.method == "POST":
			if form.is_valid():
				add_driver = form.save()
				messages.success(request, "Driver Added...")
				return redirect('drivers')
		return render(request, 'add_driver.html', {'form':form})
	else:
		messages.success(request, "You Must Be Logged In...")
		return redirect('home')


def update_driver(request, pk):
	if request.user.is_authenticated:
		current_driver = Driver.objects.get(id=pk)
		form = AddDriverForm(request.POST or None, instance=current_driver)
		if form.is_valid():
			form.save()
			messages.success(request, "Driver Has Been Updated!")
			return redirect('drivers')
		return render(request, 'update_driver.html', {'form':form})
	else:
		messages.success(request, "You Must Be Logged In...")
		return redirect('home')


#Car views
def cars(request):
	if request.user.is_authenticated:
		# Look Up Records
		cars = Car.objects.all()
		return render(request, 'cars.html', {'cars':cars})
	else:
		messages.success(request, "You Must Be Logged In To View That Page...")
		return redirect('home')

def car_record(request, pk):
	if request.user.is_authenticated:
		# Look Up Records
		car_record = Car.objects.get(id=pk)
		trips = Trip.objects.filter(car=car_record.id).order_by('-id')
		return render(request, 'car.html', {'car_record':car_record,'trips':trips})
	else:
		messages.success(request, "You Must Be Logged In To View That Page...")
		return redirect('home')



def delete_car(request, pk):
	if request.user.is_authenticated:
		delete_it = Car.objects.get(id=pk)
		delete_it.delete()
		messages.success(request, "Car Deleted Successfully...")
		return redirect('cars')
	else:
		messages.success(request, "You Must Be Logged In To Do That...")
		return redirect('home')


def add_car(request):
	form = AddCarForm(request.POST or None)
	if request.user.is_authenticated:
		if request.method == "POST":
			if form.is_valid():
				add_car = form.save()
				messages.success(request, "Car Added...")
				return redirect('cars')
		return render(request, 'add_car.html', {'form':form})
	else:
		messages.success(request, "You Must Be Logged In...")
		return redirect('home')


def update_car(request, pk):
	if request.user.is_authenticated:
		current_car = Car.objects.get(id=pk)
		form = AddCarForm(request.POST or None, instance=current_car)
		if form.is_valid():
			form.save()
			messages.success(request, "Car Has Been Updated!")
			return redirect('cars')
		return render(request, 'update_car.html', {'form':form})
	else:
		messages.success(request, "You Must Be Logged In...")
		return redirect('home')




#VL views

def vls(request):
	if request.user.is_authenticated:
		# Look Up Records
		vls = VL.objects.all()
		return render(request, 'vls.html', {'vls':vls})
	else:
		messages.success(request, "You Must Be Logged In To View That Page...")
		return redirect('home')

def vl_record(request, pk):
	if request.user.is_authenticated:
		# Look Up Records
		vl_record = VL.objects.get(id=pk)
		trips = Trip.objects.filter(vl=vl_record.id).order_by('-id')
		return render(request, 'vl.html', {'vl_record':vl_record,'trips':trips})
	else:
		messages.success(request, "You Must Be Logged In To View That Page...")
		return redirect('home')

def delete_vl(request, pk):
	if request.user.is_authenticated:
		delete_it = VL.objects.get(id=pk)
		delete_it.delete()
		messages.success(request, "VL Deleted Successfully...")
		return redirect('vls')
	else:
		messages.success(request, "You Must Be Logged In To Do That...")
		return redirect('home')


def add_vl(request):
	form = AddVlForm(request.POST or None)
	if request.user.is_authenticated:
		if request.method == "POST":
			if form.is_valid():
				add_vl = form.save()
				messages.success(request, "Car Added...")
				return redirect('vls')
		return render(request, 'add_vl.html', {'form':form})
	else:
		messages.success(request, "You Must Be Logged In...")
		return redirect('home')


def update_vl(request, pk):
	if request.user.is_authenticated:
		current_vl = VL.objects.get(id=pk)
		form = AddVlForm(request.POST or None, instance=current_vl)
		if form.is_valid():
			form.save()
			messages.success(request, "Car Has Been Updated!")
			return redirect('vls')
		return render(request, 'update_vl.html', {'form':form})
	else:
		messages.success(request, "You Must Be Logged In...")
		return redirect('home')



# Fuel Card Viewa
def fcards(request):
	if request.user.is_authenticated:
		# Look Up Records
		fcards = FCard.objects.all()
		return render(request, 'fcards.html', {'fcards':fcards})
	else:
		messages.success(request, "You Must Be Logged In To View That Page...")
		return redirect('home')

def fcard_record(request, pk):
	if request.user.is_authenticated:
		# Look Up Records
		fcard_record = FCard.objects.get(id=pk)
		return render(request, 'fcard.html', {'fcard_record':fcard_record})
	else:
		messages.success(request, "You Must Be Logged In To View That Page...")
		return redirect('home')

def delete_fcard(request, pk):
	if request.user.is_authenticated:
		delete_it = FCard.objects.get(id=pk)
		delete_it.delete()
		messages.success(request, "Fuel Card Deleted Successfully...")
		return redirect('fcards')
	else:
		messages.success(request, "You Must Be Logged In To Do That...")
		return redirect('home')


def add_fcard(request):
	form = AddFCardForm(request.POST or None)
	if request.user.is_authenticated:
		if request.method == "POST":
			if form.is_valid():
				add_fcard = form.save()
				messages.success(request, "Car Added...")
				return redirect('fcards')
		return render(request, 'add_fcard.html', {'form':form})
	else:
		messages.success(request, "You Must Be Logged In...")
		return redirect('home')


def update_fcard(request, pk):
	if request.user.is_authenticated:
		current_fcard = FCard.objects.get(id=pk)
		form = AddFCardForm(request.POST or None, instance=current_fcard)
		if form.is_valid():
			form.save()
			messages.success(request, "Fuel Card Has Been Updated!")
			return redirect('fcards')
		return render(request, 'update_fcard.html', {'form':form})
	else:
		messages.success(request, "You Must Be Logged In...")
		return redirect('home')


# Trip Viewa
def trips(request):
	if request.user.is_authenticated:
		# Look Up Records
		trips = Trip.objects.all().order_by('-id')
		return render(request, 'trips.html', {'trips':trips})
	else:
		messages.success(request, "You Must Be Logged In To View That Page...")
		return redirect('home')

def trip_record(request, pk):
	if request.user.is_authenticated:
		# Look Up Records
		trip_record = Trip.objects.get(id=pk)
		return render(request, 'trip.html', {'trip_record':trip_record})
	else:
		messages.success(request, "You Must Be Logged In To View That Page...")
		return redirect('home')

def delete_trip(request, pk):
	if request.user.is_authenticated:
		delete_it = Trip.objects.get(id=pk)
		delete_it.delete()
		messages.success(request, "Trip Deleted Successfully...")
		return redirect('trips')
	else:
		messages.success(request, "You Must Be Logged In To Do That...")
		return redirect('home')


def add_trip(request):
	form = AddTripForm(request.POST or None)
	if request.user.is_authenticated:
		if request.method == "POST":
			if form.is_valid():
				add_trip = form.save()
				messages.success(request, "Trip Added...")
				return redirect('trips')
		return render(request, 'add_trip.html', {'form':form})
	else:
		messages.success(request, "You Must Be Logged In...")
		return redirect('home')


def update_trip(request, pk):
	if request.user.is_authenticated:
		current_trip = Trip.objects.get(id=pk)
		form = AddTripForm(request.POST or None, instance=current_trip)
		if form.is_valid():
			form.save()
			messages.success(request, "Trip Has Been Updated!")
			return redirect('trips')
		return render(request, 'update_trip.html', {'form':form})
	else:
		messages.success(request, "You Must Be Logged In...")
		return redirect('home')


def trips_csv(request):
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename=all_trips.csv'
    #create csv writer
    writer = csv.writer(response)
    #designate The Model
    trips = Trip.objects.all()
    #add header to the csv file
    writer.writerow(['ID', 'Chauffør Navn', 'Bil Nr.', 'Fra(D)', 'Vl Nr.', 'Fra(T)', 'Til(D)', 'Til(T)', 'Betaling', 'Cash', 'Total', 'Aftaletype', 'Procent%', '%Indkomst', 'Timer', 'Pause', 'Betalte Timer', 'Udgifter', 'Udgifter Grund', 'Note'])
    #Loop through and output
    for trip in trips:
        writer.writerow([trip.id, trip.driver, trip.car, trip.fromd, trip.vl, trip.fromt, trip.tilld, trip.tillt, trip.income, trip.cash, trip.total, trip.p_type, trip.percent, trip.per_total, trip.work_time, trip.pause, trip.p_time, trip.expenses, trip.exp_reason, trip.note])
        
    return response

def dtrips_csv(request,pk):
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename=driver_trips.csv'
    #create csv writer
    writer = csv.writer(response)
    #designate The Model
    driver_record = Driver.objects.get(id=pk)
    trips = Trip.objects.filter(driver=driver_record.id)
    #add header to the csv file
    writer.writerow(['ID', 'Chauffør Navn', 'Bil Nr.', 'Fra(D)', 'Vl Nr.', 'Fra(T)', 'Til(D)', 'Til(T)', 'Betaling', 'Cash', 'Total', 'Aftaletype', 'Procent%', '%Indkomst', 'Timer', 'Pause', 'Betalte Timer', 'Udgifter', 'Udgifter Grund', 'Note'])
    #Loop through and output
    for trip in trips:
        writer.writerow([trip.id, trip.driver, trip.car, trip.fromd, trip.vl, trip.fromt, trip.tilld, trip.tillt, trip.income, trip.cash, trip.total, trip.p_type, trip.percent, trip.per_total, trip.work_time, trip.pause, trip.p_time, trip.expenses, trip.exp_reason, trip.note])
        
    return response

def ctrips_csv(request,pk):
	response = HttpResponse(content_type='text/csv')
	response['Content-Disposition'] = 'attachment; filename=car_trips.csv'
	#create csv writer
	writer = csv.writer(response)
	#designate The Model
	car_record = Car.objects.get(id=pk)
	trips = Trip.objects.filter(car=car_record.id).order_by('-id')
	#add header to the csv file
	writer.writerow(['ID', 'Chauffør Navn', 'Bil Nr.', 'Fra(D)', 'Vl Nr.', 'Fra(T)', 'Til(D)', 'Til(T)', 'Betaling', 'Cash', 'Total', 'Aftaletype', 'Procent%', '%Indkomst', 'Timer', 'Pause', 'Betalte Timer', 'Udgifter', 'Udgifter Grund', 'Note'])
	#Loop through and output
	for trip in trips:
		writer.writerow([trip.id, trip.driver, trip.car, trip.fromd, trip.vl, trip.fromt, trip.tilld, trip.tillt, trip.income, trip.cash, trip.total, trip.p_type, trip.percent, trip.per_total, trip.work_time, trip.pause, trip.p_time, trip.expenses, trip.exp_reason, trip.note])
        
	return response

def vtrips_csv(request,pk):
	response = HttpResponse(content_type='text/csv')
	response['Content-Disposition'] = 'attachment; filename=vl_trips.csv'
	#create csv writer
	writer = csv.writer(response)
	#designate The Model
	vl_record = VL.objects.get(id=pk)
	trips = Trip.objects.filter(vl=vl_record.id).order_by('-id')
	#add header to the csv file
	writer.writerow(['ID', 'Chauffør Navn', 'Bil Nr.', 'Fra(D)', 'Vl Nr.', 'Fra(T)', 'Til(D)', 'Til(T)', 'Betaling', 'Cash', 'Total', 'Aftaletype', 'Procent%', '%Indkomst', 'Timer', 'Pause', 'Betalte Timer', 'Udgifter', 'Udgifter Grund', 'Note'])
	#Loop through and output
	for trip in trips:
		writer.writerow([trip.id, trip.driver, trip.car, trip.fromd, trip.vl, trip.fromt, trip.tilld, trip.tillt, trip.income, trip.cash, trip.total, trip.p_type, trip.percent, trip.per_total, trip.work_time, trip.pause, trip.p_time, trip.expenses, trip.exp_reason, trip.note])
        
	return response





    
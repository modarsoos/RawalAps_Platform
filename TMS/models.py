from django.db import models
from datetime import datetime, time

class FCard(models.Model):
	fcnr = models.CharField(max_length=25)
	lastdigits = models.CharField(max_length=8)
	FCTYPE_CHOICES = [
        ("60", "60"),
        ("61", "61"),
        ("61", "62"),
        ("61", "63"),
        ("61", "64"),
        ("61", "65"),
    ]
	fctype = models.CharField(choices=FCTYPE_CHOICES,default="63",blank=True,null=True,max_length=5)
	exp_date = models.DateField(blank=True,null=True,)
	is_active = models.BooleanField()
	created_at = models.DateTimeField(auto_now_add=True)

	def __str__(self):
		return(f"{self.lastdigits}")

class Driver(models.Model):
	fname = models.CharField(max_length=25)
	lname =  models.CharField(max_length=25)
	short = models.CharField(max_length=25)
	mobile = models.CharField(max_length=15)
	email =  models.EmailField(max_length=50)
	cpr = models.CharField(max_length=15)
	address = models.CharField(max_length=100)
	bank_reg = models.CharField(max_length=10)
	bank_account = models.CharField(max_length=20)
	POSITION_CHOICES = [
        ("Chauffør", "Chauffør"),
        ("Assistent", "Assistent"),
    ]
	position = models.CharField(choices=POSITION_CHOICES,default="Chauffør",max_length=15) #DDL Lookup
	fcard = models.ForeignKey(FCard,blank=True,null=True,max_length=10,on_delete=models.DO_NOTHING) #DDL
	start = models.DateField(blank=True, null=True)
	end = models.DateField(blank=True,null=True)
	is_active = models.BooleanField()
	created_at = models.DateTimeField(auto_now_add=True)

	def __str__(self):
		return(f"{self.short}")


class Car(models.Model):
	make = models.CharField(max_length=15)
	model =  models.CharField(max_length=15)
	YEAR_CHOICES = [
		("19", "2019"),
		("20", "2020"),
		("21", "2021"),
		("22", "2022"),
		("23", "2023"),
		("24", "2024"),
		("25", "2025"),
		("26", "2026"),
		("27", "2027"),
		("28", "2028"),
		("29", "2029"),  
		("30", "2030"),  
	]
	year =  models.CharField(choices=YEAR_CHOICES,default="23",max_length=15)
	short =  models.CharField(max_length=20)
	plate =  models.CharField(max_length=20)
	SIZE_CHOICES = [
		("Stor", "Stor"),
		("Mellem", "Mellem"),
		("Lille", "Lille"),  
	]
	size =  models.CharField(choices=SIZE_CHOICES,default="Lille",blank=True,null=True,max_length=10)
	mobile =  models.CharField(blank=True,null=True,max_length=10)
	reg_nr =  models.CharField(blank=True,null=True,max_length=10)
	reg_first =  models.DateField(blank=True,null=True,)
	reg_due =  models.DateField(blank=True,null=True,)
	stairs_due =  models.DateField(blank=True,null=True,)
	lift_due =  models.DateField(blank=True,null=True,)
	tires_due =  models.DateField(blank=True,null=True,)
	fcard = models.ForeignKey(FCard,blank=True,null=True,max_length=10,on_delete=models.DO_NOTHING) #DDL
	created_at = models.DateTimeField(auto_now_add=True)

	def __str__(self):
		return(f"{self.plate}")

class VL(models.Model):
	vlnr = models.CharField(max_length=8)
	TYPE_CHOICES = [
		("1", "1"),
		("2", "2"),
		("3", "3"),
		("4", "4"),
		("5", "5"),
		("6", "6"),
		("7", "7"),
		("8", "8"),
		("9", "9"), 
		("10", "10"), 
	]	
	vltype = models.CharField(choices=TYPE_CHOICES,default="5",blank=True,null=True,max_length=8)	
	vlid = models.CharField(blank=True,null=True,max_length=8)
	vladdress = models.CharField(blank=True,null=True,max_length=100)
	is_active = models.BooleanField()
	created_at = models.DateTimeField(auto_now_add=True)

	def __str__(self):
		return(f"{self.vlnr}")



class Trip(models.Model):
	driver = models.ForeignKey(Driver,blank=True,null=True,max_length=25,on_delete=models.DO_NOTHING)
	vl = models.ForeignKey(VL,blank=True,null=True,max_length=8, on_delete=models.DO_NOTHING)
	car = models.ForeignKey(Car,blank=True,null=True,max_length=10, on_delete=models.DO_NOTHING)
	income = models.DecimalField(blank=True,null=True,max_digits=6, decimal_places=2)
	cash = models.DecimalField(blank=True,null=True,max_digits=6, decimal_places=2)
	total = models.DecimalField(blank=True,null=True,max_digits=6, decimal_places=2)
	PAYMENT_TYPE_CHOICES = [
     	("Pro%", "Pro%"),
		("Tid", "Tid"),
	]
	p_type = models.CharField(choices=PAYMENT_TYPE_CHOICES,default="Pro%",blank=True,null=True,max_length=5)
	PERCENT_CHOICES = [
		(48, 48),
		(49, 49),
  		(50, 50),
		(51, 51),
  		(52, 52),
		(53, 53),
  		(54, 54),
		(55, 55),
	]
	percent = models.IntegerField(choices=PERCENT_CHOICES,default="48",blank=True,null=True)
	per_total = models.DecimalField(blank=True,null=True,max_digits=6, decimal_places=2)
	fromd = models.DateField(blank=True,null=True)
	fromt = models.TimeField(blank=True,null=True,default="00:00")
	tilld = models.DateField(blank=True,null=True)
	tillt = models.TimeField(blank=True,null=True,default="00:00")
	work_time = models.DurationField(blank=True,null=True,)	
	pause = models.DurationField(blank=True,null=True,default="00:00")
	p_time = models.DurationField(blank=True,null=True,)
	expenses = models.DecimalField(blank=True,null=True,max_digits=6, decimal_places=2)
	exp_reason = models.CharField(blank=True,null=True,max_length=100)
	note = models.CharField(blank=True,null=True,max_length=100)
	created_at = models.DateTimeField(auto_now_add=True)


	def __str__(self):
		return(f"{self.driver} - {self.car} - {self.vl} | {self.fromd} | {self.work_time}")


    
    
	
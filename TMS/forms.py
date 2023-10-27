from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from django.forms import ModelForm
from .models import Driver, Car, VL, FCard, Trip
import datetime



class SignUpForm(UserCreationForm):
	email = forms.EmailField(label="", widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Email Address'}))
	first_name = forms.CharField(label="", max_length=100, widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'First Name'}))
	last_name = forms.CharField(label="", max_length=100, widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Last Name'}))


	class Meta:
		model = User
		fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2')


	def __init__(self, *args, **kwargs):
		super(SignUpForm, self).__init__(*args, **kwargs)

		self.fields['username'].widget.attrs['class'] = 'form-control'
		self.fields['username'].widget.attrs['placeholder'] = 'User Name'
		self.fields['username'].label = ''
		self.fields['username'].help_text = '<span class="form-text text-muted"><small>Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.</small></span>'

		self.fields['password1'].widget.attrs['class'] = 'form-control'
		self.fields['password1'].widget.attrs['placeholder'] = 'Password'
		self.fields['password1'].label = ''
		self.fields['password1'].help_text = '<ul class="form-text text-muted small"><li>Your password can\'t be too similar to your other personal information.</li><li>Your password must contain at least 8 characters.</li><li>Your password can\'t be a commonly used password.</li><li>Your password can\'t be entirely numeric.</li></ul>'

		self.fields['password2'].widget.attrs['class'] = 'form-control'
		self.fields['password2'].widget.attrs['placeholder'] = 'Confirm Password'
		self.fields['password2'].label = ''
		self.fields['password2'].help_text = '<span class="form-text text-muted"><small>Enter the same password as before, for verification.</small></span>'	


# Create Add Driver Form
class AddDriverForm(forms.ModelForm):
	fname = forms.CharField(required=True, widget=forms.TextInput(attrs={"placeholder":"First Name"}), label="First Name")
	lname = forms.CharField(required=True, widget=forms.TextInput(attrs={"placeholder":"Last Name"}), label="Last Name")
	short = forms.CharField(required=True, widget=forms.TextInput(attrs={"placeholder":"Short Name"}), label="Short Name")
	mobile = forms.CharField(required=False, widget=forms.TextInput(attrs={"placeholder":"Mobile"}), label="Mobile")
	email = forms.EmailField(required=False, widget=forms.TextInput(attrs={"placeholder":"Email"}), label="Email")
	cpr = forms.CharField(required=False, widget=forms.TextInput(attrs={"placeholder":"CPR. No."}), label="CPR. No.")
	address = forms.CharField(required=False, widget=forms.TextInput(attrs={"placeholder":"Address"}), label="Address")
	bank_reg = forms.CharField(required=False, widget=forms.TextInput(attrs={"placeholder":"Bank Reg."}), label="Bank Reg.")
	bank_account = forms.CharField(required=False, widget=forms.TextInput(attrs={"placeholder":"Bank Account"}), label="Bank Account")
	start = forms.DateField(required=False, widget=forms.TextInput(attrs={'type': 'date'}), label="Start Date")
	end = forms.DateField(required=False, widget=forms.TextInput(attrs={'type': 'date'}), label="End Date")
	is_active = forms.BooleanField(required=False)

	class Meta:
		model = Driver
		exclude = ("user",)

# Create Add Car Form
class AddCarForm(forms.ModelForm):
	make = forms.CharField(required=True, widget=forms.TextInput(attrs={"placeholder":"Make"}), label="Make")
	model = forms.CharField(required=True, widget=forms.TextInput(attrs={"placeholder":"Model"}), label="Model")
	short = forms.CharField(required=False, widget=forms.TextInput(attrs={"placeholder":"Short"}), label="Short")
	plate = forms.CharField(required=False, widget=forms.TextInput(attrs={"placeholder":"Plate No."}), label="Plate No.")
	mobile = forms.CharField(required=False, widget=forms.TextInput(attrs={"placeholder":"Mobile"}), label="Mobile")
	reg_nr = forms.CharField(required=False, widget=forms.TextInput(attrs={"placeholder":"Reg. No."}), label="Reg. No.")
	reg_first = forms.DateField(required=False, widget=forms.TextInput(attrs={'type': 'date',"placeholder":"1st Reg."}), label="1st Reg.")
	reg_due = forms.DateField(required=False, widget=forms.TextInput(attrs={'type': 'date',"placeholder":"Reg. due"}), label="Reg. due")
	stairs_due = forms.DateField(required=False, widget=forms.TextInput(attrs={'type': 'date',"placeholder":"Stairs due"}), label="Stairs due")
	lift_due = forms.DateField(required=False, widget=forms.TextInput(attrs={'type': 'date',"placeholder":"Lift due"}), label="Lift due")
	tires_due = forms.DateField(required=False, widget=forms.TextInput(attrs={'type': 'date',"placeholder":"Tires due"}), label="Tires due")


	class Meta:
		model = Car
		exclude = ("user",)
  
# Create Add VL Form
class AddVlForm(forms.ModelForm):
	vlnr = forms.CharField(required=True, widget=forms.TextInput(attrs={"placeholder":"VL No."}), label="VL No.")
	vlid = forms.CharField(required=True, widget=forms.TextInput(attrs={"placeholder":"VL Sys. ID."}), label="VL Sys. ID")
	vladdress = forms.CharField(required=True, widget=forms.TextInput(attrs={"placeholder":"VL address"}), label="VL address")
	is_active = forms.BooleanField(required=False)

	class Meta:
		model = VL
		exclude = ("user",)

# Create Add FCard Form
class AddFCardForm(forms.ModelForm):
	fcnr = forms.CharField(required=True, widget=forms.TextInput(attrs={"placeholder":"Fuel Card No."}), label="Fuel Card No.")
	lastdigits = forms.CharField(required=True, widget=forms.TextInput(attrs={"placeholder":"Last Digits"}), label="Last Digits of F. Card")
	exp_date = forms.DateField(required=True, widget=forms.TextInput(attrs={'type': 'date'}), label="Expiry Date")
	is_active = forms.BooleanField()

	class Meta:
		model = FCard
		exclude = ("user",)
  
# Create add Trip Form
class AddTripForm(forms.ModelForm):
	driver = forms.ModelChoiceField(required=True, queryset = Driver.objects.all()) #to use select
	vl = forms.ModelChoiceField(queryset = VL.objects.all())
	car = forms.ModelChoiceField(queryset = Car.objects.all())
	income = forms.DecimalField(max_digits=6, decimal_places=2, required=True,initial="00.00")
	cash = forms.DecimalField(max_digits=6, decimal_places=2,required=True,initial="00.00")
	total = forms.DecimalField(max_digits=6, decimal_places=2,required=True,initial="00.00")
	per_total = forms.DecimalField(max_digits=6, decimal_places=2,required=False,initial="00.00")
	fromd = forms.DateField(required=False,initial=datetime.date.today, widget=forms.DateInput(attrs={'type': 'date'}))
	fromt = forms.TimeField(required=False, widget=forms.TimeInput(attrs={'type': 'time'}),initial="00:00")
	tilld = forms.DateField(required=False,initial=datetime.date.today, widget=forms.DateInput(attrs={'type': 'date'}))
	tillt = forms.TimeField(required=False, widget=forms.TimeInput(attrs={'type': 'time'}),initial="00:00")
	work_time = forms.DurationField(required=False,initial="00:00", widget=forms.TimeInput(attrs={"placeholder":"Work Time"}))
	pause = forms.DurationField(required=False,initial="00:00", widget=forms.TimeInput(attrs={'type': 'time'}))
	p_time = forms.DurationField(required=False,initial="00:00", widget=forms.TimeInput(attrs={'type': 'time'}))
	expenses = forms.DecimalField(max_digits=6, decimal_places=2,required=True,initial="00.00")
	exp_reason = forms.CharField(required=False, widget=forms.Textarea(attrs={"placeholder":"exp_reason",'rows':1}))
	note = forms.CharField(required=False, widget=forms.Textarea(attrs={"placeholder":"Note",'rows':3}))

	class Meta:
		model = Trip
		exclude = ("user",)
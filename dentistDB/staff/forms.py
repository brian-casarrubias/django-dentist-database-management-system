from django import forms
from django.contrib.auth.models import User
from staff.models import *
from django.contrib.auth.forms import UserCreationForm





class StaffRegisterForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User

        fields = [
            'username',
            'email',
            'password1',
            'password2',
        ]
       


class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField()

    class Meta:
        model = User

        fields = [
            'username',
            'email',
        ]

class StaffUpdateForm(forms.ModelForm):
    class Meta:
        model = Staff
        

        fields = [
            'first_name',
            'last_name',
            'phone_number',
            'age',
        ]





class DentistRegisterForm(forms.ModelForm):

    class Meta:
            
        model = Dentist

        fields = [
            'first_name',
            'last_name',
            'email',
            'phone_number',
            'age',

        ]
		



class PatientRegisterForm(forms.ModelForm):

    class Meta:
            
        model = Patient

        fields = [
            'first_name',
            'last_name',
            'email',
            'race',
            'gender',
            'phone_number',
            'age',
            'adress',

        ]

class AppointmentRegisterForm(forms.ModelForm):
    


    class Meta:
            
        model = Appointment

        fields = [
            'patient',
            'dentist',
            'title',
            'content',
            'appointment_date',
            'appointment_time'
            
          

        ]
        widgets = {
            'appointment_date': forms.DateInput(attrs={'type': 'date'}),
            'appointment_time': forms.TimeInput(attrs={'type': 'time'}),
        }


		
		
		
		
		
		
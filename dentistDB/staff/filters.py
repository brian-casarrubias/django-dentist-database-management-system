import django_filters
from .models import *

class PatientFilter(django_filters.FilterSet):
    
    class Meta:
        model = Patient

        fields = {
                'first_name':['icontains'],
                'last_name':['icontains'],
        }



class AppointmentFilter(django_filters.FilterSet):
    class Meta:
        model = Appointment
        fields = {
            'title':['icontains'],
            'appointment_date': ['exact'],
            
        }
from django.db import models
from django.contrib.auth.models import User
import uuid
from django.urls import reverse

RACE_OPTIONS = (
    ('American Indian or Alasa Native', 'American Indian or Alasa Native'),
    ('Asian','Asian'),
    ('Black or African American', 'Black or African American'),
    ('Hispanic or Latino','Hispanic or Latino'),
    ('Native Hawaiian or Other Pacific islander', 'Native Hawaiian or Other Pacific islander'),
    ('White','White'),
)
GENDER = (
    ('Male', 'Male'),
    ('Female', 'Female'),
    ('Other', 'Other'),
)

class Patient(models.Model):
    first_name = models.CharField(max_length=100, null=True, blank=False)
    last_name = models.CharField(max_length=100, null=True, blank=False)
    email = models.CharField(max_length=150, null=True, blank=False)
    race = models.CharField(choices=RACE_OPTIONS, null=True, blank=False, max_length=50)
    gender = models.CharField(choices=GENDER, null=True, blank=False, max_length=10)
    phone_number = models.CharField(max_length=100, null=True, blank=False, help_text='eg 240-281-2912')
    age = models.IntegerField(null=True, blank=False)
    adress = models.CharField(max_length=200, null=True, blank=False)


    def __str__(self):
        return f'{self.first_name} {self.last_name}'
    
    def get_absolute_url(self):
        return reverse('patient-detail-page', kwargs={'pk':self.pk})

    
class Staff(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=100, null=True, blank=True)
    last_name = models.CharField(max_length=100, null=True, blank=True)
    email = models.CharField(max_length=150, null=True, blank=False)
    phone_number = models.CharField(max_length=100, null=True, blank=False, help_text='eg 240-281-2912')
    age = models.IntegerField(max_length=100,  null=True, blank=False,  help_text='eg.  248-293-2984')
    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)


    def __str__(self):
        return self.user.username

    
class Dentist(models.Model):
    first_name = models.CharField(max_length=100, null=True, blank=True)
    last_name = models.CharField(max_length=100, null=True, blank=True)
    email = models.CharField(max_length=150, null=True, blank=False)
    phone_number = models.CharField(max_length=100, null=True, blank=False, help_text='eg 240-281-2912')
    age = models.IntegerField(max_length=100,  null=True, blank=False,  help_text='eg.  248-293-2984')
    
    def __str__(self):
        return f'{self.first_name} {self.last_name}'
    
    def get_absolute_url(self):
        return reverse('dentist-detail-page', kwargs={'pk':self.pk})
    

    

class Appointment(models.Model):
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    dentist = models.ForeignKey(Dentist, on_delete=models.DO_NOTHING)
    title = models.CharField(max_length=200, null=True, blank=False)
    content = models.CharField(max_length=500, null=True, blank=False)
    appointment_date = models.DateTimeField(null=True, blank=False)
    appointment_time = models.TimeField(null=True, blank=False)
    # image = models.ImageField(default='default.jpg', upload_to='profile_pics', null=True, blank=True)  
    
    def __str__(self):
        return f'{self.title} {self.content}'
    
    def get_absolute_url(self):
        return reverse('appointment-detail-page', kwargs={'pk':self.pk})

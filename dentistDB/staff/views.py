from typing import Any
from django.db.models.query import QuerySet
from django.shortcuts import render, redirect,get_object_or_404
from django.http import HttpResponse
from staff.forms import *
from django.contrib import messages
from . models import *
from . filters import *
from django.contrib.auth.decorators import login_required
from django.views.generic import ListView, DetailView, DeleteView, UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
# Create your views here.

SECRET_CODE = 321
def home(request):
    return render(request, 'staff/index.html')

def about(request):
     return render(request, 'staff/about.html')

def contact(request):
     if request.method == 'POST':
          name = request.POST.get('name', None)
          email = request.POST.get('email', None)
          message = request.POST.get('message', None)

          print(f'Contact Form Message: \n \n Name: {name} \n Email {email} \n Message: {message}')

     return render(request, 'staff/contact.html')

def location(request):
     return render(request, 'staff/location.html')


def register(request):
    if request.method == 'POST':
        value = int(request.POST.get('code', None))
        if value == SECRET_CODE:
            form = StaffRegisterForm(request.POST)
            
            

            if form.is_valid():
                form.save()
                messages.success(request, 'Account Successfully Created!')
                return redirect('login-page')
            else:
                messages.error(request, 'Error, account not created!')
                return redirect('home-page')
        else:
            messages.error(request, 'Error, code not valid!')
            return redirect('home-page')

    else:
        form = StaffRegisterForm()

    context = {
        'form':form
    }

    return render(request, 'staff/register.html', context)



@login_required
def dashboard(request):
    patient = Patient.objects.all()
    dentist = Dentist.objects.all()
    appointment = Appointment.objects.all()

    context = {
        'patient':patient,
        'dentist':dentist,
        'appointment':appointment,
    }
    return render(request, 'staff/dashboard.html', context)



@login_required
def account(request, pk):

  
    
    if request.method == 'POST':
        u_form = UserUpdateForm(request.POST, instance=request.user)
        s_form = StaffUpdateForm(request.POST, instance=request.user.staff)

        if u_form.is_valid() and s_form.is_valid():
            u_form.save()
            s_form.save()
            print('should have saved')
            messages.success(request, 'Successfully Updated Account!')
            return redirect('dashboard-page')
    else:


        u_form = UserUpdateForm(instance=request.user)
        s_form = StaffUpdateForm(instance=request.user.staff)

    context = {
        'u_form':u_form,
        's_form':s_form,
       
    }
   
   

    return render(request, 'staff/account.html', context)






@login_required
def registerDentist(request):
   
    if request.method == 'POST':
        form = DentistRegisterForm(request.POST)

        if form.is_valid():
            form.save()
            messages.success(request, 'Dentist successfully added to Database!')
            return redirect('dashboard-page')
        else:
                messages.success(request, 'Error, something went wrong!')
                return redirect('dashboard-page')
        
    else:
        form = DentistRegisterForm(request.POST)


        context = {
            'form':form,
        }
           
   
    return render(request, 'staff/dentist-register.html', context)


class ViewDentist(LoginRequiredMixin, ListView):
    model = Dentist
    template_name = 'staff/dentist-list.html'
    context_object_name = 'dentists'
    ordering =['last_name']

         
    

class DentistDetailedView(LoginRequiredMixin, DetailView):
        model = Dentist
        template_name = 'staff/dentist-detail.html'
       


class DentistUpdateView(LoginRequiredMixin, UpdateView):
     model = Dentist
     template_name = 'staff/dentist-update.html'
     fields = [
          'first_name',
          'last_name',
          'email',
          'phone_number',
          'age',
     ]



class DentistDeleteView(LoginRequiredMixin,DeleteView):
     model = Dentist
     template_name = 'staff/dentist-delete.html'

     success_url = reverse_lazy('dentist-list-page')




@login_required
def registerPatient(request):
   
    if request.method == 'POST':
        form = PatientRegisterForm(request.POST)

        if form.is_valid():
            form.save()
            messages.success(request, 'Patient successfully added to Database!')
            return redirect('dashboard-page')
        else:
                messages.success(request, 'Error, something went wrong!')
                return redirect('dashboard-page')
        
    else:
        form = PatientRegisterForm(request.POST)


        context = {
            'form':form,
        }
           
   
    return render(request, 'staff/patient-register.html', context)



class ViewPatient(LoginRequiredMixin, ListView):
    model = Patient
    template_name = 'staff/patient-list.html'
    context_object_name = 'patients'
    ordering=['last_name']
   
   
    
    
    def get_queryset(self):
        queryset = super().get_queryset()
        filter = PatientFilter(self.request.GET, queryset=queryset)
        return filter.qs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['filter'] = PatientFilter(self.request.GET, queryset=self.get_queryset())
        return context



class PatientDetailedView(LoginRequiredMixin, DetailView):
        model = Patient
        template_name = 'staff/patient-detail.html'



class PatientUpdateView(LoginRequiredMixin,  UpdateView):
     model = Patient
     template_name = 'staff/patient-update.html'
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



class PatientDeleteView(LoginRequiredMixin,DeleteView):
     model = Patient
     template_name = 'staff/patient-delete.html'

     success_url = reverse_lazy('patient-list-page')







@login_required
def registerAppointment(request):
   
    if request.method == 'POST':
       
        form = AppointmentRegisterForm(request.POST)

        if form.is_valid():
            form.save()
            messages.success(request, 'Appointment successfully added to Database!')
            return redirect('dashboard-page')
        else:
                messages.success(request, 'Error, something went wrong!')
                return redirect('dashboard-page')
        
    else:
        form = AppointmentRegisterForm(request.POST)


        context = {
            'form':form,
            
        }
           
   
    return render(request, 'staff/appointment-register.html', context)

class ViewAppointment(LoginRequiredMixin, ListView):
    model = Appointment
    template_name = 'staff/appointment-list.html'
    context_object_name = 'appointments'
    paginate_by = 10
    
    
    
    def get_queryset(self):
        queryset = super().get_queryset()
        filter = AppointmentFilter(self.request.GET, queryset=queryset)
        return filter.qs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['filter'] = AppointmentFilter(self.request.GET, queryset=self.get_queryset())
        return context




class AppointmentDetailedView(LoginRequiredMixin, DetailView):
        model = Appointment
        template_name = 'staff/appointment-detail.html'

        

class AppointmentUpdateView(LoginRequiredMixin, UpdateView):
     model = Appointment
     template_name = 'staff/appointment-update.html'
     fields = [
          'patient',
          'dentist',
          'title',
          'content',
          'appointment_date',
          'appointment_time',
         
     ]

     

class AppointmentDeleteView(LoginRequiredMixin,DeleteView):
     model = Appointment
     template_name = 'staff/appointment-delete.html'

     success_url = reverse_lazy('appointment-list-page')

    
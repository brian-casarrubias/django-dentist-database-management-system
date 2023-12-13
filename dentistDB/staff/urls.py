
from django.urls import path
from . import views


urlpatterns = [
   path('', views.home, name='home-page'),
   path('dashboard/', views.dashboard, name='dashboard-page'),
   path('account/<uuid:pk>/', views.account, name='account-page'),

   path('register-dentist/', views.registerDentist, name='dentist-register-page'),
   path('view-dentist-list/', views.ViewDentist.as_view(), name='dentist-list-page'),
   path('view-dentist/<int:pk>/', views.DentistDetailedView.as_view(), name='dentist-detail-page'),
   path('update-dentist/<int:pk>/', views.DentistUpdateView.as_view(), name='dentist-update-page'),
   path('delete-dentist/<int:pk>/', views.DentistDeleteView.as_view(), name='dentist-delete-page'),


   path('register-patient/', views.registerPatient, name='patient-register-page'),
   path('view-patient-list/', views.ViewPatient.as_view(), name='patient-list-page'),
   path('view-patient/<int:pk>/', views.PatientDetailedView.as_view(), name='patient-detail-page'),
   path('update-patient/<int:pk>/', views.PatientUpdateView.as_view(), name='patient-update-page'),
   path('delete-patient/<int:pk>/', views.PatientDeleteView.as_view(), name='patient-delete-page'),


   path('register-appointment/', views.registerAppointment, name='appointment-register-page'),
   path('view-appointment-list/', views.ViewAppointment.as_view(), name='appointment-list-page'),
   path('view-appointment/<int:pk>/', views.AppointmentDetailedView.as_view(), name='appointment-detail-page'),
   path('update-appointment/<int:pk>/', views.AppointmentUpdateView.as_view(), name='appointment-update-page'),
   path('delete-appointment/<int:pk>/', views.AppointmentDeleteView.as_view(), name='appointment-delete-page'),
   
]

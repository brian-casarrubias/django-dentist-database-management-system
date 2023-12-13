from django.contrib import admin

from staff.models import *


# Register your models here.


admin.site.register(Patient)
admin.site.register(Staff)
admin.site.register(Dentist)
admin.site.register(Appointment)
from django.contrib import admin
from .models import sector, crime, victim, offender

admin.site.register(sector)
admin.site.register(crime)
admin.site.register(victim)
admin.site.register(offender)


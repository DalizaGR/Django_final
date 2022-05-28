from pickle import TRUE
from unicodedata import name
from django.db import models

# Create your models here.
from django.utils.translation import gettext_lazy as _
from django.conf import settings
from django.utils import timezone


class sector(models.Model):
		sector = models.AutoField(primary_key=True)
		title = models.CharField(max_length=200)
		before = models.ImageField(blank=True, upload_to='images/')
		after = models.ImageField(blank=True, upload_to='images/')
	
		def __str__(self):
			return self.title	

class crime(models.Model):
		class CrimeType(models.TextChoices):
			MURDERED = 'Asesinato', _('Asesinato')
			STOLE = 'Robo', _('Robo')

		id = models.AutoField(primary_key=True)
		title = models.CharField(max_length=200)
		crime_type = models.CharField(
        max_length = 10,
				choices = CrimeType.choices,
				default = CrimeType.MURDERED,
		)
		text = models.TextField()
		event_date = models.DateTimeField(default=timezone.now)
		reasons = models.TextField(blank=True)
		sector = models.ForeignKey(sector, on_delete=models.CASCADE)

		def __str__(self):
		    return self.title


class victim(models.Model):
		id_crimes = models.ForeignKey(crime, on_delete=models.CASCADE)
		victim = models.AutoField(primary_key=True)
		name = models.CharField(max_length=40)
		year = models.IntegerField()
		detail= models.TextField(blank=True)
		img = models.ImageField(blank=True, upload_to='images/') 

		def __str__(self):
			return self.name
	

class offender(models.Model):
		crimes= models.ForeignKey(crime, on_delete=models.CASCADE)
		offender = models.AutoField(primary_key=True)
		name = models.CharField(max_length=40)
		year = models.IntegerField()
		detail= models.TextField(blank=True)
		img = models.ImageField(blank=True, upload_to='images/') 
		
		def __str__(self):
			return self.name
	

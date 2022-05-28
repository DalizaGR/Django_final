from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from .models import  sector, crime, victim, offender
from django.db.models import Prefetch
#from .forms import PostForm

def post_list(request):
    posts = crime.objects.filter(event_date__lte=timezone.now()).order_by('-event_date')
    return render(request, 'blog/Home.html', {'posts': posts})

def victim_list(request):
	#victims = victim.objects.all().order_by('-victim')
	victims = victim.objects.raw("SELECT b.victim,b.name,b.year ,b.detail,b.img,a.id FROM informes_crime  AS a left JOIN informes_victim AS b  group by b.victim")
	return render(request, 'blog/Victimas.html', {'victimas': victims})

def offender_list(request):
	offende = offender.objects.raw("SELECT b.*,a.id FROM informes_crime  AS a left JOIN informes_offender AS b  group by b.offender")
	return render(request, 'blog/Criminales.html', {'Criminales': offende})

def sector_list(request):
	Sectores = sector.objects.all()
	return render(request, 'blog/sectores.html', {'Sectores': Sectores})

def sector_Crimen(request, pk):
	Sector = sector.objects.filter(sector=pk).only('title')
	Crimines = crime.objects.filter(sector=pk).order_by('-event_date')
	return render(request, 'blog/crimenes_sector.html', {'Crimines': Crimines, 'Sector': Sector})

def victims_Crimen(request, pk):
		Crimen = crime.objects.filter(id=pk).order_by('-event_date')
		Victima = victim.objects.filter(id_crimes=pk).order_by('-victim')
		Criminales = offender.objects.filter(crimes=pk).order_by('-offender')
		return render(request, 'blog/crimen.html', {'Crimenes': Crimen, "victimas": Victima, "Criminales": Criminales })

def list_asesintos(request):
	Crimen = crime.objects.filter(crime_type="Asesinato").order_by('-event_date')
	return render(request, 'blog/asesinatos.html', {'Crimenes': Crimen})

def list_robos(request):
	Crimen = crime.objects.filter(crime_type="Robo").order_by('-event_date')
	return render(request, 'blog/robos.html', {'Crimenes': Crimen})
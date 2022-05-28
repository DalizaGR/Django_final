from django.urls import path
from . import views


urlpatterns = [
  path('', views.post_list, name='Lista de Crimenes'),
	path('Robos/',views.list_robos,name='Robos'),
	path('Asesinatos/',views.list_asesintos,name='Asesinatos'),
	path('victimas', views.victim_list, name='Victimas'),
	path('criminales', views.offender_list, name='crimnales'),
	path('sectores', views.sector_list, name='Sectores'),
	path('Crimen/<int:pk>/', views.victims_Crimen, name='Crimen'),
	path('Crimen_sector/<int:pk>/', views.sector_Crimen, name='Crimen_Sector'),
]

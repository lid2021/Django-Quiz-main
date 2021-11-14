from django.urls import path
from django.conf.urls import url  
from django.contrib import admin




from .views import (
			inicio, 
			portada,
			loginView, 
			registro, 
			logout_vista,
			HomeUsuario, 
			jugar,
			resultado_pregunta,
			tablero,
			grupo3,
			reglamento,
			)

urlpatterns = [
	
	path('', inicio, name='inicio'),
	path('portada/', portada, name='portada'),
	path('login/', loginView, name='login'),
	path('registro/', registro, name='registro'),
	path('HomeUsuario/', HomeUsuario, name='HomeUsuario'),
	path('logout_vista/', logout_vista, name='logout_vista'),
	path('tablero/', tablero, name='tablero'),
	path('jugar/', jugar, name='jugar'),
	path('resultado/<int:pregunta_respondida_pk>/', resultado_pregunta, name='resultado'),
    path('grupo3/', grupo3, name='grupo3'),
	path('reglamento/', reglamento, name='reglamento'),

]



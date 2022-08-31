from django.urls import path,include
from . import views
from django.contrib.auth import views as auth_views
from django.contrib.auth.views import logout_then_login







urlpatterns = [

	path("agregar/",views.agregar,name="agregar"),

	path("eliminar/<int:tarea_id>/",views.eliminar, name="eliminar"),

	path("editar/<int:tarea_id>/",views.editar,name="editar"),

	path('accounts', include('django.contrib.auth.urls')),

	path('logout/',logout_then_login,name='logout'),
	


	

]



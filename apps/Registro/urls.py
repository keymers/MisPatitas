from django.urls import path, include
from . import views
from rest_framework.urlpatterns import format_suffix_patterns
from apps.Registro import views

urlpatterns = [

    # listar las clientes de la bd
    path('listarClientes', views.listar_clientes, name="listar_clientes"),
        
    # agregar una cliente    
    path('agregar_cliente', views.agregar_cliente, name="agregar_cliente"),

    # editar una cliente
    path('editar_cliente/<int:cliente_id>', views.editar_cliente ,name="editar_cliente"),

    # borrar una cliente
    path('borrar_cliente/<int:cliente_id>', views.borrar_cliente, name="borrar_cliente"),

    path('api/', views.API_objects.as_view()),
    path('api/<int:pk>/', views.API_objects_details.as_view()),



]

urlpatterns = format_suffix_patterns(urlpatterns)
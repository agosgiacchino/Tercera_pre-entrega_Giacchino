from django.urls import path

from AppNomads import views





urlpatterns = [
   
    path('', views.inicio, name="Inicio"), #esta era nuestra primer view
    path('cursos', views.cursos, name="Cursos"),
    path('nomades', views.nomades, name="Nomades"),
    path('usuarios', views.usuarios, name="Usuarios"),
    path('viajes', views.viajes, name="Viajes"),
    #path('productoFormulario', views.productoFormulario, name="ProductoFormulario"),
    #path('nomadesFormulario', views.nomadesFormulario, name="NomadesFormulario"),
    #path('busquedaCodigo',  views.busquedaCodigo, name="BusquedaCodigo"),
    path('buscar/', views.buscar),
   
]


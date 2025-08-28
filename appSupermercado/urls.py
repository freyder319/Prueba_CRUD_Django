from django.contrib import admin 
from django.urls import path,include
from appSupermercado import views

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", views.home, name="home"),
    path("agregar/", views.agregar, name="agregar"),
    path("editar/<int:producto_id>/", views.editar,name="editar"),
    path("eliminar/<int:producto_id>/", views.eliminar,name="eliminar")
]
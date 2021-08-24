"""gamecenter URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from inicio import views
from django.conf import settings
from ventas import views as views_ventas

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views_ventas.ventas, name="principal"),
    path('nosotros/',views_ventas.nosotros, name="nosotros"),
    path('registrar/',views_ventas.registrar,name="Registrar"),
    path('favs/',views_ventas.favs, name="favs"),
    path('contacto/',views_ventas.contacto, name="contacto"),
    path('consultarComentario/',views_ventas.consultarComentarioContacto,name="Comentarios"),
    path('eliminarComentario/<int:id>/',views_ventas.eliminarComentarioContacto,name='Eliminar'),
    path('formEditarComentario/<int:id>/',views_ventas.consultarComentarioIndividual,name='ConsultaIndividual'),
    path('editarComentario/<int:id>/',views_ventas.editarComentarioContacto, name='Editar'),
]
if settings.DEBUG:
    from django.conf.urls.static import static
    urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)


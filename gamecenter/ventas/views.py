from django.shortcuts import render
from .models import ComentarioContacto, Ventas
from .models import Nosotros
from .forms import ComentarioContactoForm 
from django.shortcuts import get_object_or_404
#from .models import Desarrolladores
# Create your views here.

def ventas(request):
    ventas=Ventas.objects.all()
#all recupera todos los objetos del modelo (registros de la tabla alumnos)
    return render(request,"ventas/principal.html",{'ventas':ventas})
#Indicamos el lugar donde se renderizará el resultado de esta vista
# y enviamos la lista de alumnos recuparados

def nosotros(request):
    nosotros=Nosotros.objects.all()
    return render(request,"ventas/nosotros.html",{'nosotros':nosotros})

def favs(request):
    ventas=Ventas.objects.all()
    return render (request,"ventas/favs.html",{'ventas':ventas})

def contacto(request):
    return render (request,"ventas/contacto.html")

def registrar(request):
    if request.method == 'POST':
        form = ComentarioContactoForm(request.POST)
        if form.is_valid(): #Si los datos recibidos son correctos
            form.save() #inserta
            comentarios=ComentarioContacto.objects.all()
            return render(request,"ventas/consultaContacto.html",{'comentarios':comentarios})
            
    form = ComentarioContactoForm()
    #Si algo sale mal se reenvian al formulario los datos ingresados
    return render(request,'ventas/contacto.html',{'form': form}) 

def consultarComentarioContacto(request):
    comentarios=ComentarioContacto.objects.all()
    #all recupera todos los objetos del modelo (registros de la tabla
    #comentariosContacto)
    return render(request,"ventas/consultaContacto.html",{'comentarios':comentarios})

def eliminarComentarioContacto(request, id, confirmacion='ventas/confirmarEliminacion.html'):
    comentario= get_object_or_404(ComentarioContacto, id=id)
    if request.method=='POST':
        comentario.delete()
        comentarios=ComentarioContacto.objects.all()
        return render(request,"ventas/consultaContacto.html",{'comentarios':comentarios})
    return render(request, confirmacion, {'object':comentario})

def consultarComentarioIndividual(request, id):
    comentario=ComentarioContacto.objects.get(id=id)
    
    return render(request,"ventas/formEditarComentario.html",{'comentario':comentario})

def editarComentarioContacto(request, id):
    comentario= get_object_or_404(ComentarioContacto, id=id)
    form= ComentarioContactoForm(request.POST, instance=comentario)
    if form.is_valid():
        form.save()
        comentarios=ComentarioContacto.objects.all()
        return render(request,"ventas/consultaContacto.html",{'comentarios':comentarios})
    return render(request,"ventas/formEditarComentario.html",{'comentario':comentario})

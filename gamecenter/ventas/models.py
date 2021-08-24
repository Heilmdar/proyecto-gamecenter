from django.db import models


# Create your models here.
class Ventas(models.Model): #define la estructura de la tabla
    descripcion = models.TextField(null = True,max_length=500,verbose_name="Descripcion del producto")
    nombre = models.TextField(null = True,max_length=80,verbose_name="Nombre del producto") #texto largo
    cantidad = models.TextField(null = True,max_length=10,verbose_name="Cantidad en stock")
    precio= models.IntegerField(null = True,verbose_name="Precio del producto")
    imagen = models.ImageField(null = True, upload_to="fotos",verbose_name="Fotografía del producto")
    color= models.TextField(null = True,max_length=80,verbose_name="Color del producto")
    created = models.DateTimeField(auto_now_add=True) #fecha y tiempo
    updated = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "Venta"
        verbose_name_plural = "Ventas"
        ordering = ["-created"]
    
    def __str__(self):
        return self.nombre


class Nosotros(models.Model): #define la estructura de la tabla
    nombre = models.CharField(null = True,max_length=80,verbose_name="Nombre del desarrollador") #texto largo
    informacion = models.TextField(null = True,max_length=500,verbose_name="Informacion del desarrollador")
    imagen = models.ImageField(null = True, upload_to="fotos",verbose_name="Fotografía del desarrollador")
    created = models.DateTimeField(auto_now_add=True) #fecha y tiempo
    updated = models.DateTimeField(auto_now_add=True)
    class Meta:
        verbose_name = "Nosotro"
        verbose_name_plural = "Nosotros"
        ordering = ["-created"]
    
    def __str__(self):
        return self.nombre

class ComentarioContacto(models.Model):
    id = models.AutoField(primary_key=True,verbose_name="Clave")
    usuario = models.TextField(verbose_name="Usuario")
    mensaje = models.TextField(verbose_name="Comentario")
    created = models.DateTimeField(auto_now_add=True,verbose_name="Registrado")
   
    class Meta:
        verbose_name="Comentario Contacto"
        verbose_name_plural="Comentarios Contactos"
        ordering=["-created"]

    def __str__(self):
        return self.mensaje

from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    pass

class Subasta(models.Model):
    nombre= models.CharField(max_length=64)
    descripcion=models.TextField()
    fecha_ini=models.DateField()
    fecha_fin=models.DateField()
    estado= models.BooleanField() # true para activa y false para cerrada
    # Convertir el objeto subasta en una cadena al consultar la BD
    def __str__(self):
        return f"{self.id}: {self.nombre} y {self.descripcion}"
    

class CategoriaProd(models.Model):
    nombre= models.TextField()
    
class Producto(models.Model):
    nombre=models.CharField(max_length=64)
    descripcion= models.TextField()
    precio_inicial=models.FloatField()
    categoria=models.ForeignKey(CategoriaProd, on_delete=models.CASCADE,related_name="categoria")
    def __str__(self):
        return f"{self.nombre}: {self.descripcion} y {self.categoria}"
    
class Oferta(models.Model):
    monto=models.FloatField()
    subasta=models.ForeignKey(Subasta,on_delete=models.CASCADE,related_name="subasta")
    usuario=models.ForeignKey(User, on_delete=models.CASCADE,related_name="usuario")
    
class Subastado(models.Model):
    subasta=models.ForeignKey(Subasta,on_delete=models.CASCADE,related_name="subastado")
    producto=models.ForeignKey(Producto,on_delete=models.CASCADE,related_name="producto_sub")

    class Meta:
        unique_together = (('subasta', 'producto'),)
        #  la clase Meta es una clase interna que puedes usar en tus modelos para definir opciones de modelo específicas

class ImagenProducto(models.Model):
    id_producto = models.ForeignKey(Producto, on_delete=models.CASCADE)
    imagen = models.ImageField(upload_to='ruta/donde/guardar/imagenes')
    descripcion = models.TextField()

class ComentarioSubasta(models.Model):
    comentario=models.TextField()
    subasta=models.ForeignKey(Subasta,on_delete=models.CASCADE,related_name="comentarioSubasta")
    usuario=models.ForeignKey(User, on_delete=models.CASCADE,related_name="ComentarioUsuario")

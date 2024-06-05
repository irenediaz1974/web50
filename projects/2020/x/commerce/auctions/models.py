from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    pass

class Categoria(models.Model):
    cat_name= models.CharField(max_length=64)

    def __str__(self):
        return self.cat_name

class Imagen(models.Model):
    imagen = models.ImageField(upload_to='media')
    i_descrip = models.TextField()

class Producto(models.Model):
    p_nombre=models.CharField(max_length=64)
    p_descrip= models.TextField()
    p_monto_ini=models.FloatField()
    id_cat=models.ForeignKey(Categoria, on_delete=models.CASCADE,related_name="categoria_prod")
    id_imagen = models.ForeignKey(Imagen, on_delete=models.CASCADE, related_name="imagen_prod")
    
    def __str__(self):
        return f"{self.p_nombre}: {self.p_descrip} "
    

class Subasta(models.Model):

    id_user= models.ForeignKey(User, on_delete=models.CASCADE,related_name="usuario_subasta")
    s_nombre= models.CharField(max_length=64)
    s_descrip=models.TextField()
    s_fecha_ini=models.DateField(auto_now_add=True)
    s_fecha_fin=models.DateField()
    s_estado= models.BooleanField() # true para activa y false para cerrada

    def __str__(self):
        return self.s_nombre  
    
class Oferta(models.Model):

    o_monto=models.FloatField()
    id_subasta=models.ForeignKey(Subasta,on_delete=models.CASCADE,related_name="oferta_subasta")
    id_user=models.ForeignKey(User, on_delete=models.CASCADE,related_name="usuario_oferta")
    
class Subastado(models.Model):
    id_subasta=models.ForeignKey(Subasta,on_delete=models.CASCADE,related_name="subasta")
    id_producto=models.ForeignKey(Producto,on_delete=models.CASCADE,related_name="producto_subastado")

    class Meta:
        unique_together = (('id_subasta', 'id_producto'),)
        #  la clase Meta es una clase interna que puedes usar en tus modelos para definir opciones de modelo específicas


class Comentario(models.Model):
    s_coment=models.TextField()
    id_subasta=models.ForeignKey(Subasta,on_delete=models.CASCADE,related_name="Subasta_comentario")
    id_user=models.ForeignKey(User, on_delete=models.CASCADE,related_name="user_comentario")

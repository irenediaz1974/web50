from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.timezone import make_aware
from datetime import datetime

aware_datetime = make_aware(datetime.now())

class User(AbstractUser):
    pass

class Categoria(models.Model):
    cat_name= models.CharField(max_length=64)

    def __str__(self):
        return self.cat_name

    

class Subasta(models.Model):

    id_user= models.ForeignKey(User, on_delete=models.CASCADE,related_name="usuario_subasta")
    s_nombre= models.CharField(max_length=64)
    s_descrip=models.TextField()
    s_fecha_ini=models.DateTimeField(default=aware_datetime)
    s_fecha_fin=models.DateTimeField(default=aware_datetime)
    s_estado= models.BooleanField() # true para activa y false para cerrada

    def __str__(self):
        return f"{self.s_nombre}: {self.id_user} " 
    
class Imagen(models.Model):
    
    imagen = models.ImageField(upload_to='img')
    i_descrip = models.TextField()

    def __str__(self):
        return self.i_descrip
    
class Producto(models.Model):
    p_nombre=models.CharField(max_length=64)
    p_descrip= models.TextField()
    p_monto_ini=models.FloatField()
    id_cat=models.ForeignKey(Categoria, on_delete=models.CASCADE,related_name="categoria_prod")
    subasta = models.ForeignKey( Subasta, on_delete=models.CASCADE, related_name='productos')
    id_imagen = models.ForeignKey (Imagen, on_delete=models.CASCADE, related_name="id_imagen" )

    def __str__(self):
        return f"{self.p_nombre}: {self.p_descrip} "
     
    
class Oferta(models.Model):

    o_monto=models.FloatField()
    id_subasta=models.ForeignKey(Subasta,on_delete=models.CASCADE,related_name="oferta_subasta")
    id_user=models.ForeignKey(User, on_delete=models.CASCADE,related_name="usuario_oferta")
    o_fecha=models.DateTimeField(default=aware_datetime)
    
class Subastado(models.Model):
    won_user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="user_won_auctions" )
    id_subasta=models.ForeignKey(Subasta,on_delete=models.CASCADE,related_name="subasta")
    id_producto=models.ForeignKey(Producto,on_delete=models.CASCADE,related_name="producto_subastado")

    def __str__(self):
        return str(self.won_user)
        # return self.won_user

    class Meta:
        unique_together = (('id_subasta', 'id_producto'),)
        #  la clase Meta es una clase interna que puedes usar en tus modelos para definir opciones de modelo específicas


class Comentario(models.Model):
    s_coment=models.TextField()
    id_producto=models.ForeignKey(Producto,on_delete=models.CASCADE,related_name="producto_comentario", null=True)
    id_user=models.ForeignKey(User, on_delete=models.CASCADE,related_name="user_comentario")
    c_fecha=models.DateTimeField(default=aware_datetime)

class Watchlist(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    w_producto = models.ForeignKey(Producto, on_delete=models.CASCADE)
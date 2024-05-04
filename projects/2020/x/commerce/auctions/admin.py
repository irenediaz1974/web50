from django.contrib import admin
from .models import User, Subasta, Oferta, CategoriaProd, Producto, Subastado, ImagenProducto, ComentarioSubasta

# Register your models here.
admin.site.register(User)
admin.site.register(Subasta)
admin.site.register(Oferta)
admin.site.register(CategoriaProd)
admin.site.register(Producto)
admin.site.register(Subastado)
admin.site.register(ImagenProducto)
admin.site.register(ComentarioSubasta)
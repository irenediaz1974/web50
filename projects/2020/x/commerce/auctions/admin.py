from django.contrib import admin
from .models import User, Subasta, Oferta, Categoria, Producto, Subastado, Imagen, Comentario, Watchlist

# Register your models here.
admin.site.register(User)
admin.site.register(Subasta)
admin.site.register(Oferta)
admin.site.register(Categoria)
admin.site.register(Producto)
admin.site.register(Subastado)
admin.site.register(Imagen)
admin.site.register(Comentario)
admin.site.register(Watchlist)
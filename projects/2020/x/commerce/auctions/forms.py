from django import forms
from .models import Producto, CategoriaProd, Subasta, Subastado, Oferta,ComentarioSubasta,ImagenProducto

class ProductoForm(forms.ModelForm):
    class Meta:
        model = Producto
        fields = '__all__' 

class CategoriaForm(forms.ModelForm):
    class Meta:
        model = CategoriaProd
        fields = '__all__' 

class SubastaForm(forms.ModelForm):
    class Meta:
        model = Subasta
        fields = '__all__' 

class SubastadoForm(forms.ModelForm):
    class Meta:
        model = Subastado
        fields = '__all__' 

class OfertaForm(forms.ModelForm):
    class Meta:
        model = Oferta
        fields = '__all__' 

class ComentarioForm(forms.ModelForm):
    class Meta:
        model = ComentarioSubasta
        fields = '__all__' 

class ImagenProductoForm(forms.ModelForm):
    class Meta:
        model = ImagenProducto
        fields = '__all__' 
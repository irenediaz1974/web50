from django import forms
from .models import Producto, CategoriaProd, Subasta, Subastado, Oferta,ComentarioSubasta,ImagenProducto

class ProductoForm(forms.ModelForm):
    
    id_categoria = forms.ModelChoiceField(queryset=CategoriaProd.objects.all(), to_field_name="nombre")
    nombre = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control form-control-sm', 'id': 'nombre_producto'}))
    descripcion = forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control form-control-sm', 'id':'descripcion_producto', 'cols': 20, 'rows': 4}))
    
    class Meta:
        model = Producto
        fields = '__all__' 

class CategoriaForm(forms.ModelForm):

    nombre = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control form-control-sm', 'id': 'nombre_categoria'}))

    class Meta:
        model = CategoriaProd
        fields = '__all__' 

class SubastaForm(forms.ModelForm):
    
    fecha_ini=forms.DateField()
    fecha_fin=forms.DateField()
    descripcion = forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control form-control-sm', 'id':'descripcion_subasta', 'cols': 20, 'rows': 4}))
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
    descripcion = forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control form-control-sm', 'id':'descripcion_imagen','cols': 10, 'rows': 4}))
    class Meta:
        model = ImagenProducto
        fields = '__all__' 
        exclude = ['id_producto']
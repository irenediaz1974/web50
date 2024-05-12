from django import forms
from .models import Producto, Categoria, Subasta, Subastado, Oferta,Comentario,Imagen

class Categoria_form(forms.ModelForm):

    cat_name = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control form-control-sm', 'id': 'nombre_categoria'}))

    class Meta:
        model = Categoria
        fields = '__all__' 

class Imagen_form(forms.ModelForm):
    i_descrip = forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control form-control-sm', 'id':'descripcion_imagen','cols': 10, 'rows': 4}))
    class Meta:
        model = Imagen
        fields = '__all__' 
        

class Producto_form(forms.ModelForm):
    
    id_cat = forms.ModelChoiceField(queryset=Categoria.objects.all(), to_field_name="nombre_cat")
    p_nombre = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control form-control-sm', 'id': 'nombre_producto'}))
    p_descrip= forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control form-control-sm', 'id':'descripcion_producto', 'cols': 20, 'rows': 4}))
    id_imagen = forms.ModelChoiceField(queryset=Imagen.objects.all(), to_field_name="imagen")

    class Meta:
        model = Producto
        fields = '__all__' 



class Subasta_form(forms.ModelForm):
    
    fecha_ini=forms.DateField(required=True)
    fecha_fin=forms.DateField(required=True)
    s_descrip = forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control form-control-sm', 'id':'descripcion_subasta', 'cols': 20, 'rows': 4}))
    class Meta:
        model = Subasta
        fields = '__all__' 
    
class Oferta_form(forms.ModelForm):
    class Meta:
        model = Oferta
        fields = '__all__' 

class Subastado_form(forms.ModelForm):
    class Meta:
        model = Subastado
        fields = '__all__' 

class Coment_form(forms.ModelForm):
    class Meta:
        model = Comentario
        fields = '__all__' 


from django import forms
from django.forms import inlineformset_factory
from django.forms import modelformset_factory
from .models import Producto, Categoria, Subasta, Subastado, Oferta,Comentario,Imagen



class Categoria_form(forms.ModelForm):

    cat_name = forms.CharField(help_text="Enter category for products.", widget=forms.TextInput(attrs={'class': 'form-control form-control-sm', 'id': 'nombre_categoria'}))

    class Meta:
        model = Categoria
        fields = '__all__' 

class Imagen_form(forms.ModelForm):
    i_descrip = forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control form-control-sm', 'id':'descripcion_imagen','cols': 10, 'rows': 4}))
    
    class Meta:
        model = Imagen
        fields = '__all__' 
        

class Producto_form(forms.ModelForm):
    
    id_cat = forms.ModelChoiceField(queryset=Categoria.objects.all(), to_field_name="cat_name", required=False)
    p_nombre = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control form-control-sm', 'id': 'nombre_producto'}))
    p_descrip = forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control form-control-sm', 'id':'descripcion_producto', 'cols': 20, 'rows': 4}))
    id_imagen = forms.ModelChoiceField(queryset=Imagen.objects.all(), to_field_name="imagen", required=False)

    class Meta:
        model = Producto
        exclude = ['subasta']


# Inline Formsets to use in Products CRUD
ImageFormSet = inlineformset_factory(Producto, Imagen, form=Imagen_form, extra=1)
CategoryFormSet = modelformset_factory(Categoria, form=Categoria_form, extra=1)



class Subasta_form(forms.ModelForm):
    s_fecha_ini = forms.DateField( label="Fecha Inicial de Subasta", required=True,
        widget=forms.DateInput(format="%Y-%m-%d", attrs={"type": "date"}),
        input_formats=["%Y-%m-%d"])
    s_fecha_fin = forms.DateField(label="Fecha Final Programada", required=True,
        widget=forms.DateInput(format="%Y-%m-%d", attrs={"type": "date"}),
        input_formats=["%Y-%m-%d"])
    s_descrip= forms.CharField(label="Descripción de la Subasta", required=True,
                widget=forms.Textarea(attrs={'class': 
                'form-control form-control-sm', 'id':'descrip_subasta', 'cols': 10, 'rows': 2}))

    class Meta:
        model = Subasta
        fields = '__all__'
        exclude = ['id_user']

    def __init__(self, *args, **kwargs):
        super(Subasta_form, self).__init__(*args, **kwargs)
        self.fields['s_nombre'].label = "Nombre Subasta"
        self.fields['s_estado'].label = "Activa?"
       

    
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


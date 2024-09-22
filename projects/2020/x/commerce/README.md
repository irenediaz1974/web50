# README

## Tips: :bulb:

### :point_right: Tarea 1

a. En el modelado se definen 7 tablas: Usuario, Subasta, Producto, Categoria, Oferta, subastado, Imagen, Comentarios
 En el caso de la tabla subastado hay que prever que el mismo producto puede estar en varias subastas, por lo que la llave primaria de esta tabla seria una combinacion de dos llaves primarias de Producto y Subasta.
 Para implementarlo usé la clase Meta:

 ```python
 class Subastado(models.Model):
    id_subasta = models.ForeignKey(Subasta, on_delete=models.CASCADE)
    id_producto = models.ForeignKey(Producto, on_delete=models.CASCADE)

    class Meta:
        unique_together = (('id_subasta', 'id_producto'),)
 ```

 unique_together asegura que la combinación de id_subasta e id_producto sea única, actuando efectivamente como una clave primaria compuesta.
 :duck: **La clase Meta es una clase interna que puedes usar en tus modelos para definir opciones de modelo específicas. Por ejemplo, puedes usarla para especificar el nombre de la tabla de la base de datos, el orden de clasificación por defecto, si la combinación de algunos campos debe ser única (como en tu caso con unique_together), entre otras cosas. Es una forma de proporcionar metadatos adicionales a tu modelo.**
b. En el modelo del almacenamiento de la imagen del producto, utilicé segun recomendación de Duck la libreria Pillow.

```python
 class ImagenProducto(models.Model):
    id_producto = models.ForeignKey(Producto, on_delete=models.CASCADE)
    imagen = models.ImageField(upload_to='ruta/donde/guardar/imagenes')
    descripcion = models.TextField()
```

:duck: **Donde, upload_to es la ruta donde se guardarán las imágenes subidas. Django manejará automáticamente la subida de archivos y almacenará la ruta al archivo en la base de datos. Por favor, ten en cuenta que para usar ImageField, necesitarás tener instalada la biblioteca Pillow.**

```python
 pip install Pillow
```

c. Crear cuenta de superuser que permite acceder a la interface admin de Django

 ```python
 run python manage.py createsuperuser
 ```

d. :duck: **Django 3.2 introdujo una nueva configuración llamada DEFAULT_AUTO_FIELD para controlar el tipo de campo que se utiliza para las claves primarias automáticas. Antes de Django 3.2, el tipo de campo predeterminado era AutoField, que es un entero de 32 bits. Sin embargo, si tienes una gran cantidad de objetos, puedes quedarte sin valores. Por eso, Django 3.2 cambió el valor predeterminado a BigAutoField, que es un entero de 64 bits. Para eliminar que se cree por default la PK BigAutoField, debido a que mi BD es pequeña, debo:**

* Agregar en apps.py default_auto_field

```python
from django.apps import AppConfig

class AuctionsConfig(AppConfig):
    default_auto_field = 'django.db.models.AutoField' # Para que no cree BigAutoField por default
    name = 'auctions'
```

Revisar que en settings.py solo quede:
:bulb: Eliminé 'auctions' a sugerencia de Duck

```python
INSTALLED_APPS = [
    # otras apps aquí
    'auctions.apps.AuctionsConfig',  # tu configuración personalizada
]
```

e. Acciones en el modelo:

* Migrar el modelo: python manage.py makemigrations
* aplicar el modelo: python manage.py migrate

### Deshacer migraciones

```python
python manage.py migrate auctions 0001_initial
```

f. Trabajo con los campos fecha:

* Utilicé en el modelo: DateTimeField, para evitar el siguiente error a la hora de **migrate**

```python
RuntimeWarning: DateTimeField Oferta.o_fecha received a naive datetime (2024-06-06 06:08:14.107491) while time zone support is active
```

* :duck:
*Este aviso se refiere a que estás proporcionando una fecha y hora "naive" (ingenua), es decir, una que no tiene información de zona horaria, a un campo que espera una fecha y hora "aware" (consciente), es decir, una que tiene información de zona horaria.

Django utiliza zonas horarias en sus campos DateTimeField si la configuración USE_TZ está establecida como True. Si estás proporcionando una fecha y hora sin información de zona horaria, Django emitirá esta advertencia.

Para solucionar esto, puedes hacer que tu fecha y hora sean "aware" utilizando la función make_aware de Django. Aquí tienes un ejemplo de cómo podrías hacerlo:
`from django.utils.timezone import make_aware
from datetime import datetime

aware_datetime = make_aware(datetime.now())`*

* Para manipular los datos desde admin.py :
 debemos entrar los modelos que queremos utilizar en admin.py :

### Register your models here

admin.site.register(User)
admin.site.register(Subasta)
admin.site.register(Oferta)
admin.site.register(CategoriaProd)
admin.site.register(Producto)
admin.site.register(Subastado)
admin.site.register(ImagenProducto)
admin.site.register(ComentarioSubasta)
***

## :point_right: Tarea 2

a- Crear los modelos de formulario en forms.py

* Creo primeramente forms.py y le añado los formularios de cada tabla de la misma manera:

```python
from django import forms
from .models import Producto...

class ProductForm(forms.ModelForm):
    class Meta:
        model = Producto
        fields = '__all__' 
```

b- Crear la vista de añadir producto

* Para la imagen del producto instalé pillow. Ahora toca configurarlo:
:duck: **Primero, necesitas configurar MEDIA_URL y MEDIA_ROOT en tu archivo settings.py. MEDIA_ROOT es el directorio del sistema de archivos donde se guardarán los archivos cargados por los usuarios, y MEDIA_URL es la URL que se utilizará para referirse a estos archivos.**
:boom: Recordar añadirla a gitignore cuando vaya a submit el proyecto.

:duck: ### MEDIA_ROOT y MEDIA_URL son configuraciones en Django que se utilizan para manejar archivos de medios, como imágenes, que los usuarios de tu sitio web pueden subir. MEDIA_ROOT es la ubicación física en tu sistema de archivos donde estos archivos de medios se almacenarán. Por otro lado, MEDIA_URL es la URL base que Django usará para servir estos archivos de medios. Cuando se solicita un archivo de medios, Django busca el archivo en MEDIA_ROOT y luego lo sirve en una URL que comienza con MEDIA_URL.

Para configurar MEDIA_URL en tu archivo settings.py.
MEDIA_ROOT = os.path.join(BASE_DIR, '/media')
MEDIA_URL = '/media/'

## Tarea a realizar

### Complete la implementación de su sitio de subastas. Debes cumplir los siguientes requisitos

:white_check_mark: 1.-  **Models:** su aplicación debe tener al menos tres modelos además del modelo de Usuario: uno para subastas, uno para ofertas y otro para comentarios realizados en las subastas. Depende de usted decidir qué campos debe tener cada modelo y cuáles deben ser los tipos de esos campos. Es posible que tenga modelos adicionales si lo desea.

:white_check_mark: 2.- **Create Listing**
los usuarios deben poder crear una nueva entrada para un artículo que desean subastar. Deberán proporcionar un título para la subasta, una descripción del artículo, y la oferta inicial. También pueden optar por proporcionar una URL para una imagen del artículo y/o una categoría como Moda, Juguetes, Electrónica, Hogar, etc.

:white_check_mark: 3.- **Active Listings Page**: La ruta predeterminada de su aplicación web debería permitir a los usuarios ver todos los productos de subastas activos actualmente. Para cada producto activo, esta página debe mostrar (como mínimo) el título, la descripción, el precio actual y la foto (si existe una para el producto).

:negative_squared_cross_mark: 4.- **Listing Page**: Al hacer clic en un listado, los usuarios deberían acceder a una página específica de ese listado. En esa página, los usuarios deberían poder ver todos los detalles sobre el listado, incluido el precio actual del listado.

* Si el usuario ha iniciado sesión, debería poder agregar el elemento a su "Lista de seguimiento". Si el elemento ya está en la lista de seguimiento, el usuario debería poder eliminarlo.
* Si el usuario ha iniciado sesión, debería poder ofertar por el artículo. La oferta debe ser al menos tan grande como la oferta inicial y debe ser mayor que cualquier otra oferta que se haya realizado (si la hubiera). Si la oferta no cumple con esos criterios, se le debería presentar un error al usuario.
* Si el usuario ha iniciado sesión y es quien creó el listado, el usuario debería tener la capacidad de "cerrar" la subasta desde esta página, lo que convierte al mejor postor en el ganador de la subasta y hace que el listado ya no esté activo.
* Si un usuario ha iniciado sesión en una página de listado cerrada y el usuario ganó esa subasta, la página debería indicarlo.
        *  Los usuarios que hayan iniciado sesión deberían poder agregar comentarios a la página de listado. La página del listado debe mostrar todos los comentarios que se han realizado en el listado
:negative_squared_cross_mark: 5.- **Watchlist** : Los usuarios que hayan iniciado sesión deberían poder visitar una página de Lista de seguimiento, que debería mostrar todos los listados que un usuario ha agregado a su lista de seguimiento. Al hacer clic en cualquiera de esos listados, el usuario debería acceder a la página de ese listado.

:negative_squared_cross_mark: 6.- **Categories**: Los usuarios deberían poder visitar una página que muestre una lista de todas las categorías de listados. Al hacer clic en el nombre de cualquier categoría, el usuario debería acceder a una página que muestra todos los listados activos en esa categoría.

:negative_squared_cross_mark: 7.- **Django Admin Interface**: A través de la interfaz de administración de Django, un administrador del sitio debería poder ver, agregar, editar y eliminar cualquier listado, comentario y oferta realizada en el sitio.

Pistas

* Para crear una cuenta de superusuario que pueda acceder a la interfaz de administración de Django, ejecute:

```python
     python enable.py createsuperuser
     ```
     ###### user:root
     pass:rootAdmin
- Consulte la referencia del campo Modelo de Django para conocer los posibles tipos de campos para su modelo Django.
- Probablemente necesitarás crear algunos formularios de Django para varias partes de esta aplicación web.
- Agregar el decorador @login_required encima de cualquier vista garantizará que solo un usuario que haya iniciado sesión pueda acceder a esa vista.
- ¡Puedes modificar el CSS tanto como quieras para personalizar el sitio web! Algunas capturas de pantalla de muestra se muestran en la parte superior de esta página. Estos solo sirven como ejemplos: no es necesario que tu aplicación sea estéticamente igual a las capturas de pantalla aquí (¡te animamos a ser creativo!).
 


***
## Pasos seguidos:

- Luego de creado subdirectorio commerce
-  cd into the commerce
- Ejecutar para correr migrations en auctions app:


```python
    python manage.py makemigrations auctions
```

* Ejecutar  para aplicar migraciones a la Base de datos:

```python
python manage.py migrate
```

System check identified some issues:

   ```console
    WARNINGS:
    ←[33;1mauctions.User: (models.W042) Auto-created primary key used when not defining a primary key type, by default 'django.db.models.AutoField'.
            HINT: Configure the DEFAULT_AUTO_FIELD setting or the AuctionsConfig.default_auto_field attribute to point to a subclass of AutoField, e.g. 'django.db.models.BigAutoField'.←[0m
    ←[36;1mOperations to perform:←[0m
    ←[1m  Apply all migrations: ←[0madmin, auctions, auth, contenttypes, sessions
    ←[36;1mRunning migrations:←[0m
    Applying contenttypes.0001_initial...←[32;1m OK←[0m
   
   ```

***

## REQUERIMIENTOS

1. Manejar imagenes

```python
 pip install Pillow
```

2.Para visualizar la imagen utilizando Pillow debo agregar en settings.py:

```python
'django.template.context_processors.media'
```

sería en settings.py:
`TEMPLATES = [
    {
        ...
        'OPTIONS': {
            'context_processors': [
                ...
                'django.template.context_processors.media',
            ],
        },
    },
]`

En urls.py:

`from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    # your other url patterns
]

if settings.DEBUG:`

En views.py:

`from django.conf import settings
from django.shortcuts import render

def index(request):
    productos = Producto.objects.filter(subasta__s_estado=True).select_related('subasta', 'id_imagen').values('p_nombre', 'p_descrip', 'p_monto_ini', 'id_imagen__imagen')
    context = {
        'productos': productos,
        'MEDIA_URL': settings.MEDIA_URL,
    }
    return render(request, 'index.html', context)`

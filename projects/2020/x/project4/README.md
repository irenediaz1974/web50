# README *Project4*

*Diseñar un sitio web de red social similar a Threads para realizar publicaciones y seguir a usuarios.*

![Network Image](network/static/network/network.png)

## Tips: :bulb:

To Do

### :point_right: Tarea 1: New Post

a. - Ejecutar para correr migrations:

```python
   python manage.py makemigrations network
   python manage.py migrate
```


a. Añadí a admin.py los modelos proporcionados por el ejercicio:

```python
from django.contrib import admin
from .models import User

# Register your models here.
admin.site.register(User)
```

b. Crear cuenta de superuser que permite acceder a la interface admin de Django

 ```python
python manage.py createsuperuser
 ```

```console
Username: root
Email address: root@example.com
Password: rootAdmin
Password (again): rootAdmin
Superuser created successfully.
```

c.

d.

### :point_right: Tarea 2

-

### :point_right: Tarea 3

### :point_right: Tarea 4

### :point_right: Tarea 5

-

***

***

## Tarea a realizar

### Utilizando Python, JavaScript, HTML y CSS, complete la implementación de una red social que permita a los usuarios realizar publicaciones, seguir a otros usuarios y dar “me gusta” a las publicaciones. Debes cumplir con los siguientes requisitos

:negative_squared_cross_mark: 1.-  **New Post** Los usuarios que hayan iniciado sesión deberían poder escribir una nueva publicación basada en texto completando texto en un área de texto y luego haciendo clic en un botón para enviar la publicación.

- La captura de pantalla en la parte superior de esta especificación muestra el cuadro "Nueva publicación" y en la parte superior de la página "Todas las publicaciones". Puede optar por hacer esto también o puede hacer que la función "Nueva publicación" sea una página separada.

:negative_squared_cross_mark: 2.- **All Posts**  El enlace “All Posts”  en la barra de navegación debería llevar al usuario a una página donde pueda ver todas las publicaciones de todos los usuarios, con las publicaciones más recientes primero.

- Cada publicación debe incluir el nombre de usuario del autor, el contenido de la publicación en sí, la fecha y hora en que se realizó la publicación y la cantidad de "me gusta" que tiene la publicación (esto será 0 para todas las publicaciones hasta que implemente la capacidad de "Me gusta" una publicación más tarde)

:negative_squared_cross_mark: 3.- **Profile Page** Al hacer clic en un nombre de usuario se debería cargar la página de perfil de ese usuario. Esta página debería:

- Muestra la cantidad de seguidores que tiene el usuario, así como la cantidad de personas que sigue.
- Muestra todas las publicaciones de ese usuario, en orden cronológico inverso.
- Para cualquier otro usuario que haya iniciado sesión, esta página también debería mostrar un botón "Seguir" o "Dejar de seguir" que permitirá al usuario actual alternar si sigue o no las publicaciones de este usuario. Tenga en cuenta que esto sólo se aplica a cualquier "otro" usuario: un usuario no debería poder seguirse a sí mismo.

:negative_squared_cross_mark: 4.- **Following** El enlace “Following” en la barra de navegación debe llevar al usuario a una página donde vea todas las publicaciones realizadas por los usuarios que sigue el usuario actual.

- Esta página debería comportarse igual que la página "Todas las publicaciones", solo que con un conjunto más limitado de publicaciones.
- Esta página solo debería estar disponible para los usuarios que hayan iniciado sesión.

:negative_squared_cross_mark: 5.- **Pagination** En cualquier página que muestre publicaciones, las publicaciones solo deben mostrarse *10* en una página. Si hay más de diez publicaciones, debería aparecer un botón "Siguiente" para llevar al usuario a la siguiente página de publicaciones (que debe ser anterior a la página de publicaciones actual). Si no está en la primera página, debería aparecer un botón "Anterior" para llevar al usuario también a la página anterior de publicaciones.

- Consulte la sección Pistas para obtener algunas sugerencias sobre cómo implementar esto.

 6.- **Edit Post**  Los usuarios deberían poder hacer clic en el botón "Editar" o en el enlace de cualquiera de sus propias publicaciones para editar esa publicación.

- Cuando un usuario hace clic en "Editar" en una de sus propias publicaciones, el contenido de su publicación debe reemplazarse con un área de texto donde el usuario pueda editar el contenido de su publicación.
- Luego, el usuario debería poder "Guardar" la publicación editada. Usando JavaScript, deberías poder lograr esto sin necesidad de recargar toda la página.
- Por seguridad, asegúrese de que su aplicación esté diseñada de manera que no sea posible para un usuario, por cualquier ruta, editar las publicaciones de otro usuario.

:negative_squared_cross_mark: 7.- **“Like” and “Unlike”** Los usuarios deberían poder hacer clic en un botón o enlace en cualquier publicación para alternar si les "gusta" o no esa publicación.

- Al utilizar JavaScript, debe informar al servidor de forma asincrónica que actualice el recuento de me gusta (como mediante una llamada para recuperar) y luego actualizar el recuento de me gusta de la publicación que se muestra en la página, sin necesidad de volver a cargar toda la página.

 :white_check_mark:

### Pistas

Para ver ejemplos de llamadas de recuperación de JavaScript, es posible que le resulten útiles algunas de las rutas del Proyecto 3.

- Probablemente necesitarás crear uno o más modelos en network/models.py y/o modificar el modelo de usuario existente para almacenar los datos necesarios para tu aplicación web.
- La clase Paginator de Django puede ser útil para implementar la paginación en el back-end (en su código Python)
- Las funciones de paginación de Bootstrap pueden resultar útiles para mostrar páginas en el front-end (en su HTML).

:negative_squared_cross_mark:

***

## Pasos seguidos

- Download  <https://cdn.cs50.net/web/2020/spring/projects/4/network.zip> y descompacta.
- cd hacia el directorio project4.
- Realizar la migración.

  ```python
    python manage.py makemigrations network
 
- Ejecutar  para aplicar migraciones a la Base de datos:

```python
python manage.py migrate
```

***

## REQUERIMIENTOS

## Comprensión del proyecto

:file_folder: *project4* Contiene una única aplicación llamada network.

- En el código de distribución hay un proyecto de Django llamado proyecto4 que contiene una única aplicación llamada network, estructurada de manera similar a la aplicación de subastas del Proyecto 2.

- Primero, abra network/urls.py, donde se define la configuración de URL para esta aplicación. Tenga en cuenta que ya hemos escrito algunas URL para usted, incluida una ruta de índice predeterminada, una ruta /login, una ruta /logout y una ruta /register.

- Eche un vistazo a network/views.py para ver las vistas asociadas con cada una de estas rutas. La vista de índice por ahora devuelve una plantilla index.html casi vacía. La vista login_view muestra un formulario de inicio de sesión cuando un usuario intenta hacer un  GET a la página. Cuando un usuario envía el formulario utilizando el método de solicitud POST, el usuario se autentica, inicia sesión y se le redirige a index page. La vista logout_view cierra la sesión del usuario y lo redirige a  index page. Finalmente, register route muestra un formulario de registro al usuario y crea un nuevo usuario cuando se envía el formulario. Todo esto ya está hecho, por lo que debería ejecutar la aplicación y crear algunos usuarios.

- Ejecute python Manage.py RunServer para iniciar el servidor web Django y visite el sitio web en su navegador. Haga clic en "Registrarse" y regístrese para obtener una cuenta. Debería ver que ahora ha iniciado sesión como su cuenta de usuario y que los enlaces en la parte superior de la página han cambiado. ¿Cómo cambió el HTML? Eche un vistazo a network/templates/network/layout.html para ver el diseño HTML de esta aplicación. Tenga en cuenta que varias partes de la plantilla están incluidas en una verificación de if user.is_authentication, de modo que se puede representar contenido diferente dependiendo de si el usuario ha iniciado sesión o no. ¡Puedes cambiar este archivo si deseas agregar o modificar algo en el diseño!

- Finalmente, eche un vistazo a network/models.py. Aquí es donde definirá cualquier modelo para su aplicación web, donde cada modelo representa algún tipo de datos que desea almacenar en su base de datos. Comenzamos con un modelo de Usuario que representa a cada usuario de la aplicación. Debido a que hereda de AbstractUser, ya tendrá campos para un nombre de usuario, correo electrónico, contraseña, etc., pero puede agregar nuevos campos a la clase Usuario si hay información adicional sobre un usuario que desea representar. También deberá agregar modelos adicionales a este archivo para representar detalles sobre publicaciones, me gusta y seguidores. Recuerde que cada vez que cambie algo en network/models.py, primero deberá ejecutar python Manage.py makemigrations y luego python Manage.py migrar para migrar esos cambios a su base de datos.

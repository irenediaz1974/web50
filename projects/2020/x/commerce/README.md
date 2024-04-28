***
### Tips: :bulb:

***
## Tarea a realizar:

#### Complete la implementación de su sitio de subastas. Debes cumplir los siguientes requisitos:

:negative_squared_cross_mark: 1-  **Models:** su aplicación debe tener al menos tres modelos además del modelo de Usuario: uno para listados de subastas, uno para ofertas y otro para comentarios realizados en listados de subastas. Depende de usted decidir qué campos debe tener cada modelo y cuáles deben ser los tipos de esos campos. Es posible que tenga modelos adicionales si lo desea.

:negative_squared_cross_mark: 2- **Create Listing**: Los usuarios deberían poder visitar una página para crear una nueva lista. Deberían poder especificar un título para el listado, una descripción basada en texto y cuál debería ser la oferta inicial. Opcionalmente, los usuarios también deberían poder proporcionar una URL para una imagen del listado y/o una categoría (por ejemplo, moda, juguetes, electrónica, hogar, etc.).

:negative_squared_cross_mark: 3- **Active Listings Page**: La ruta predeterminada de su aplicación web debería permitir a los usuarios ver todos los listados de subastas activos actualmente. Para cada listado activo, esta página debe mostrar (como mínimo) el título, la descripción, el precio actual y la foto (si existe una para el listado).

:negative_squared_cross_mark: 4- **Listing Page**: Al hacer clic en un listado, los usuarios deberían acceder a una página específica de ese listado. En esa página, los usuarios deberían poder ver todos los detalles sobre el listado, incluido el precio actual del listado.

        * Si el usuario ha iniciado sesión, debería poder agregar el elemento a su "Lista de seguimiento". Si el elemento ya está en la lista de seguimiento, el usuario debería poder eliminarlo.
        *  Si el usuario ha iniciado sesión, debería poder ofertar por el artículo. La oferta debe ser al menos tan grande como la oferta inicial y debe ser mayor que cualquier otra oferta que se haya realizado (si la hubiera). Si la oferta no cumple con esos criterios, se le debería presentar un error al usuario.
        *  Si el usuario ha iniciado sesión y es quien creó el listado, el usuario debería tener la capacidad de "cerrar" la subasta desde esta página, lo que convierte al mejor postor en el ganador de la subasta y hace que el listado ya no esté activo.
        *  Si un usuario ha iniciado sesión en una página de listado cerrada y el usuario ganó esa subasta, la página debería indicarlo.
        *  Los usuarios que hayan iniciado sesión deberían poder agregar comentarios a la página de listado. La página del listado debe mostrar todos los comentarios que se han realizado en el listado. 

:negative_squared_cross_mark: 5- **Watchlist** : Los usuarios que hayan iniciado sesión deberían poder visitar una página de Lista de seguimiento, que debería mostrar todos los listados que un usuario ha agregado a su lista de seguimiento. Al hacer clic en cualquiera de esos listados, el usuario debería acceder a la página de ese listado.

:negative_squared_cross_mark: 6- **Categories**: Los usuarios deberían poder visitar una página que muestre una lista de todas las categorías de listados. Al hacer clic en el nombre de cualquier categoría, el usuario debería acceder a una página que muestra todos los listados activos en esa categoría.

:negative_squared_cross_mark: 7- **Django Admin Interface**: A través de la interfaz de administración de Django, un administrador del sitio debería poder ver, agregar, editar y eliminar cualquier listado, comentario y oferta realizada en el sitio.

Pistas

- Para crear una cuenta de superusuario que pueda acceder a la interfaz de administración de Django, ejecute:
     ```python
     python enable.py createsuperuser
     ```
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
 ###### System check identified some issues:

    ```console
    WARNINGS:
    ←[33;1mauctions.User: (models.W042) Auto-created primary key used when not defining a primary key type, by default 'django.db.models.AutoField'.
            HINT: Configure the DEFAULT_AUTO_FIELD setting or the AuctionsConfig.default_auto_field attribute to point to a subclass of AutoField, e.g. 'django.db.models.BigAutoField'.←[0m
    ←[36;1mMigrations for 'auctions':←[0m
    ←[1mauctions\migrations\0001_initial.py←[0m
        - Create model User
    ```
 
- Ejecutar  para aplicar migraciones a la Base de datos:
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
   
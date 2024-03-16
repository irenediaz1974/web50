
***
### Tips: :bulb:

1.- Como mostrar archivos **Markdown** *.md en HTML con **Django**.

Función en views.py que devuelve contenido HTML de un archivo markdown *.md:
    
```python
def entry(request, title):
    # Crear clase markdown para usarla para convertir de markdown a html
    mark_cont=Markdown()
    return render(request, "encyclopedia/title.html", {
         "title": title,
         "title_cont": mark_cont.convert(util.get_entry(title))
    })
``` 

   >Luego en la página html que vamos a renderizar debemos utilizar el filtro safe.

   ```python
    {{ title_cont|safe }}
   ```

This tells Django to treat title_cont as safe HTML and not escape it. If you're not using the safe filter, Django will escape the HTML, which could be why it's not rendering correctly.

2.- Debemos modificar la lista mostrada en **index.html** para que cada elemento *.md mostrado sea además un enlace a su página html (Se renderiza cuando se le da click)

Esto se resuelve logrando que cada elemento de la lista generada sea un enlace a la vista que renderiza la pagina, **title.html**
En index.html donde se genera la lista , dentro del ciclo For, agregamos:

    - <li><a href="{% url 'entry' entry %}">{{ entry }}</a></li>

Explicación de Duck: 
En la plantilla Django, cuando usas {% url 'entry' entry %}, el primer entry es el nombre de la vista en tu archivo urls.py, que debería apuntar a la función correspondiente en views.py. El segundo entry es el argumento que se pasa a esa vista.

Entonces, si tu vista entry en views.py se ve algo así:
```python
def entry(request, title):
    ...
```

El entry dentro de {% url 'entry' entry %} se reemplaza por cada elemento en tu lista entries, y ese valor se pasa como el argumento title a tu vista entry.

***
## Tarea a realizar:

En el código de distribución hay un proyecto de Django llamado wiki que contiene una única aplicación llamada enciclopedia.

1- Abrir encyclopedia/urls.py, donde se define la configuración de URL para esta aplicación. Observe que comenzamos con una única ruta predeterminada asociada con la función views.index.

2- A continuación, mire encyclopedia/util.py. No necesitará cambiar nada en este archivo, pero tenga en cuenta que hay tres funciones que pueden resultar útiles para interactuar con las entradas de la enciclopedia. list_entries devuelve una lista de los nombres de todas las entradas de la enciclopedia guardadas actualmente. save_entry guardará una nueva entrada de la enciclopedia, dado su título y parte del contenido de Markdown. get_entry recuperará una entrada de enciclopedia por su título y devolverá su contenido de Markdown si la entrada existe o Ninguno si la entrada no existe.

> default_storage es una instancia de la clase Storage que Django usa para manejar archivos estáticos y de medios. Esta instancia se configura en tu archivo settings.py con la variable DEFAULT_FILE_STORAGE. Por defecto, Django usa el sistema de archivos del sistema operativo, pero puedes cambiarlo a otros sistemas de almacenamiento como Amazon S3 o Google Cloud Storage.** Cualquiera de las vistas que escriba puede utilizar estas funciones para interactuar con las entradas de la enciclopedia

Cada entrada de la enciclopedia se guardará como un archivo Markdown dentro del directorio entries/. Donde existen ahora algunas entradas de muestra. Puedes agregar más!

Ahora, veamos enciclopedia/views.py. Ahora solo hay una vista aquí, la vista de índice. Esta vista devuelve una plantilla enciclopedia/index.html, proporcionando a la plantilla una lista de todas las entradas de la enciclopedia (obtenida llamando a util.list_entries, que vimos definida en util.py).

Puede encontrar la plantilla consultando encyclopedia/templates/encyclopedia/index.html. Esta plantilla hereda de un archivo base layout.html y especifica cuál debe ser el título de la página y qué debe haber en el cuerpo de la página: en este caso, una lista desordenada de todas las entradas de la enciclopedia. Mientras tanto, layout.html define la estructura más amplia de la página: cada página tiene una barra lateral con un campo de búsqueda (que por ahora no hace nada), un enlace para ir a casa y enlaces (que aún no funcionan) para crear una página. nueva página o visite una página aleatoria.

> La entrada {% load static %} en Django se utiliza para cargar la biblioteca de plantillas estáticas. Esto te permite acceder a tus archivos estáticos, como CSS, JavaScript o imágenes, que has almacenado en tu directorio STATICFILES_DIRS.


Especificación

Completa la implementación de tu enciclopedia Wiki. Debes cumplir con los siguientes requisitos:

:white_check_mark: 1.- Entry Page: visitar /wiki/TITLE, donde TíTULO es el título de una entrada de enciclopedia, debería mostrar una página que muestre el contenido de esa entrada de enciclopedia.

> Para que "Title" pueda aceptar un título variable. En Django, puedes hacerlo utilizando <str:variable> en tu ruta. Por ejemplo, podrías tener algo como ```path("wiki/<str:title>", views.entry, name="entry")``` donde views.entry es la función de vista que manejará la solicitud y mostrará la entrada de la enciclopedia.

 * La vista debe obtener el contenido de la entrada de la enciclopedia llamando a la función de utilidad adecuada.
 * Si se solicita una entrada que no existe, se le debe presentar al usuario una página de error que indica que no se encontró la página solicitada.
 * Si la entrada existe, se le debe presentar al usuario una página que muestra el contenido de la entrada. El título de la página debe incluir el nombre de la entrada.

:white_check_mark: 2.- Index Page: actualice index.html de modo que, en lugar de simplemente enumerar los nombres de todas las páginas de la enciclopedia, el usuario pueda hacer clic en el nombre de cualquier entrada para ir directamente a esa página de entrada.

:negative_squared_cross_mark: 3.- Search: permite al usuario escribir una consulta en el cuadro de búsqueda de la barra lateral para buscar una entrada de enciclopedia.
 * Si la consulta coincide con el nombre de una entrada de la enciclopedia, el usuario debe ser redirigido a la página de esa entrada.
 * Si la consulta no coincide con el nombre de una entrada de la enciclopedia, el usuario debería ser llevado a una página de resultados de búsqueda que muestra una lista de todas las entradas de la enciclopedia que tienen la consulta como subcadena. Por ejemplo, si la consulta de búsqueda fuera ytho, entonces Python debería aparecer en los resultados de la búsqueda.
 * Al hacer clic en cualquiera de los nombres de las entradas en la página de resultados de búsqueda, el usuario debería acceder a la página de esa entrada.

:negative_squared_cross_mark: 4.- New Page: Al hacer clic en "Crear nueva página" en la barra lateral, el usuario debería acceder a una página donde puede crear una nueva entrada de enciclopedia.
 * Los usuarios deberían poder ingresar un título para la página y, en un área de texto, deberían poder ingresar el contenido de Markdown para la página.
 * Los usuarios deberían poder hacer clic en un botón para guardar su nueva página.
 * Cuando se guarda la página, si ya existe una entrada de enciclopedia con el título proporcionado, se le debe presentar al usuario un mensaje de error.
 * De lo contrario, la entrada de la enciclopedia debe guardarse en el disco y el usuario debe ser llevado a la página de la nueva entrada.

:negative_squared_cross_mark: 5.- Edit Page: En cada página de entrada, el usuario debería poder hacer clic en un enlace para ir a una página donde el usuario puede editar el contenido de Markdown de esa entrada en un área de texto.
 * El área de texto debe rellenarse previamente con el contenido de Markdown existente de la página. (es decir, el contenido existente debe ser el valor inicial del área de texto).
 * El usuario debería poder hacer clic en un botón para guardar los cambios realizados en la entrada.
 * Una vez guardada la entrada, el usuario debe ser redirigido nuevamente a la página de esa entrada.

:negative_squared_cross_mark: 6.- Random Page: Al hacer clic en "Página aleatoria" en la barra lateral, el usuario debería acceder a una entrada aleatoria de la enciclopedia.
  
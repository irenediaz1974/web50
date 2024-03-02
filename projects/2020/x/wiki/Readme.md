Comprension:

En el código de distribución hay un proyecto de Django llamado wiki que contiene una única aplicación llamada enciclopedia.

1- Abrir encyclopedia/urls.py, donde se define la configuración de URL para esta aplicación. Observe que comenzamos con una única ruta predeterminada asociada con la función views.index.

2- A continuación, mire encyclopedia/util.py. No necesitará cambiar nada en este archivo, pero tenga en cuenta que hay tres funciones que pueden resultar útiles para interactuar con las entradas de la enciclopedia. list_entries devuelve una lista de los nombres de todas las entradas de la enciclopedia guardadas actualmente. save_entry guardará una nueva entrada de la enciclopedia, dado su título y parte del contenido de Markdown. get_entry recuperará una entrada de enciclopedia por su título y devolverá su contenido de Markdown si la entrada existe o Ninguno si la entrada no existe. Cualquiera de las vistas que escriba puede utilizar estas funciones para interactuar con las entradas de la enciclopedia.

Cada entrada de la enciclopedia se guardará como un archivo Markdown dentro del directorio entradas/. Si marca allá ahora, verá que hemos creado previamente algunas entradas de muestra. Puedes agregar más!

Ahora, veamos enciclopedia/views.py. Ahora solo hay una vista aquí, la vista de índice. Esta vista devuelve una plantilla enciclopedia/index.html, proporcionando a la plantilla una lista de todas las entradas de la enciclopedia (obtenida llamando a util.list_entries, que vimos definida en util.py).

Puede encontrar la plantilla consultando encyclopedia/templates/encyclopedia/index.html. Esta plantilla hereda de un archivo base layout.html y especifica cuál debe ser el título de la página y qué debe haber en el cuerpo de la página: en este caso, una lista desordenada de todas las entradas de la enciclopedia. Mientras tanto, layout.html define la estructura más amplia de la página: cada página tiene una barra lateral con un campo de búsqueda (que por ahora no hace nada), un enlace para ir a casa y enlaces (que aún no funcionan) para crear una página. nueva página o visite una página aleatoria.

Especificación

Completa la implementación de tu enciclopedia Wiki. Debes cumplir con los siguientes requisitos:

    1. Entry Page: visitar /wiki/TITLE, donde TíTULO es el título de una entrada de enciclopedia, debería mostrar una página que muestre el contenido de esa entrada de enciclopedia.
        * La vista debe obtener el contenido de la entrada de la enciclopedia llamando a la función de utilidad adecuada.
        * Si se solicita una entrada que no existe, se le debe presentar al usuario una página de error que indica que no se encontró la página solicitada.
        * Si la entrada existe, se le debe presentar al usuario una página que muestra el contenido de la entrada. El título de la página debe incluir el nombre de la entrada.
    2. Index Page: actualice index.html de modo que, en lugar de simplemente enumerar los nombres de todas las páginas de la enciclopedia, el usuario pueda hacer clic en el nombre de cualquier entrada para ir directamente a esa página de entrada.

  3. Search: permite al usuario escribir una consulta en el cuadro de b�squeda de la barra lateral para buscar una entrada de enciclopedia.
        * Si la consulta coincide con el nombre de una entrada de la enciclopedia, el usuario debe ser redirigido a la página de esa entrada.
        * Si la consulta no coincide con el nombre de una entrada de la enciclopedia, el usuario debería ser llevado a una página de resultados de búsqueda que muestra una lista de todas las entradas de la enciclopedia que tienen la consulta como subcadena. Por ejemplo, si la consulta de búsqueda fuera ytho, entonces Python debería aparecer en los resultados de la búsqueda.
       *  Al hacer clic en cualquiera de los nombres de las entradas en la página de resultados de búsqueda, el usuario debería acceder a la página de esa entrada.
    4. New Page: Al hacer clic en "Crear nueva página" en la barra lateral, el usuario debería acceder a una página donde puede crear una nueva entrada de enciclopedia.
        * Los usuarios deberían poder ingresar un título para la página y, en un área de texto, deberían poder ingresar el contenido de Markdown para la página.
        * Los usuarios deberían poder hacer clic en un botón para guardar su nueva página.
        * Cuando se guarda la página, si ya existe una entrada de enciclopedia con el título proporcionado, se le debe presentar al usuario un mensaje de error.
        * De lo contrario, la entrada de la enciclopedia debe guardarse en el disco y el usuario debe ser llevado a la página de la nueva entrada.

   5. Edit Page: En cada página de entrada, el usuario debería poder hacer clic en un enlace para ir a una página donde el usuario puede editar el contenido de Markdown de esa entrada en un área de texto.
        * El área de texto debe rellenarse previamente con el contenido de Markdown existente de la página. (es decir, el contenido existente debe ser el valor inicial del área de texto).
        * El usuario debería poder hacer clic en un botón para guardar los cambios realizados en la entrada.
        * Una vez guardada la entrada, el usuario debe ser redirigido nuevamente a la página de esa entrada.

   6. Random Page: Al hacer clic en "Página aleatoria" en la barra lateral, el usuario debería acceder a una entrada aleatoria de la enciclopedia.
   7. Markdown to HTML Conversion: en la página de cada entrada, cualquier contenido de Markdown en el archivo de entrada debe convertirse a HTML antes de mostrarse al usuario. Puede utilizar el paquete python-markdown2 para realizar esta conversión, que se puede instalar mediante pip3 install markdown2.
       * Desafío para aquellos más cómodos: si se siente más cómodo, intente implementar la conversión de Markdown a HTML sin utilizar bibliotecas externas, sin admitir encabezados, texto en negrita, listas desordenadas, enlaces y párrafos. Puede que le resulte útil utilizar expresiones regulares en Python(https://docs.python.org/3/howto/regex.html)

Pista:
De forma predeterminada, al sustituir un valor en una plantilla de Django, Django HTML escapa del valor para evitar generar HTML no deseado. Si desea permitir que se genere una cadena HTML, puede hacerlo con el filtro seguro (como agregando |seguro después del nombre de la variable que está sustituyendo).
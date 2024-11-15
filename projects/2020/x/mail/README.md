# README *MAIL*

*Diseñar una interfaz para un cliente de correo electrónico que realice llamadas API para enviar y recibir correos electrónicos.*

## Explicación junto a la solicitud del proyecto:

- project3: contiene una única aplicación llamada mail.

- Primero, después de realizar y aplicar las migraciones para el proyecto, ejecute python manage.py runserver para iniciar el servidor web. Abra el servidor web en su navegador y use el enlace “Registrar” para registrarse para una nueva cuenta. Los correos electrónicos que enviará y recibirá en este proyecto se almacenarán completamente en su base de datos (en realidad no se enviarán a servidores de correo electrónico reales), por lo que puede elegir cualquier dirección de correo electrónico (por ejemplo, foo@example.com) y contraseña que desee para este proyecto: las credenciales no necesitan ser credenciales válidas para direcciones de correo electrónico reales.

- Una vez que haya iniciado sesión, debería verse dirigido a la página Bandeja de entrada del cliente de correo, aunque esta página está mayormente en blanco (por ahora). Haga clic en los botones para navegar a sus buzones de correo Enviados y Archivados, y observe cómo estos también están actualmente en blanco. Haga clic en el botón “Redactar” y será dirigido a un formulario que le permitirá redactar un nuevo correo electrónico. Sin embargo, cada vez que haces clic en un botón, no se te lleva a una nueva ruta ni se realiza una nueva solicitud web: en cambio, toda esta aplicación es solo una página única, con JavaScript utilizado para controlar la interfaz de usuario. Ahora, observemos más de cerca el código de distribución para ver cómo funciona.

- Observa mail/urls.py y observa que la ruta predeterminada carga una función de índice en views.py. Por lo tanto, abramos views.py y observemos la función de índice. Observa que, siempre que el usuario haya iniciado sesión, esta función muestra la plantilla mail/inbox.html. Observemos esa plantilla, almacenada en mail/templates/mail/inbox.html. Notarás que en el cuerpo de la página, la dirección de correo electrónico del usuario se muestra primero en un elemento h2. Después de eso, la página tiene una secuencia de botones para navegar entre varias páginas de la aplicación. Debajo de eso, observa que esta página tiene dos secciones principales, cada una definida por un elemento div. El primero (con un id de emails-view) contiene el contenido de un buzón de correo electrónico (inicialmente vacío). El segundo (con un id de compose-view) contiene un formulario donde el usuario puede redactar un nuevo correo electrónico. Los botones de la parte superior, entonces, deben mostrar y ocultar selectivamente estas vistas: el botón de redacción, por ejemplo, debe ocultar la vista de correos electrónicos y mostrar la vista de redacción; el botón de bandeja de entrada, por su parte, debe ocultar la vista de redacción y mostrar la vista de correos electrónicos.
¿Cómo lo hacen? Observa que en la parte inferior de inbox.html se incluye el archivo JavaScript mail/inbox.js. Abre ese archivo, almacenado en mail/static/mail/inbox.js, y échale un vistazo. Observa que cuando se ha cargado el contenido DOM de la página, adjuntamos detectores de eventos a cada uno de los botones. Cuando se hace clic en el botón de la bandeja de entrada, por ejemplo, llamamos a la función load_mailbox con el argumento 'inbox'; cuando se hace clic en el botón de redacción, mientras tanto, llamamos a la función compose_email. ¿Qué hacen estas funciones? La función compose_email primero oculta la vista de correos electrónicos (al establecer su propiedad style.display en none) y muestra la vista de redacción (al establecer su propiedad style.display en block). Después de eso, la función toma todos los campos de entrada del formulario (donde el usuario puede escribir una dirección de correo electrónico de destinatario, línea de asunto y cuerpo de correo electrónico) y establece su valor en la cadena vacía '' para borrarlos. Esto significa que cada vez que haga clic en el botón “Redactar”, se le debe presentar un formulario de correo electrónico en blanco: puede probar esto escribiendo valores en el formulario, cambiando la vista a la Bandeja de entrada y luego volviendo a la vista Redactar.

- Mientras tanto, la función load_mailbox primero muestra la vista de correos electrónicos y oculta la vista de redacción. La función load_mailbox también toma un argumento, que será el nombre del buzón de correo que el usuario está intentando ver. Para este proyecto, diseñará un cliente de correo electrónico con tres buzones de correo: una bandeja de entrada, un buzón de correo enviado de todo el correo enviado y un archivo de correos electrónicos que alguna vez estuvieron en la bandeja de entrada pero que desde entonces se han archivado. El argumento de load_mailbox, entonces, será uno de esos tres valores, y la función load_mailbox muestra el nombre del buzón de correo seleccionado actualizando el innerHTML de la vista de correos electrónicos (después de poner en mayúscula el primer carácter). Por eso, cuando eliges un nombre de buzón en el navegador, ves que el nombre de ese buzón (en mayúscula) aparece en el DOM: la función load_mailbox está actualizando la vista de correos electrónicos para incluir el texto apropiado.

- Por supuesto, esta aplicación está incompleta. Todos los buzones simplemente muestran el nombre del buzón (Bandeja de entrada, Enviados, Archivo) pero en realidad todavía no muestran ningún correo electrónico. Todavía no hay una vista para ver realmente el contenido de ningún correo electrónico. Y el formulario de redacción te permitirá escribir el contenido de un correo electrónico, pero el botón para enviar el correo electrónico en realidad no hace nada. ¡Ahí es donde entras tú!

- API

- Recibirás, enviarás y actualizarás correos electrónicos mediante la API de esta aplicación. Hemos escrito toda la API para ti (y la documentamos a continuación), para que puedas usarla en tu código JavaScript. (De hecho, ten en cuenta que hemos escrito todo el código Python para este proyecto. Deberías poder completar este proyecto simplemente escribiendo HTML y JavaScript).

Esta aplicación admite las siguientes rutas API:



## Tips: :bulb:

### :point_right: Tarea 1: Send Mail

### :point_right: Tarea 2: Mailbox

### :point_right: Tarea 3: View Email

### :point_right: Tarea 4: Archive and Unarchive

### :point_right: Tarea 5: Reply

***

## Tarea a realizar

### Utilizando JavaScript, HTML y CSS, complete la implementación de su cliente de correo electrónico de aplicación de una sola página dentro de inbox.js. Debes cumplir con los siguientes requisitos

:negative_squared_cross_mark: 1.-  **Send Mail** Agregue código JavaScript para enviar un correo electrónico cuando el usuario envíe el formulario de redacción de correo electrónico.

- Probablemente quieras realizar una solicitud POST a /emails, pasando valores para los destinatarios, el asunto y el cuerpo.

- Una vez enviado el correo electrónico, cargue el buzón de enviados del usuario.

:negative_squared_cross_mark: 2.- **Mailbox** Cargue el buzón correspondiente cuando el usuario visite su Bandeja de entrada, Buzón de enviados o Archivo.

- Probablemente desee realizar una solicitud GET a /emails/<mailbox> para solicitar los correos electrónicos de un buzón en particular.
- Cuando se visita un buzón, la aplicación primero debe consultar la API para conocer los últimos correos electrónicos en ese buzón.
- Cuando se visita un buzón, el nombre del buzón debe aparecer en la parte superior de la página (esta parte se hace por usted).
- Luego, cada correo electrónico debe presentarse en su propio cuadro (por ejemplo, como un <div> con un borde) que muestra de quién proviene el correo electrónico, cuál es la línea de asunto y la marca de tiempo del correo electrónico.
- Si el correo electrónico no está leído, debería aparecer con un fondo blanco. Si el correo electrónico ha sido leído, debería aparecer con un fondo gris.

:negative_squared_cross_mark: 3.- **View Email** Cuando un usuario hace clic en un correo electrónico, se le debe llevar a una vista donde ve el contenido de ese correo electrónico.

- Probablemente quieras realizar una solicitud GET a /emails/<email_id> para solicitar el correo electrónico.
- Su aplicación debe mostrar el remitente, los destinatarios, el asunto, la marca de tiempo y el cuerpo del correo electrónico.
- Probablemente quieras agregar un div adicional a inbox.html (además de emails-view y compose-view) para mostrar el correo electrónico.
- Asegúrese de actualizar su código para ocultar y mostrar las vistas correctas cuando se hace clic en las opciones de navegación.
- Consulte la sugerencia en la sección [sugerencias](#Pistas) sobre cómo agregar un detector de eventos a un elemento HTML que haya agregado al DOM.
- Una vez que haya hecho clic en el correo electrónico, debe marcarlo como leído. Recuerde que puede enviar una solicitud PUT a /emails/<email_id> para actualizar si un correo electrónico se lee o no.

:negative_squared_cross_mark: 4.- **Archive and Unarchive** Permita a los usuarios archivar y desarchivar los correos electrónicos que hayan recibido.

- Al ver un correo electrónico de la Bandeja de entrada, al usuario se le debe presentar un botón que le permite archivar el correo electrónico. Al ver un correo electrónico Archivado, al usuario se le debe presentar un botón que le permite desarchivar el correo electrónico. Este requisito no se aplica a los correos electrónicos en el buzón de Enviados.
- Recuerde que puede enviar una solicitud PUT a /emails/<email_id> para marcar un correo electrónico como archivado o no archivado.
- Una vez que un correo electrónico ha sido archivado o desarchivado, cargue la bandeja de entrada del usuario.

:negative_squared_cross_mark: 5.- **Reply** Permitir a los usuarios responder a un correo electrónico.

- Al ver un correo electrónico, al usuario se le debe presentar un botón "Responder" que le permite responder al correo electrónico.
- Cuando el usuario hace clic en el botón "Responder", se le debe dirigir al formulario de redacción del correo electrónico.
- Complete previamente el formulario de redacción con el campo de destinatario configurado para quien envió el correo electrónico original.
- Complete previamente la línea de asunto. Si el correo electrónico original tenía una línea de asunto foo, la nueva línea de asunto debería ser Re: foo. (Si la línea de asunto ya comienza con Re:, no es necesario volver a agregarla).
- Complete previamente el cuerpo del correo electrónico con una línea como "El 1 de enero de 2020, a las 12:00 a. m., foo@example.com escribió:" seguida del texto original del correo electrónico.

:white_check_mark:

### Pistas

Para crear un elemento HTML y agregarle un controlador de eventos, puede usar código JavaScript como el siguiente:
    
`const element = document.createElement('div');
element.innerHTML = 'This is the content of the div.';
element.addEventListener('click', function() {
        console.log('This element has been clicked!')
});
document.querySelector('#container').append(element);`
    

Este código crea un nuevo elemento div, establece su HTML interno, agrega un controlador de eventos para ejecutar una función particular cuando se hace clic en ese div y luego lo agrega a un elemento HTML cuya identificación es container (este código supone que hay un elemento HTML cuya identificación es container: es probable que desee cambiar el argumento a querySelector para que sea cualquier elemento al que desee agregar un elemento).

- Puede resultarle útil editar mail/static/mail/styles.css para agregar cualquier CSS que necesite para la aplicación.
- Recuerde que si tiene una matriz de JavaScript, puede recorrer cada elemento de esa matriz usando forEach.
- Recuerde que normalmente, para solicitudes POST y PUT, Django requiere un token CSRF para protegerse contra posibles ataques de falsificación de solicitudes entre sitios. Para este proyecto, hemos hecho intencionalmente que las rutas API estén exentas de CSRF, por lo que no necesitará un token. Sin embargo, en un proyecto del mundo real, ¡siempre es mejor protegerse contra tales vulnerabilidades potenciales!

:negative_squared_cross_mark:

***

## Pasos seguidos

- Luego de creado descompactar <https://cdn.cs50.net/web/2020/spring/projects/3/mail.zip>
- cd into the mail
- Ejecutar para correr migrations:

```python
   python manage.py makemigrations mail
```

- Ejecutar  para aplicar migraciones a la Base de datos:

```python
python manage.py migrate
```



***

## REQUERIMIENTOS




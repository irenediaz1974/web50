# README *MAIL*

*Diseñar una interfaz para un cliente de correo electrónico que realice llamadas API para enviar y recibir correos electrónicos.*

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
- Consulte la sugerencia en la sección [Link to Pistas](#Pistas) sobre cómo agregar un detector de eventos a un elemento HTML que haya agregado al DOM.
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
    ```
    const element = document.createElement('div');
    element.innerHTML = 'This is the content of the div.';
    element.addEventListener('click', function() {
        console.log('This element has been clicked!')
    });
    document.querySelector('#container').append(element);
    ```

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

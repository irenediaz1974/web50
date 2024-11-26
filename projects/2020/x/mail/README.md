# README *MAIL*

*Diseñar una interfaz para un cliente de correo electrónico que realice llamadas API para enviar y recibir correos electrónicos.*

## Tips: :bulb:

Para "Limpiar" el navegador Mozilla Firefox de estilo CSS:
 Herramientas > Ajustes > Privacy & Security > Cookies and Site Data > Clear Data.

### :point_right: Tarea 1: Send Mail

a. Añadí a admin.py los modelos:

```python
from django.contrib import admin
from .models import User, Email

# Register your models here.
admin.site.register(User)
admin.site.register(Email)
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

c. En models.py se define una clase *Email* con una funcion **serialize** que se utiliza para convertir una instancia del modelo en un formato que se puede fácilmente convertir a JSON. Esto es útil para enviar datos a través de una API.
Este ejercicio solo tiene dos modelos de datos : Email y User

```python
class Email(models.Model):
    user = models.ForeignKey("User", on_delete=models.CASCADE, related_name="emails")
    sender = models.ForeignKey("User", on_delete=models.PROTECT, related_name="emails_sent")
    recipients = models.ManyToManyField("User", related_name="emails_received")
    subject = models.CharField(max_length=255)
    body = models.TextField(blank=True)
    timestamp = models.DateTimeField(auto_now_add=True)
    read = models.BooleanField(default=False)
    archived = models.BooleanField(default=False)

    def serialize(self):
        return {
            "id": self.id,
            "sender": self.sender.email,
            "recipients": [user.email for user in self.recipients.all()],
            "subject": self.subject,
            "body": self.body,
            "timestamp": self.timestamp.strftime("%b %d %Y, %I:%M %p"),
            "read": self.read,
            "archived": self.archived
        }
```

d. Esta seria la implementación en javascript para visualizar los correos que ha enviado el usuario logueado creando un div en en inbox.html :

```htm
 <div id="emails-container"></div>
```  

```javascript
fetch('/emails/sent')
    .then(response => response.json())
    .then(emails => {
    const container = document.getElementById('emails-container');
    container.innerHTML = ''; // Clear any existing content

    emails.forEach(email => {
        const emailElement = document.createElement('div');
        emailElement.innerHTML = `
            <h3>${email.subject}</h3>
            <p>From: ${email.sender}</p>
            <p>${email.timestamp}</p>
            <p>${email.body}</p>
        `;
        container.appendChild(emailElement);
        });
    });
```

### :point_right: Tarea 2: Mailbox

- Se visualizan o no los <div> que forman parte del buzon que se solicita por cada boton utilizando style= none, no se visualizará este div

 ```htm
  document.querySelector('#emails-container').style.display = 'none';
  document.querySelector('#emails-archived').style.display = 'block';
 ```

- Para evitar que un submit vaya hacia el server-side:

```javascript
 function save_email(event) {
  event.preventDefault();
  // code here
 }
```

### :point_right: Tarea 3: View Email

### :point_right: Tarea 4: Archive and Unarchive

- Una vez que se ha modificado, deberia verse el buzon inbox sin el elemento archivado, usé para ello:

```javascript
location.reload();
```

- Al añadirse codigo a evento click del botón archivar y al click del <li> como tal, para evitar que se ejecute el click del <li>

```javascript
event.stopPropagation();
``` 

### :point_right: Tarea 5: Reply

- Para agregar en el body el dato de la fecha en la que se escribió el correo que deseo responder debo convertir timestamp a un formato más "legible"

```javascript
const timestamp = new Date(email.timestamp);
const options = { 
  day: 'numeric', 
  month: 'long', 
  year: 'numeric', 
  hour: 'numeric', 
  minute: 'numeric', 
  hour12: true 
};
const formattedDate = timestamp.toLocaleString('es-ES', options);
```

***

## Tarea a realizar

### Utilizando JavaScript, HTML y CSS, complete la implementación de su cliente de correo electrónico de aplicación de una sola página dentro de inbox.js. Debes cumplir con los siguientes requisitos

:white_check_mark: 1.-  **Send Mail** Agregue código JavaScript para enviar un correo electrónico cuando el usuario envíe el formulario de redacción de correo electrónico.

- Probablemente quieras realizar una solicitud POST a /emails, pasando valores para los destinatarios, el asunto y el cuerpo.

- Una vez enviado el correo electrónico, cargue el buzón de enviados del usuario.

:white_check_mark: 2.- **Mailbox** Cargue el buzón correspondiente cuando el usuario visite su Bandeja de entrada, Buzón de enviados o Archivo.

- Probablemente desee realizar una solicitud GET a /emails/<mailbox> para solicitar los correos electrónicos de un buzón en particular.
- Cuando se visita un buzón, la aplicación primero debe consultar la API para conocer los últimos correos electrónicos en ese buzón.
- Cuando se visita un buzón, el nombre del buzón debe aparecer en la parte superior de la página (esta parte se hace por usted).
- Luego, cada correo electrónico debe presentarse en su propio cuadro (por ejemplo, como un <div> con un borde) que muestra de quién proviene el correo electrónico, cuál es la línea de asunto y la marca de tiempo del correo electrónico.
- Si el correo electrónico no está leído, debería aparecer con un fondo blanco. Si el correo electrónico ha sido leído, debería aparecer con un fondo gris.

:white_check_mark: 3.- **View Email** Cuando un usuario hace clic en un correo electrónico, se le debe llevar a una vista donde ve el contenido de ese correo electrónico.

- Probablemente quieras realizar una solicitud GET a /emails/<email_id> para solicitar el correo electrónico.
- Su aplicación debe mostrar el remitente, los destinatarios, el asunto, la marca de tiempo y el cuerpo del correo electrónico.
- Probablemente quieras agregar un div adicional a inbox.html (además de emails-view y compose-view) para mostrar el correo electrónico.
- Asegúrese de actualizar su código para ocultar y mostrar las vistas correctas cuando se hace clic en las opciones de navegación.
- Consulte la sugerencia en la sección [sugerencias](#pistas) sobre cómo agregar un detector de eventos a un elemento HTML que haya agregado al DOM.
- Una vez que haya hecho clic en el correo electrónico, debe marcarlo como leído. Recuerde que puede enviar una solicitud PUT a /emails/<email_id> para actualizar si un correo electrónico se lee o no.

:white_check_mark: 4.- **Archive and Unarchive** Permita a los usuarios archivar y desarchivar los correos electrónicos que hayan recibido.

- Al ver un correo electrónico de la Bandeja de entrada, al usuario se le debe presentar un botón que le permite archivar el correo electrónico. Al ver un correo electrónico Archivado, al usuario se le debe presentar un botón que le permite desarchivar el correo electrónico. Este requisito no se aplica a los correos electrónicos en el buzón de Enviados.
- Recuerde que puede enviar una solicitud PUT a /emails/<email_id> para marcar un correo electrónico como archivado o no archivado.
- Una vez que un correo electrónico ha sido archivado o desarchivado, cargue la bandeja de entrada del usuario.

:white_check_mark: 5.- **Reply** Permitir a los usuarios responder a un correo electrónico.

- Al ver un correo electrónico, al usuario se le debe presentar un botón "Responder" que le permite responder al correo electrónico.
- Cuando el usuario hace clic en el botón "Responder", se le debe dirigir al formulario de redacción del correo electrónico.
- Complete previamente el formulario de redacción con el campo de destinatario configurado para quien envió el correo electrónico original.
- Complete previamente la línea de asunto. Si el correo electrónico original tenía una línea de asunto foo, la nueva línea de asunto debería ser Re: foo. (Si la línea de asunto ya comienza con Re:, no es necesario volver a agregarla).
- Complete previamente el cuerpo del correo electrónico con una línea como "El 1 de enero de 2020, a las 12:00 a. m., <foo@example.com> escribió:" seguida del texto original del correo electrónico.


:negative_squared_cross_mark:

### Pistas

Para crear un elemento HTML y agregarle un controlador de eventos, puede usar código JavaScript como el siguiente:

```javascript
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

- Luego de ejecutado se creaon los modelos User y Email

    ```console
    - Create model User
    - Create model Email
    ```

- Ejecutar  para aplicar migraciones a la Base de datos:

```python
python manage.py migrate
```

***

## REQUERIMIENTOS

## Explicación junto a la solicitud del proyecto

:file_folder: *project3* Contiene una única aplicación llamada mail.

- Despues de la migracion ejecute *python manage.py runserver* para iniciar el servidor web. Abra el servidor web en su navegador y use el enlace “Registrar” para registrarse para una nueva cuenta. Los correos electrónicos que enviará y recibirá en este proyecto se almacenarán completamente en su base de datos local, por lo que puede elegir cualquier dirección de correo electrónico (por ejemplo, <foo@example.com>) y contraseña que desee para este proyecto.

- Observa mail/urls.py y observa que la ruta predeterminada carga una función de índice en views.py. Por lo tanto, abramos views.py y observemos la función de índice. Observa que, siempre que el usuario haya iniciado sesión, esta función muestra la plantilla mail/inbox.html. Observemos esa plantilla, almacenada en mail/templates/mail/inbox.html. Notarás que en el cuerpo de la página, la dirección de correo electrónico del usuario se muestra primero en un elemento h2. Después de eso, la página tiene una secuencia de botones para navegar entre varias páginas de la aplicación. Debajo de eso, observa que esta página tiene dos secciones principales, cada una definida por un elemento div. El primero (con un id de emails-view) contiene el contenido de un buzón de correo electrónico (inicialmente vacío). El segundo (con un id de compose-view) contiene un formulario donde el usuario puede redactar un nuevo correo electrónico. Los botones de la parte superior, entonces, deben mostrar y ocultar selectivamente estas vistas: el botón de redacción, por ejemplo, debe ocultar la vista de correos electrónicos y mostrar la vista de redacción; el botón de bandeja de entrada, por su parte, debe ocultar la vista de redacción y mostrar la vista de correos electrónicos.
¿Cómo lo hacen? Observa que en la parte inferior de inbox.html se incluye el archivo JavaScript mail/inbox.js. Abre ese archivo, almacenado en mail/static/mail/inbox.js, y échale un vistazo. Observa que cuando se ha cargado el contenido DOM de la página, adjuntamos detectores de eventos a cada uno de los botones. Cuando se hace clic en el botón de la bandeja de entrada, por ejemplo, llamamos a la función load_mailbox con el argumento 'inbox'; cuando se hace clic en el botón de redacción, mientras tanto, llamamos a la función compose_email. ¿Qué hacen estas funciones? La función compose_email primero oculta la vista de correos electrónicos (al establecer su propiedad style.display en none) y muestra la vista de redacción (al establecer su propiedad style.display en block). Después de eso, la función toma todos los campos de entrada del formulario (donde el usuario puede escribir una dirección de correo electrónico de destinatario, línea de asunto y cuerpo de correo electrónico) y establece su valor en la cadena vacía '' para borrarlos. Esto significa que cada vez que haga clic en el botón “Redactar”, se le debe presentar un formulario de correo electrónico en blanco: puede probar esto escribiendo valores en el formulario, cambiando la vista a la Bandeja de entrada y luego volviendo a la vista Redactar.

- Mientras tanto, la función load_mailbox primero muestra la vista de correos electrónicos y oculta la vista de redacción. La función load_mailbox también toma un argumento, que será el nombre del buzón de correo que el usuario está intentando ver. Para este proyecto, diseñará un cliente de correo electrónico con tres buzones de correo: una bandeja de entrada, un buzón de correo enviado de todo el correo enviado y un archivo de correos electrónicos que alguna vez estuvieron en la bandeja de entrada pero que desde entonces se han archivado. El argumento de load_mailbox, entonces, será uno de esos tres valores, y la función load_mailbox muestra el nombre del buzón de correo seleccionado actualizando el innerHTML de la vista de correos electrónicos (después de poner en mayúscula el primer carácter). Por eso, cuando eliges un nombre de buzón en el navegador, ves que el nombre de ese buzón (en mayúscula) aparece en el DOM: la función load_mailbox está actualizando la vista de correos electrónicos para incluir el texto apropiado.

- Por supuesto, esta aplicación está incompleta. Todos los buzones simplemente muestran el nombre del buzón (Bandeja de entrada, Enviados, Archivo) pero en realidad todavía no muestran ningún correo electrónico. Todavía no hay una vista para ver realmente el contenido de ningún correo electrónico. Y el formulario de redacción te permitirá escribir el contenido de un correo electrónico, pero el botón para enviar el correo electrónico en realidad no hace nada. ¡Ahí es donde entras tú!

### API

- Recibirás, enviarás y actualizarás correos electrónicos mediante la API de esta aplicación. Hemos escrito toda la API para ti (y la documentamos a continuación), para que puedas usarla en tu código JavaScript. (De hecho, ten en cuenta que hemos escrito todo el código Python para este proyecto. Deberías poder completar este proyecto simplemente escribiendo HTML y JavaScript).

Esta aplicación admite las siguientes rutas API:

#### GET /emails/<str:mailbox>

Al enviar una solicitud GET a /emails/<buzón> donde <buzón> es bandeja de entrada, enviado o archivo, le devolverá (en formato JSON) una lista de todos los correos electrónicos en ese buzón, en orden cronológico inverso. Por ejemplo, si envía una solicitud GET a /emails/inbox, es posible que obtenga una respuesta JSON como la siguiente (que representa dos correos electrónicos):

```json
[
    {
        "id": 100,
        "sender": "foo@example.com",
        "recipients": ["bar@example.com"],
        "subject": "Hello!",
        "body": "Hello, world!",
        "timestamp": "Jan 2 2020, 12:00 AM",
        "read": false,
        "archived": false
    },
    {
        "id": 95,
        "sender": "baz@example.com",
        "recipients": ["bar@example.com"],
        "subject": "Meeting Tomorrow",
        "body": "What time are we meeting?",
        "timestamp": "Jan 1 2020, 12:00 AM",
        "read": true,
        "archived": false
    }
]
```

Tenga en cuenta que cada correo electrónico especifica su identificación (un identificador único), una dirección de correo electrónico del remitente, una serie de destinatarios, una cadena para el asunto, el cuerpo y la marca de tiempo, así como dos valores booleanos que indican si el correo electrónico se ha leído y si el correo electrónico ha sido leído. ha sido archivado.

¿Cómo obtendrías acceso a dichos valores en JavaScript? Recuerde que en JavaScript, puede utilizar fetch para realizar una solicitud web. Por lo tanto, el siguiente código JavaScript

```javascript
fetch('/emails/inbox')
.then(response => response.json())
.then(emails => {
    // Print emails
    console.log(emails);

    // ... do something else with emails ...
});
```

haría una solicitud GET a /emails/inbox, convertiría la respuesta resultante a JSON y luego le proporcionaría la matriz de correos electrónicos dentro de la variable emails. Puede imprimir ese valor en la consola del navegador usando console.log (si no tiene ningún correo electrónico en su bandeja de entrada, será una matriz vacía), o hacer otra cosa con esa matriz.

Tenga en cuenta también que si solicita un buzón no válido (cualquier cosa que no sea bandeja de entrada, enviado o archivo), recibirá la respuesta JSON  {"error": "Invalid mailbox."}.

#### GET /emails/<int:email_id>

Al enviar una solicitud GET a /emails/email_id donde email_id es un ID entero para un correo electrónico, se devolverá una representación JSON del correo electrónico, como la siguiente:

```json
{
        "id": 100,
        "sender": "foo@example.com",
        "recipients": ["bar@example.com"],
        "subject": "Hello!",
        "body": "Hello, world!",
        "timestamp": "Jan 2 2020, 12:00 AM",
        "read": false,
        "archived": false
}
```

Tenga en cuenta que si el correo electrónico no existe, o si el usuario no tiene acceso al correo electrónico, la ruta devolverá un error 404 No encontrado con una respuesta JSON de {"error": "Correo electrónico no encontrado".

Para obtener el correo electrónico número 100, por ejemplo, puede escribir código JavaScript como

```javascript
fetch('/emails/100')
.then(response => response.json())
.then(email => {
    // Print email
    console.log(email);

    // ... do something else with email ...
});
```

#### POST /emails

Hasta ahora, hemos visto cómo recibir correos electrónicos: todos los correos electrónicos de un buzón o solo un correo electrónico. Para enviar un correo electrónico, puede enviar una solicitud POST a la ruta /emails. La ruta requiere que se envíen tres datos: un valor de destinatario (una cadena separada por comas de todos los usuarios a los que enviar un correo electrónico), una cadena de asunto y una cadena de cuerpo. Por ejemplo, podría escribir código JavaScript como

```javascript
fetch('/emails', {
  method: 'POST',
  body: JSON.stringify({
      recipients: 'baz@example.com',
      subject: 'Meeting time',
      body: 'How about we meet tomorrow at 3pm?'
  })
})
.then(response => response.json())
.then(result => {
    // Print result
    console.log(result);
});
```

Si el correo electrónico se envía correctamente, la ruta responderá con un código de estado 201 y una respuesta JSON de {"message": "Correo electrónico enviado correctamente."}.

Tenga en cuenta que debe haber al menos un destinatario de correo electrónico: si no se proporciona uno, la ruta responderá con un código de estado 400 y una respuesta JSON de {"error": "Se requiere al menos un destinatario". Todos los destinatarios también deben ser usuarios válidos que se hayan registrado en esta aplicación web en particular: si intenta enviar un correo electrónico a <baz@example.com> pero no hay ningún usuario con esa dirección de correo electrónico, obtendrá una respuesta JSON de {"error ": "El usuario con correo electrónico <baz@example.com> no existe."}.

#### PUT /emails/<int:email_id>

La última ruta que necesitará es la capacidad de marcar un correo electrónico como leído/no leído o como archivado/no archivado. Para hacerlo, envíe una solicitud PUT (en lugar de una solicitud GET) a /emails/<email_id> donde email_id es la identificación del correo electrónico que está intentando modificar. Por ejemplo, código JavaScript como

```javascript
fetch('/emails/100', {
  method: 'PUT',
  body: JSON.stringify({
      archived: true
  })
})
```

marcaría el correo electrónico número 100 como archivado. El cuerpo de la solicitud PUT también podría ser {archived: false} para desarchivar el mensaje, y también podría ser {read: true} o read: false} para marcar el correo electrónico como leído o no leído, respectivamente.

Al utilizar estas cuatro rutas API (recibir todos los correos electrónicos en un buzón, obtener un solo correo electrónico, enviar un correo electrónico y actualizar un correo electrónico existente), debería tener todas las herramientas que necesita ahora para completar este proyecto.

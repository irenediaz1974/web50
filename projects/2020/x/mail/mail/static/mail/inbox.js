document.addEventListener('DOMContentLoaded', function() {
  // Use buttons to toggle between views
  document.querySelector('#inbox').addEventListener('click', () => {
    history.pushState({ mailbox: 'inbox' }, '', '#inbox');
    load_mailbox('inbox');
  });
  document.querySelector('#sent').addEventListener('click', () => {
    history.pushState({ mailbox: 'sent' }, '', '#sent');
    load_mailbox('sent');
  });
  document.querySelector('#archived').addEventListener('click', () => {
    history.pushState({ mailbox: 'archive' }, '', '#archive');
    load_mailbox('archive');
  });
  document.querySelector('#compose').addEventListener('click', function() {
    history.pushState({ compose: {} }, '', '#compose');
    compose_email({});
  });
  // By default, load the inbox
  load_mailbox('inbox');
});

window.addEventListener('popstate', (event) => {
  if (event.state) {
    if (event.state.mailbox) {
      load_mailbox(event.state.mailbox);
    } else if (event.state.compose) {
      compose_email(event.state.compose);
    }
  }
});



function compose_email(email) {

  // Show compose view and hide other views
  document.querySelector('#emails-view').style.display = 'none';
  document.querySelector('#compose-view').style.display = 'block';

  // Clear out composition fields
  document.querySelector('#compose-recipients').value = '';
  document.querySelector('#compose-subject').value = '';
  document.querySelector('#compose-body').value = '';

   // save email
  if (email) {
    // email exists, write data inside html
    document.querySelector('#compose-recipients').value= email.sender;

    if (!email.subject.startsWith('Re: ')) {
      document.querySelector('#compose-subject').value = 'Re: '+ email.subject;
    } else {
      document.querySelector('#compose-subject').value = email.subject;
    }

    document.querySelector('#compose-body').value = 'El: ' + convert(email.timestamp) + ', ' + email.sender + " escribió: " + email.body;
  } else {
    // email does not exist, handle accordingly
  }
  document.querySelector('form').onsubmit=save_email; 
}

function load_mailbox(mailbox) {
  
  // Show the mailbox and hide other views
  document.querySelector('#emails-view').style.display = 'block';
  document.querySelector('#compose-view').style.display = 'none';

  // Show the mailbox name
  document.querySelector('#emails-view').innerHTML = `<h3>${mailbox.charAt(0).toUpperCase() + mailbox.slice(1)}</h3>`;
  
  // obtain data from API (django views)


  fetch('/emails/' + mailbox)
    .then(response => response.json())
    .then(data => {
                
      let ul = document.createElement('ul');
      data.forEach(item => {
          let li = document.createElement('li');
      
          let sender = document.createElement('span');
          sender.textContent = `Sender: ${item.sender}`;
          sender.id = 'sender';
      
          let subject = document.createElement('span');
          subject.textContent = `   ${item.subject}`;
          subject.id = 'subject';

          let timestamp = document.createElement('span');
          timestamp.textContent = `${item.timestamp}`;
          timestamp.id = 'timestamp';
          
      
          li.appendChild(sender);
          li.appendChild(subject);
          li.appendChild(timestamp);
         
          if (mailbox==='inbox'){
            
            let archivedButton = document.createElement('button');
            archivedButton.textContent = "Archivar";
            archivedButton.id = 'archivedButton';
            archivedButton.addEventListener('click', function(event) {
              event.stopPropagation();
              archivar(item.id, true, mailbox);
              location.reload();
            });

            li.appendChild(archivedButton);

            if (item.read === true) {
             // SET li style
              li.classList.add('highlight');
            }
            li.addEventListener('click', function() {
              leer(item.id);
            });
          }

          if (mailbox==='archive'){
          
            let archivedButton = document.createElement('button');
            archivedButton.textContent = "NO Archivar";
            archivedButton.id = 'archivedButton';                     
            archivedButton.addEventListener('click', function() {
              archivar(item.id, false, mailbox);
              location.reload();
            });
          
            li.appendChild(archivedButton);

          }
           // Click Event to Read Email
      
        ul.appendChild(li);

      });

      document.querySelector('#emails-view').appendChild(ul);
            console.log(data);
            console.log(mailbox);
    });
}


function archivar(id_email, setear, mailbox) {

  fetch(`/emails/${id_email}`, {
      method: 'PUT',
      body: JSON.stringify({
          archived: setear
      })
  })
  .then(response => {
    if (response.ok && mailbox === "inbox") {
        // Elimina el botón del DOM
        archivedButton.parentElement.remove();
        load_mailbox('inbox');
    }
  });

  if (mailbox === "archive"){
    const container = document.getElementById('emails-view');
    if (container!=null) {
      container.innerHTML = ''; // Clear any existing content
      
    } 
  }   
}

function leer(id_email) {

  document.querySelector('#emails-view').style.display = 'block';
  document.querySelector('#compose-view').style.display = 'none';

  const container = document.getElementById('emails-view');
  if (container!=null) {
    container.innerHTML = ''; // Clear any existing content
  }
  
  // obtain all mail data from django view email(request, email_id):
  fetch(`/emails/${id_email}`)
  .then(response => response.json())
  .then(email => {
    const emailElement = document.createElement('div');
    emailElement.innerHTML = `
      <h3>Sender: ${email.sender}</h3>
      <h3>Subject: ${email.subject}</h3>
      <p>From: ${email.sender}</p>
      <p>${email.timestamp}</p>
      <p>${email.body}</p>
      <button id="replyButton">Reply</button>
    `;
    container.appendChild(emailElement);
    document.getElementById('replyButton').addEventListener('click', function() {
      compose_email(email);

    });
    console.log(email);
  });
  
  // mark element as read
  fetch(`/emails/${id_email}`, {
    method: 'PUT',
    body: JSON.stringify({
      read: true
    })
  });

}

function save_email(event) {
  
  event.preventDefault();
  
  const v_recipients = document.querySelector('#compose-recipients').value;
  const v_subject = document.querySelector('#compose-subject').value;
  const v_body = document.querySelector('#compose-body').value;

  fetch('/emails', {
    method: 'POST',
    body: JSON.stringify({
        recipients: v_recipients,
        subject: v_subject,
        body: v_body
    })
  })
  .then(response => response.json())
  .then(result => {
      console.log(result);
  })
  .catch(error => {
      console.log("Este es un error:", error);
  });

  load_mailbox('sent');

}

function convert(timestamp) {
  const date = new Date(timestamp);
  const options = { 
    day: 'numeric', 
    month: 'long', 
    year: 'numeric', 
    hour: 'numeric', 
    minute: 'numeric', 
    hour12: true 
  };
  return date.toLocaleString('es-ES', options);
}


document.addEventListener('DOMContentLoaded', function() {

  // Use buttons to toggle between views
  document.querySelector('#inbox').addEventListener('click', () => load_mailbox('inbox'));
  document.querySelector('#sent').addEventListener('click', () => load_mailbox('sent'));
  document.querySelector('#archive').addEventListener('click', () => load_mailbox('archive'));
  document.querySelector('#compose').addEventListener('click', compose_email);
  document.querySelector('form').onsubmit=save_email; 

  // By default, load the inbox
  load_mailbox('inbox');
});

function compose_email() {


  // Show compose view and hide other views
  document.querySelector('#sent-view').style.display = 'none';
  document.querySelector('#archive-view').style.display = 'none';
  document.querySelector('#inbox-view').style.display = 'none';
  document.querySelector('#compose-view').style.display = 'block';

  // Clear out composition fields
  document.querySelector('#compose-recipients').value = '';
  document.querySelector('#compose-subject').value = '';
  document.querySelector('#compose-body').value = '';
 
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
        // Print result
        console.log(result);
    })
    .catch(error => {
        console.log("Este es un error:", error);
    });

    fetch('/emails/sent')
    .then(response => response.json())
    .then(emails => {
    const container = document.getElementById('sent-view');
    container.innerHTML = ''; // Clear any existing content

    emails.forEach(email => {
        const emailElement = document.createElement('div');
        emailElement.className = "email-body";
        emailElement.innerHTML = `
            <h3>${email.subject}</h3>
            <p>From: ${email.sender}</p>
            <p>${email.timestamp}</p>
        `;
        container.appendChild(emailElement);
    });
});

  load_mailbox('sent')
}



function load_mailbox(mailbox) {

    // Show the mailbox and hide other views

    let variable = mailbox;
  
    if (mailbox === "inbox") {
        // Your code for inbox
         document.querySelector('#sent-view').style.display = 'none';
         document.querySelector('#archive-view').style.display = 'none';
         document.querySelector('#inbox-view').style.display = 'block';
         document.querySelector('#compose-view').style.display = 'none';
         document.querySelector('#show-view').style.display = 'none';

         load_data(mailbox);


    } else if (mailbox === "sent") {
        // Your code for sent
        document.querySelector('#sent-view').style.display = 'block';
        document.querySelector('#archive-view').style.display = 'none';
        document.querySelector('#inbox-view').style.display = 'none';
        document.querySelector('#compose-view').style.display = 'none';
        document.querySelector('#show-view').style.display = 'none';
        load_data(mailbox);


    } else if (mailbox === "archive") {
        // Your code for archive
        document.querySelector('#sent-view').style.display = 'none';
        document.querySelector('#archive-view').style.display = 'block';
        document.querySelector('#inbox-view').style.display = 'none';
        document.querySelector('#compose-view').style.display = 'none';
        document.querySelector('#show-view').style.display = 'none';
        load_data(mailbox);

    } else {
        // Handle invalid mailbox
        console.error("Algo salio mal con mailbox.");
    }

  // Show the mailbox name
  document.querySelector('#'+ mailbox + '-view').innerHTML = `<h2>${mailbox.charAt(0).toUpperCase() + mailbox.slice(1)}</h2>`;
  console.log(mailbox);
}

function load_data(mailbox) {
  
  const variable = mailbox;
  fetch(`/emails/${variable}`)
  .then(response => response.json())
  .then(emails => {
      const container = document.getElementById(variable + '-view');

      if (container!=null) {
        container.innerHTML = ''; // Clear any existing content
        const titleElement = document.createElement('h4');
        titleElement.innerText = mailbox.charAt(0).toUpperCase() + mailbox.slice(1);
        container.appendChild(titleElement);
      }
     
      emails.forEach(email => {
          const emailElement = document.createElement('div');
          emailElement.className = "email-body"; 
          emailElement.addEventListener('click', function() {      
            showEmail(email.id)
          });
          if (email.read === true && mailbox === 'inbox') {
            emailElement.style.backgroundColor = "lightgray";
          }
          console.log(email);
          
          emailElement.innerHTML = `
              <h3>${email.subject}</h3>
              <p>From: ${email.sender}</p>
              <p>${email.timestamp}</p>
          `;
          if (email.archived === true && mailbox === 'archive') {
            console.log("Estoy en archive ");

            // Create the undo archived button
            const undoButton = document.createElement('button');
            undoButton.textContent = 'Undo  Archived';
            undoButton.onclick = function() {
              fetch(`/emails/${email.id}`, {
                method: 'PUT',
                body: JSON.stringify({
                  archived: false
                })
              })
              console.log('Deshacer email archived');
            };
            emailElement.appendChild(undoButton);
         }
          container.appendChild(emailElement);
    });
  }); 
}

function showEmail(idEmail) {

  document.querySelector('#sent-view').style.display = 'none';
  document.querySelector('#archive-view').style.display = 'none';
  document.querySelector('#inbox-view').style.display = 'none';
  document.querySelector('#compose-view').style.display = 'none';
  document.querySelector('#show-view').style.display = 'block';

  const id_email = String(idEmail);
  fetch(`/emails/${id_email}`)
  .then(response => response.json())
  .then(email => {
    const container = document.getElementById('show-view');
    if (container!=null) {
      container.innerHTML = ''; // Clear any existing content
    }
    const emailElement = document.createElement('div');
    emailElement.innerHTML = `
        <h3>Sender: ${email.sender}</h3>
        <h3>Subject:${email.subject}</h3>
        <p>From: ${email.sender}</p>
        <p>H${email.timestamp}</p>
        <p>${email.body}</p>
        
      `;
      // Create the Archived button
      const archiveButton = document.createElement('button');
      archiveButton.textContent = 'Archived';
      archiveButton.onclick = function() {
        fetch(`/emails/${id_email}`, {
          method: 'PUT',
          body: JSON.stringify({
            archived: true
          })
        })
        console.log('Archived button clicked');
      };

      // Append the button to the emailElement
      emailElement.appendChild(archiveButton);
      container.appendChild(emailElement);
  })

  fetch(`/emails/${id_email}`, {
    method: 'PUT',
    body: JSON.stringify({
      read: true
    })
  })
  .then(response => {
    if (!response.ok) {
      throw new Error('Network response was not ok');
    }
    return response.text(); // Use .text() to avoid JSON parsing error
  })
  .then(data => {
    console.log('Email marked as read:');
  })
  .catch(error => {
    console.error('There was a problem with the fetch operation:', error);
  });
}

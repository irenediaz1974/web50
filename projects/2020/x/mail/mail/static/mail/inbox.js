document.addEventListener('DOMContentLoaded', function() {

  // Use buttons to toggle between views
  document.querySelector('#inbox').addEventListener('click', () => load_mailbox('inbox'));
  document.querySelector('#sent').addEventListener('click', () => load_mailbox('sent'));
  document.querySelector('#archived').addEventListener('click', () => load_mailbox('archive'));
  document.querySelector('#compose').addEventListener('click', compose_email);
  document.querySelector('form').onsubmit=save_email; 

  // By default, load the inbox
  load_mailbox('inbox');
});

function compose_email() {


  // Show compose view and hide other views
  document.querySelector('#sent-view').style.display = 'none';
  document.querySelector('#archived-view').style.display = 'none';
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
        emailElement.innerHTML = `
            <h3>${email.subject}</h3>
            <p>From: ${email.sender}</p>
            <p>${email.timestamp}</p>
            <p>${email.body}</p>
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
         document.querySelector('#archived-view').style.display = 'none';
         document.querySelector('#inbox-view').style.display = 'block';
         document.querySelector('#compose-view').style.display = 'none';

         load_data(mailbox);


    } else if (mailbox === "sent") {
        // Your code for sent
        document.querySelector('#sent-view').style.display = 'block';
        document.querySelector('#archived-view').style.display = 'none';
        document.querySelector('#inbox-view').style.display = 'none';
        document.querySelector('#compose-view').style.display = 'none';
        load_data(mailbox);


    } else if (mailbox === "archive") {
        // Your code for archive
        document.querySelector('#sent-view').style.display = 'none';
        document.querySelector('#archived-view').style.display = 'block';
        document.querySelector('#inbox-view').style.display = 'none';
        document.querySelector('#compose-view').style.display = 'none';
        load_data(mailbox);

    } else {
        // Handle invalid mailbox
        console.error("Algo salio mal con mailbox.");
    }

  // Show the mailbox name
  // document.querySelector('#inbox-view').innerHTML = `<h3>${mailbox.charAt(0).toUpperCase() + mailbox.slice(1)}</h3>`;
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
      }
      
      emails.forEach(email => {
          const emailElement = document.createElement('div');
          emailElement.innerHTML = `
              <h3>${email.subject}</h3>
              <p>From: ${email.sender}</p>
              <p>${email.timestamp}</p>
          `;
          container.appendChild(emailElement);
    });
  });

 
}
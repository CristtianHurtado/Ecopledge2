document.getElementById('register-form').addEventListener('submit', function(event) {
  event.preventDefault(); // Evitar el envío tradicional del formulario

  const email = document.getElementById('email').value;
  const password = document.getElementById('password').value;
  const name = document.getElementById('name').value;

  fetch('/api/auth/register', {
      method: 'POST',
      headers: {
          'Content-Type': 'application/json'
      },
      body: JSON.stringify({ email, password, name })
  })
  .then(response => response.json())
  .then(data => {
      if (response.ok) {
          alert(data.message);
          // Redirigir o hacer algo más aquí
      } else {
          alert(data.message);
      }
  })
  .catch(error => {
      console.error('Error:', error);
  });
});

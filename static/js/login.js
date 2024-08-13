async function login() {
  const email = document.getElementById('email').value;
  const password = document.getElementById('password').value;

  try {
      const response = await fetch('/api/auth/login', {
          method: 'POST',
          headers: {
              'Content-Type': 'application/json'
          },
          body: JSON.stringify({ email, password })
      });

      if (!response.ok) {
          throw new Error('Network response was not ok');
      }

      const data = await response.json();
      const responseMessage = document.getElementById('responseMessage');

      if (response.ok) {
          responseMessage.innerText = data.message;
          responseMessage.style.color = 'green';
          window.location.href = '/recicla.html'; // Redirigir a la página de reciclaje
      } else {
          responseMessage.innerText = data.message;
          responseMessage.style.color = 'red';
      }
  } catch (error) {
      console.error('Error:', error);
      document.getElementById('responseMessage').innerText = 'Error en la solicitud.';
      document.getElementById('responseMessage').style.color = 'red';
  }
}
1
document.addEventListener('DOMContentLoaded', () => {
  const yearEl = document.getElementById('year');
  if (yearEl) yearEl.textContent = new Date().getFullYear();

  const form = document.getElementById('contact-form');
  const status = document.getElementById('form-status');
  if (!form) return;

  form.addEventListener('submit', async (e) => {
    e.preventDefault();
    const submitBtn = form.querySelector('button[type="submit"]');
    const data = {
      name: form.name.value.trim(),
      email: form.email.value.trim(),
      message: form.message.value.trim(),
    };

    status.textContent = '';
    status.className = 'form-status';

    if (!data.name || !data.email || !data.message) {
      status.textContent = 'Por favor completa todos los campos.';
      status.classList.add('error');
      return;
    }

    submitBtn.disabled = true;
    submitBtn.textContent = 'Enviando…';

    try {
      const res = await fetch('/api/contact', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify(data),
      });
      const result = await res.json();

      if (res.ok) {
        status.textContent = result.message || 'Mensaje enviado. Te responderemos pronto.';
        status.classList.add('ok');
        form.reset();
      } else {
        status.textContent = result.message || 'No se pudo enviar el mensaje. Intenta de nuevo.';
        status.classList.add('error');
      }
    } catch (err) {
      status.textContent = 'No se pudo conectar con el servidor. Intenta de nuevo.';
      status.classList.add('error');
    } finally {
      submitBtn.disabled = false;
      submitBtn.textContent = 'Enviar mensaje';
    }
  });
});

# CG NEX — Sitio web

Estructura del proyecto:

```
cgnex_site/
├── app.py                 # Backend en Python (Flask)
├── requirements.txt       # Dependencias de Python
├── messages.json          # Se crea solo al recibir el primer mensaje
├── templates/
│   └── index.html         # Estructura de la página
└── static/
    ├── css/
    │   └── style.css      # Estilos
    ├── js/
    │   └── main.js        # Lógica del formulario de contacto
    └── img/
        └── logo.png       # Logo de CG NEX (fondo transparente)
```

## Cómo ejecutarlo localmente

1. Instala las dependencias:
   ```bash
   pip install -r requirements.txt
   ```

2. Inicia el servidor:
   ```bash
   python app.py
   ```

3. Abre tu navegador en:
   ```
   http://localhost:5000
   ```

## Qué hace cada parte

- **`app.py`**: sirve la página y expone `/api/contact`, que valida y guarda
  los mensajes del formulario en `messages.json`. También expone
  `/api/messages` para que puedas revisar los mensajes recibidos desde el
  navegador (uso interno, no enlazado en la página).
- **`static/js/main.js`**: envía el formulario sin recargar la página
  (fetch al backend) y muestra el resultado al usuario.
- **`static/css/style.css`**: todo el diseño visual, con variables de color
  para soportar modo claro/oscuro automáticamente.

## Personalizar

- Cambia el correo y el WhatsApp de contacto directamente en
  `templates/index.html` (sección `#contacto`).
- Para enviar los mensajes por correo real en vez de solo guardarlos,
  reemplaza el comentario en `app.py` (`/api/contact`) por tu integración
  de SMTP, SendGrid, etc.
- Reemplaza `static/img/logo.png` si consigues una versión de mayor
  resolución de tu logo.

## Desplegar en producción

Este proyecto está listo para desplegarse en cualquier servicio que soporte
Python/Flask (Render, Railway, PythonAnywhere, un VPS propio, etc.). Para
producción, sirve la app con un servidor WSGI como Gunicorn en vez de
`app.run(debug=True)`:

```bash
pip install gunicorn
gunicorn app:app
```

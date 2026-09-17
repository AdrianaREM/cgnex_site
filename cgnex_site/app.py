"""
CG NEX — servidor web
----------------------
Sirve la página principal y procesa el formulario de contacto,
guardando cada mensaje en messages.json.

Ejecutar:
    pip install -r requirements.txt
    python app.py

Luego abre http://localhost:5000 en tu navegador.
"""

import json
import re
from datetime import datetime
from pathlib import Path

from flask import Flask, jsonify, render_template, request

app = Flask(__name__)

MESSAGES_FILE = Path(__file__).parent / "messages.json"
EMAIL_RE = re.compile(r"^[^@\s]+@[^@\s]+\.[^@\s]+$")


def load_messages():
    if MESSAGES_FILE.exists():
        with open(MESSAGES_FILE, "r", encoding="utf-8") as f:
            return json.load(f)
    return []


def save_message(entry):
    messages = load_messages()
    messages.append(entry)
    with open(MESSAGES_FILE, "w", encoding="utf-8") as f:
        json.dump(messages, f, ensure_ascii=False, indent=2)


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/api/contact", methods=["POST"])
def contact():
    data = request.get_json(silent=True) or {}
    name = (data.get("name") or "").strip()
    email = (data.get("email") or "").strip()
    message = (data.get("message") or "").strip()

    if not name or not email or not message:
        return jsonify(message="Todos los campos son obligatorios."), 400

    if not EMAIL_RE.match(email):
        return jsonify(message="Ingresa un correo válido."), 400

    entry = {
        "name": name,
        "email": email,
        "message": message,
        "received_at": datetime.utcnow().isoformat() + "Z",
    }
    save_message(entry)

    # Aquí es donde conectarías un envío de correo real (SMTP, SendGrid, etc.)
    # o una integración con un CRM. Por ahora, el mensaje queda guardado
    # en messages.json para que puedas revisarlo.

    return jsonify(message="Mensaje enviado. Te responderemos pronto."), 200


@app.route("/api/messages")
def list_messages():
    """Endpoint simple para revisar los mensajes recibidos (uso interno)."""
    return jsonify(load_messages())


if __name__ == "__main__":
    app.run(debug=True, port=5000)

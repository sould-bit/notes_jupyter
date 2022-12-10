import yowsup
import time

# Autenticación en la API de WhatsApp
yowsup.auth(3053074359, auth_code)

# Conexión a la API de WhatsApp
yowsup.client()

while True:
    # Envío del mensaje a nuestra novia
    yowsup.send(3162114537, "Buenos días")

    # Esperamos 24 horas para enviar el siguiente mensaje
    time.sleep(24 * 60 * 60)

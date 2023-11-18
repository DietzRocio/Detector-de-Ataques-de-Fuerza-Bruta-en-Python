# Detector-de-Ataques-de-Fuerza-Bruta-en-Python
Este proyecto consiste en un script simple en Python para detectar posibles ataques de fuerza bruta en registros de inicio de sesión. El script analiza direcciones IP en un archivo de registro y notifica si se supera un umbral predefinido de intentos fallidos.

Reemplaza 'ruta_del_archivo.log' con la ruta real de tu archivo de registro a analizar.
with open('ruta_del_archivo.log', 'r') as file:
    log_file = file.read()


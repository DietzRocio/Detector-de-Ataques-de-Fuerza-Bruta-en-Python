import re
from collections import Counter
#carga de registros simulados
log_file = """
Successful login from 192.168.0.4
Failed login attempt from 192.168.0.1
Failed login attempt from 192.168.0.2
Successful login from 192.168.0.5
Failed login attempt from 192.168.0.1
Failed login attempt from 192.168.0.3
Successful login from 192.168.0.6
Failed login attempt from 192.168.0.2
"""
#Acá a analizamos archivos de registro
def detect_brute_force(log_data):
    ip_addresses = re.findall(r'(\d+\.\d+\.\d+\.\d+)', log_data)
    ip_counter = Counter(ip_addresses)
    threshold = 3
    brute_force_attempts = [ip for ip, count in ip_counter.items() if count > threshold]
    return brute_force_attempts
#mostramos el resultado del analisis
brute_force_ips = detect_brute_force(log_file)
if brute_force_ips:
    print("Posible ataque de fuerza bruta detectado. Direcciones IP sospechosas:")
    for ip in brute_force_ips:
        print(ip)
else:
    print("No se detectaron ataques de fuerza bruta.")

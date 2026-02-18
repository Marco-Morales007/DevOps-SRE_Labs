"""
15. Script que valide la conectividad de microservicios (simulado) 
    - Da una lista de IPs/URLs, prueba conexión a puerto 80/443 y notifica si están caídos. 
    - Aprende: socket, manejo de excepciones, color en terminal.
"""

import socket

# Lista de hosts/IPs a verificar
servicios = [
    ("google.com", 80),
    ("github.com", 443),
    ("localhost", 22)  # SSH en mi VM de virtual box con ubuntu
]

def probar_conexion(host, puerto, timeout=3):
    try:
        with socket.create_connection((host, puerto), timeout=timeout):
            print(f" {host}:{puerto} está disponible")
    except Exception as e:
        print(f" {host}:{puerto} no responde ({e})")

if __name__ == "__main__":
    for host, puerto in servicios:
        probar_conexion(host, puerto)

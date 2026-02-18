"""
14. Generador de contraseñas seguras 
    - Script que cree contraseñas aleatorias seguras para servicios. 
    - Aprende: random, secrets, string.
"""

import secrets
import string

def generar_password(longitud=16):
    caracteres = string.ascii_letters + string.digits + string.punctuation
    return ''.join(secrets.choice(caracteres) for _ in range(longitud))

if __name__ == "__main__":
    for i in range(5):
        print(f" Contraseña {i+1}: {generar_password()}") #generar_password(X) donde X es la longitud de contra (16 por default)

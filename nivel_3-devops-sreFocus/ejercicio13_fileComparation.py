"""
13. Comparador de archivos de configuración 
    - Compara dos archivos .conf y muestra diferencias. 
    - Aprende: difflib, fileinput.

"""

import difflib

def comparar_archivos(archivo1, archivo2):
    with open(archivo1, "r") as f1, open(archivo2, "r") as f2:
        contenido1 = f1.readlines()
        contenido2 = f2.readlines()

    diff = difflib.unified_diff(
        contenido1, contenido2,
        fromfile=archivo1, tofile=archivo2,
        lineterm=""
    )

    print("\n".join(diff))

# Ejemplo de uso
comparar_archivos("config1.conf", "config2.conf")

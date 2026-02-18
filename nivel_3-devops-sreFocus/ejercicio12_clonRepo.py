"""
12. Script para clonar repositorios de Git 
    - Le das una lista de URLs de repos, los clona y crea carpetas. 
    - Aprende: subprocess, git, bucles.
"""

import subprocess
import os

#repos a clonar
repos = [
    "https://github.com/git/git.git",
    "https://github.com/vim/vim.git"
]
#crear la carpeta para almacenar repos si no existe
def clonar_repositorios(lista, destino="repositorios"):
    if not os.path.exists(destino):
        os.makedirs(destino)

    os.chdir(destino)
    for repo in lista:
        nombre = repo.split("/")[-1].replace(".git", "")
        if os.path.exists(nombre):
            print(f" {nombre} ya existe, omitiendo...")
        else:
            print(f" Clonando {repo}...")
            subprocess.run(["git", "clone", repo])

if __name__ == "__main__":
    clonar_repositorios(repos)

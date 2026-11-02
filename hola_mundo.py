import os
import sys

def main():
    # Obtiene el usuario de las variables de entorno (compatible con Linux y Windows)
    nombre = os.getenv("USER") or os.getenv("USERNAME") or "Desconocido"
    
    # Detecta el lenguaje y versión que está corriendo (ej. Python 3.11.4)
    lenguaje = f"Python {sys.version.split()[0]}"
    
    print(f"¡Hola, {nombre} desde {lenguaje}!")

if __name__ == "__main__":
    main()

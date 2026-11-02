import os

def main():
    # Si os.getenv devuelve None o texto vacío, usa un valor de respaldo
    nombre = os.getenv("USERNAME")
    lenguaje = os.getenv("LANGUAGE") or "Python"
    
    print(f"¡Hola, {nombre}! Tu lenguaje favorito es {lenguaje}.")

if __name__ == "__main__":
    main()
